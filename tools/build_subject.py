#!/usr/bin/env python3
"""Build a learning folder for a subject from tools/content/<subject>.py

    python tools/build_subject.py angular            # compile+run programs, write everything
    python tools/build_subject.py angular --skip-run  # reuse cached outputs (fast PDF/tracker tweaks)

Output goes to <repo>/<Subject>/ : 00_Roadmap.pdf, Notes/, Programs/, <Subject>_Tracker.xlsx
Re-running updates the existing folder (never duplicates); tracker progress is preserved.
"""
import importlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from learning import harness, render, tracker  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def main():
    name = sys.argv[1]
    mod = importlib.import_module(f"content.{name}")
    subject, topics = mod.SUBJECT, mod.TOPICS
    root = REPO / subject
    nums = {t["slug"]: f"{i:02d}" for i, t in enumerate(topics, 1)}

    programs = []
    for t in topics:
        for p in t.get("programs", []):
            programs.append({**p, "dir": f"{nums[t['slug']]}_{t['slug']}"})

    cache = REPO / "tools" / "angular_harness" / "outputs.json"
    if "--skip-run" in sys.argv:
        outputs = json.loads(cache.read_text())
    else:
        outputs = harness.run_all(programs)
        cache.write_text(json.dumps(outputs, indent=1))
    print(f"{len(programs)} programs verified")

    # Programs/
    for p in programs:
        f = root / "Programs" / p["dir"] / p["file"]
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(p["code"])

    jobs = [(render.roadmap_html(subject, topics), root / "00_Roadmap.pdf")]
    rows = []
    for i, t in enumerate(topics, 1):
        pdf = f"{nums[t['slug']]}_{t['slug']}.pdf"
        progs = [p for p in programs if p["dir"] == f"{nums[t['slug']]}_{t['slug']}"]
        jobs.append((render.topic_html(subject, nums[t["slug"]], t, progs, outputs), root / "Notes" / pdf))
        rows.append({"topic": t["title"], "level": t["level"], "notes_pdf": pdf,
                     "programs": [p["file"] for p in progs]})
    render.write_pdfs(jobs)
    tracker.write_tracker(root / f"{subject}_Tracker.xlsx", subject, rows)
    print(f"Built {root}: {len(topics)} topics")


if __name__ == "__main__":
    main()
