"""HTML -> PDF rendering for roadmap and topic notes (Chromium shapes Tamil correctly)."""
import html
import re
from pathlib import Path

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ACCENT = "#dd0031"
LEVEL_COLORS = {"Beginner": "#2e7d32", "Intermediate": "#1565c0", "Advanced": "#ef6c00", "Master": "#6a1b9a"}
_fmt = HtmlFormatter(nowrap=True, style="friendly")

CSS = f"""
@page {{ size: A4; margin: 16mm 15mm 18mm 15mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'Noto Sans', 'DejaVu Sans', sans-serif; font-size: 10.5pt; line-height: 1.5; color: #222; }}
.ta {{ font-family: 'Noto Sans Tamil', 'Noto Sans', sans-serif; line-height: 1.8; }}
h1 {{ font-size: 22pt; margin: 0 0 2pt; color: {ACCENT}; }}
h2 {{ font-size: 13pt; margin: 16pt 0 6pt; padding: 3pt 8pt; background: #f4f4f6; border-left: 4px solid {ACCENT};
      break-after: avoid; }}
.badge {{ display: inline-block; padding: 1pt 8pt; border-radius: 10pt; color: #fff; font-size: 9pt; }}
.meta {{ color: #666; font-size: 9.5pt; margin-bottom: 8pt; }}
p {{ margin: 4pt 0 6pt; }}
code {{ font-family: 'DejaVu Sans Mono', monospace; background: #f1f1f4; padding: 0 3px; border-radius: 3px; font-size: 9.5pt; }}
pre {{ font-family: 'DejaVu Sans Mono', monospace; font-size: 8.4pt; line-height: 1.38; background: #f8f8fb;
       border: 1px solid #dcdce4; border-radius: 4px; padding: 7pt 9pt; margin: 4pt 0 8pt; white-space: pre-wrap;
       word-break: break-word; }}
pre.out {{ background: #14141a; color: #d8f5d8; border-color: #14141a; }}
.fname {{ font-family: 'DejaVu Sans Mono', monospace; font-size: 8.8pt; color: #555; margin-top: 6pt; }}
ul, ol {{ margin: 3pt 0 6pt 18pt; padding: 0; }}
li {{ margin-bottom: 3pt; }}
.qa {{ margin: 0 0 7pt; break-inside: avoid; }}
.qa .q {{ font-weight: 700; }}
.tamil {{ background: #fff8e6; border: 1px solid #f0d58a; border-radius: 6px; padding: 8pt 12pt; }}
.note {{ color: #666; font-style: italic; }}
.diagram {{ border: 1px dashed #b9b9c6; border-radius: 6px; padding: 10pt; background: #fcfcfe; text-align: center;
            break-inside: avoid; }}
.row {{ display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 4pt 0; }}
.box {{ border: 1.5px solid {ACCENT}; background: #fff; border-radius: 6px; padding: 5pt 9pt; font-weight: 600;
        font-size: 9.5pt; min-width: 70pt; }}
.box small {{ display: block; font-weight: 400; color: #555; font-size: 8pt; white-space: pre-line; }}
.arrow {{ color: {ACCENT}; font-size: 15pt; padding: 0 5pt; font-weight: 700; }}
.arrow small {{ display: block; font-size: 7.5pt; color: #777; font-weight: 400; margin-top: -3pt; }}
.layer {{ border: 1.5px solid {ACCENT}; background: #fff; border-radius: 6px; padding: 5pt 9pt; margin: 4pt auto;
          max-width: 78%; font-weight: 600; font-size: 9.5pt; }}
.layer small {{ font-weight: 400; color: #555; margin-left: 6pt; }}
.tree ul {{ list-style: none; margin: 0; padding: 0 0 0 0; display: flex; justify-content: center; gap: 8pt; }}
.tree li {{ margin: 0; text-align: center; padding-top: 12pt; position: relative; }}
.tree li > .box {{ display: inline-block; }}
.tree li::before {{ content: ''; position: absolute; top: 0; left: 50%; height: 12pt; border-left: 1.5px solid {ACCENT}; }}
.tree > ul > li::before {{ display: none; }}
.tree > ul > li {{ padding-top: 0; }}
.cap {{ color: #666; font-size: 8.8pt; margin-top: 6pt; }}
table.road {{ width: 100%; border-collapse: collapse; margin-bottom: 8pt; }}
table.road td {{ padding: 4pt 6pt; border-bottom: 1px solid #e4e4ea; vertical-align: top; }}
table.road td.n {{ width: 28pt; color: #888; font-weight: 700; }}
table.road td.t {{ width: 30%; font-weight: 600; }}
.lvl {{ margin-top: 14pt; color: #fff; padding: 5pt 10pt; border-radius: 4px; font-size: 13pt; font-weight: 700;
        break-after: avoid; }}
{_fmt.get_style_defs('.hl')}
.hl {{ color: #222; }}
"""


def inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])", r"<i>\1</i>", t)
    return t


def paras(text):
    if isinstance(text, str):
        text = [text]
    return "".join(f"<p>{inline(p)}</p>" for p in text)


def code_block(code, lang):
    try:
        body = highlight(code.rstrip("\n"), get_lexer_by_name(lang), _fmt)
    except Exception:
        body = html.escape(code)
    return f'<pre class="hl">{body}</pre>'


def _box(step):
    if isinstance(step, (list, tuple)):
        return f'<div class="box">{html.escape(step[0])}<small>{html.escape(step[1])}</small></div>'
    return f'<div class="box">{html.escape(step)}</div>'


def diagram_html(d):
    kind = d["type"]
    if kind == "flow":
        labels = d.get("arrow_labels", [])
        parts = []
        for i, s in enumerate(d["steps"]):
            if i:
                lab = labels[i - 1] if i - 1 < len(labels) else ""
                parts.append(f'<div class="arrow">&rarr;<small>{html.escape(lab)}</small></div>' if lab
                             else '<div class="arrow">&rarr;</div>')
            parts.append(_box(s))
        body = f'<div class="row">{"".join(parts)}</div>'
    elif kind == "layers":
        body = "".join(
            f'<div class="layer">{html.escape(l[0])}<small>{html.escape(l[1]) if len(l) > 1 else ""}</small></div>'
            for l in d["layers"])
    elif kind == "tree":
        def node(n):
            kids = n.get("children", [])
            sub = f"<ul>{''.join(node(k) for k in kids)}</ul>" if kids else ""
            return f"<li>{_box(n['label'] if 'sub' not in n else (n['label'], n['sub']))}{sub}</li>"
        body = f'<div class="tree"><ul>{node(d)}</ul></div>'
    elif kind == "rows":  # several flows stacked, each with an optional title
        body = ""
        for r in d["rows"]:
            body += (f'<div class="cap"><b>{html.escape(r.get("title", ""))}</b></div>' if r.get("title") else "")
            body += diagram_html({"type": "flow", "steps": r["steps"], "arrow_labels": r.get("arrow_labels", [])})
    else:
        raise ValueError(kind)
    cap = f'<div class="cap">{html.escape(d["caption"])}</div>' if d.get("caption") else ""
    return f'<div class="diagram">{body}{cap}</div>'


