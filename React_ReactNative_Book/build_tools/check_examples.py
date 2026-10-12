"""Runs every ```js block in src/*.md with node (modules as .mjs) and prints output."""
import re, subprocess, sys, glob, os, tempfile
d = tempfile.mkdtemp()
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "..", "src", "*.md"))):
    t = open(f, encoding="utf-8").read()
    for i, m in enumerate(re.finditer(r"```js\n(.*?)```", t, re.S)):
        code = m.group(1)
        if "===== File" in code:
            name = re.search(r"File \d: (\S+) =====", code).group(1)
            open(os.path.join(d, name), "w").write(code)
            continue
        p = os.path.join(d, "ex_%s_%d.mjs" % (os.path.basename(f)[:2], i))
        open(p, "w", encoding="utf-8").write(code)
        r = subprocess.run(["node", p], capture_output=True, text=True, cwd=d, timeout=20)
        print("=== %s #%d rc=%d" % (os.path.basename(f), i, r.returncode)); print(r.stdout + r.stderr)
    if os.path.exists(os.path.join(d, "main.mjs")):
        r = subprocess.run(["node", "main.mjs"], capture_output=True, text=True, cwd=d)
        print("=== main.mjs", r.stdout, r.stderr)
