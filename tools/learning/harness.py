"""Build and run every Angular example program, and capture its real output.

Program kinds (set per program in the content file):
  support   - extra file (e.g. a lazy-loaded component); compiled with the rest, not run alone.
  component - Angular standalone component with selector 'app-root'. Compiled with
              AOT + strictTemplates, bootstrapped in headless Chromium, and the
              rendered text (after optional UI `actions`) is the output.
  script    - plain TypeScript, executed with tsx; stdout is the output.
  test      - Vitest spec file; the test report is the output.
"""
import http.server
import json
import re
import shutil
import socketserver
import subprocess
import threading
from pathlib import Path

HARNESS = Path(__file__).resolve().parent.parent / "angular_harness"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def _key(p):
    return f"{p['dir']}/{p['file']}"


def _root_class(code):
    m = re.search(r"selector:\s*'app-root'[\s\S]*?export class (\w+)", code)
    if not m:
        raise SystemExit("component program needs selector 'app-root': " + code[:80])
    return m.group(1)


def _prepare(programs):
    progdir = HARNESS / "src" / "programs"
    shutil.rmtree(progdir, ignore_errors=True)
    entries = []
    for p in programs:
        f = progdir / p["dir"] / p["file"]
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(p["code"])
        if p["kind"] == "component":
            cls = _root_class(p["code"])
            entries.append(
                f"  '{_key(p)}': () => import('./programs/{p['dir']}/{p['file'][:-3]}')"
                f".then((m: any) => ({{ component: m.{cls}, appConfig: m.appConfig }})),"
            )
    (HARNESS / "src" / "registry.ts").write_text(
        "export const registry: Record<string, () => Promise<{ component: any; appConfig?: any }>> = {\n"
        + "\n".join(entries) + "\n};\n"
    )
    (HARNESS / "src" / "main.ts").write_text(
        "import { bootstrapApplication } from '@angular/platform-browser';\n"
        "import { registry } from './registry';\n"
        "const key = new URLSearchParams(location.search).get('p')!;\n"
        "registry[key]().then(({ component, appConfig }) =>\n"
        "  bootstrapApplication(component, appConfig ?? {}).catch(e => console.error(e)));\n"
    )


def _run(cmd, **kw):
    return subprocess.run(cmd, cwd=HARNESS, capture_output=True, text=True, **kw)


def _clean(text):
    lines = [l.rstrip() for l in text.splitlines()]
    return "\n".join(l for l in lines if l)


def _browser_outputs(programs, outputs, errors):
    from playwright.sync_api import sync_playwright

    dist = HARNESS / "dist" / "browser"

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(dist), **k)

        def log_message(self, *a):
            pass

    srv = socketserver.TCPServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    cors = {"access-control-allow-origin": "*", "access-control-allow-headers": "*",
            "access-control-allow-methods": "*"}
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        for p in programs:
            if p["kind"] != "component":
                continue
            page = browser.new_page()
            problems = []
            page.on("pageerror", lambda e: problems.append(str(e)))
            page.on("console", lambda m: problems.append(m.text) if m.type == "error" else None)
            mocks = p.get("mocks", {})

            def api(route, _request=None, mocks=mocks):
                req = route.request
                if req.method == "OPTIONS":
                    return route.fulfill(status=204, headers=cors)
                for frag, spec in mocks.items():
                    if frag in req.url:
                        status = 200
                        body = spec
                        if isinstance(spec, dict) and "__status" in spec:
                            status, body = spec["__status"], spec.get("body", {})
                        return route.fulfill(status=status, headers=cors,
                                             content_type="application/json", body=json.dumps(body))
                route.fulfill(status=404, headers=cors, body="{}")

            page.route("**/api.example.com/**", api)
            page.goto(f"http://127.0.0.1:{port}/?p={_key(p)}")
            page.wait_for_selector("app-root > *", state="attached", timeout=10000)
            page.wait_for_timeout(500)
            snaps = []
            for act in p.get("actions", []):
                op = act[0]
                if op == "snap":
                    snaps.append(f"--- {act[1]} ---\n" + _clean(page.inner_text("app-root")))
                elif op == "hover":
                    page.hover(act[1])
                elif op == "click":
                    page.click(act[1])
                elif op == "fill":
                    page.fill(act[1], act[2])
                elif op == "select":
                    page.select_option(act[1], act[2])
                elif op == "wait":
                    page.wait_for_timeout(act[1])
                page.wait_for_timeout(120)
            page.wait_for_timeout(300)
            outputs[_key(p)] = "\n\n".join(snaps) if snaps else _clean(page.inner_text("app-root"))
            if p.get("expect_http_errors"):
                problems = [m for m in problems if "Failed to load resource" not in m]
            if problems:
                errors.append(f"{_key(p)}: {problems}")
            page.close()
        browser.close()
    srv.shutdown()


def run_all(programs):
    """Return {program key: output text}. Raises SystemExit if anything fails."""
    _prepare(programs)
    outputs, errors = {}, []
    r = _run(["npx", "ng", "build", "--configuration", "development"])
    if r.returncode:
        raise SystemExit("ng build failed:\n" + r.stdout[-6000:] + r.stderr[-3000:])
    _browser_outputs(programs, outputs, errors)
    for p in programs:
        path = f"src/programs/{p['dir']}/{p['file']}"
        if p["kind"] == "script":
            r = _run(["npx", "tsx", path])
            if r.returncode:
                errors.append(f"{_key(p)} failed:\n{r.stderr}")
            outputs[_key(p)] = r.stdout.strip()
        elif p["kind"] == "test":
            r = _run(["npx", "vitest", "run", path, "--reporter=verbose"],
                     env={**__import__("os").environ, "NO_COLOR": "1", "CI": "1"})
            if r.returncode:
                errors.append(f"{_key(p)} failed:\n{r.stdout}{r.stderr}")
            lines = [l for l in (r.stdout + r.stderr).splitlines()
                     if l.strip() and "RUN" not in l and "Duration" not in l and "Start at" not in l]
            outputs[_key(p)] = "\n".join(lines)
    if errors:
        raise SystemExit("PROGRAM ERRORS:\n" + "\n".join(errors))
    return outputs