def topic_html(subject, num, t, programs, outputs):
    """programs: list of program dicts for this topic; outputs: dict key -> output."""
    color = LEVEL_COLORS[t["level"]]
    h = [f"<h1>{num} &middot; {html.escape(t['title'])}</h1>",
         f'<div class="meta"><span class="badge" style="background:{color}">{t["level"]}</span> '
         f'&nbsp; {html.escape(subject)} learning notes</div>']
    h.append("<h2>a. Definition</h2>" + paras(t["definition"]))
    h.append("<h2>b. Diagram</h2>" + diagram_html(t["diagram"]))
    h.append("<h2>c. Syntax</h2>")
    if t.get("syntax"):
        h.append(code_block(t["syntax"], t.get("syntax_lang", "typescript")))
    else:
        h.append('<p class="note">Not applicable for this topic.</p>')
    h.append("<h2>d. Example Program</h2>")
    if programs:
        main = programs[0]
        h.append(f'<div class="fname">Programs/{main["dir"]}/{html.escape(main["file"])}</div>')
        h.append(code_block(main["code"], "typescript"))
        if len(programs) > 1:
            more = ", ".join(f"<code>{html.escape(p['file'])}</code>" for p in programs[1:])
            h.append(f'<p class="note">More programs in the same folder: {more}</p>')
        out_main = outputs[f"{main['dir']}/{main['file']}"]
        out_note = {"component": "Rendered in the browser (text on screen" + (
            ", after the UI steps below" if main.get("actions") else "") + "):",
                    "script": "Console output (run with <code>npx tsx</code>):",
                    "test": "Test report (run with <code>npx vitest run</code>):"}[main["kind"]]
        steps = ""
        if main.get("actions"):
            steps = "<ol>" + "".join(f"<li>{inline(s)}</li>" for s in main.get("action_notes", [])) + "</ol>" \
                if main.get("action_notes") else ""
    else:
        ex = t["example"]
        h.append(code_block(ex["code"], ex.get("lang", "bash")))
        out_main, out_note, steps = ex["output"], "Expected output:", ""
    h.append("<h2>e. Output</h2>")
    h.append(f"<p>{out_note}</p>{steps}<pre class='out'>{html.escape(out_main)}</pre>")
    h.append('<h2>f. Real-World Example in Tamil (தமிழ் உதாரணம்)</h2>')
    h.append(f'<div class="tamil ta">{paras(t["tamil"])}</div>')
    h.append("<h2>g. Common Mistakes</h2><ul>" + "".join(f"<li>{inline(m)}</li>" for m in t["mistakes"]) + "</ul>")
    h.append("<h2>h. Interview Questions</h2>" + "".join(
        f'<div class="qa"><div class="q">Q{i}. {inline(q)}</div><div>{inline(a)}</div></div>'
        for i, (q, a) in enumerate(t["interview"], 1)))
    h.append("<h2>i. Practice Exercises</h2><ol>" + "".join(f"<li>{inline(e)}</li>" for e in t["exercises"]) + "</ol>")
    return page("\n".join(h))


def roadmap_html(subject, topics):
    h = [f"<h1>{html.escape(subject)} &mdash; Zero to Master Roadmap</h1>",
         f'<div class="meta">{len(topics)} topics in learning order. Follow the numbers: read the PDF in '
         f"<b>Notes/</b>, type and run the programs in <b>Programs/</b>, then update the tracker.</div>"]
    for level in ["Beginner", "Intermediate", "Advanced", "Master"]:
        items = [(i, t) for i, t in enumerate(topics, 1) if t["level"] == level]
        if not items:
            continue
        h.append(f'<div class="lvl" style="background:{LEVEL_COLORS[level]}">{level} '
                 f"({len(items)} topics)</div><table class='road'>")
        for i, t in items:
            h.append(f"<tr><td class='n'>{i:02d}</td><td class='t'>{html.escape(t['title'])}</td>"
                     f"<td>{html.escape(t['summary'])}</td></tr>")
        h.append("</table>")
    return page("\n".join(h))


def page(body):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"


def write_pdfs(jobs):
    """jobs: list of (html_string, Path). One Chromium launch for all."""
    from playwright.sync_api import sync_playwright

    footer = ("<div style='font-size:8px;width:100%;text-align:center;color:#888'>"
              "<span class='pageNumber'></span> / <span class='totalPages'></span></div>")
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = browser.new_page()
        for content, path in jobs:
            path.parent.mkdir(parents=True, exist_ok=True)
            pg.set_content(content)
            pg.pdf(path=str(path), format="A4", print_background=True, display_header_footer=True,
                   header_template="<span></span>", footer_template=footer,
                   margin={"top": "16mm", "bottom": "18mm", "left": "15mm", "right": "15mm"})
        browser.close()
