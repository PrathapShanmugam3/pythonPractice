#!/usr/bin/env python3
"""Build <Subject>/<Subject>_Zero_to_Master.pdf for every subject in tools/content/guides_*.py

    python tools/build_guides.py            # all subjects
    python tools/build_guides.py Java Git   # selected subjects
"""
import importlib
import pkgutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import content  # noqa: E402
from learning import guide, render  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def all_guides():
    from content import extras_backend, extras_data, extras_js, extras_node, extras_tools
    from content._dsl import apply_extras
    extras = {
        "JavaScript": extras_js.JAVASCRIPT, "TypeScript": extras_js.TYPESCRIPT, "React": extras_js.REACT,
        "Next.js": extras_node.NEXTJS, "Node.js": extras_node.NODEJS, "Express.js": extras_node.EXPRESS,
        "Java": extras_backend.JAVA, "Spring Boot": extras_backend.SPRINGBOOT,
        "Python": extras_backend.PYTHON, "FastAPI": extras_backend.FASTAPI,
        "MySQL": extras_data.MYSQL, "PostgreSQL": extras_data.POSTGRESQL, "MongoDB": extras_data.MONGODB,
        "Git": extras_tools.GIT, "GitLab": extras_tools.GITLAB, "GitHub": extras_tools.GITHUB,
        "DevOps": extras_tools.DEVOPS, "AI ML": extras_tools.AIML,
    }
    out = []
    for m in pkgutil.iter_modules(content.__path__):
        if m.name.startswith("guides_"):
            for g in importlib.import_module(f"content.{m.name}").GUIDES:
                apply_extras(g["topics"], extras[g["name"]])
                out.append(g)
    from content import angular_guide
    out.insert(0, angular_guide.build())
    return out


def main():
    want = {a.lower() for a in sys.argv[1:]}
    jobs = []
    for g in all_guides():
        if want and g["name"].lower() not in want:
            continue
        folder = g["name"].replace(" ", "_").replace("/", "_")
        jobs.append((guide.guide_html(g), REPO / folder / f"{folder}_Zero_to_Master.pdf"))
    render.write_pdfs(jobs)
    for _, p in jobs:
        print("wrote", p.relative_to(REPO))


if __name__ == "__main__":
    main()
