"""One combined 'Zero to Master' PDF per subject (all topics, grouped by level)."""
import html

from .render import LEVEL_COLORS, code_block, inline, lists_html, page, paras, realworld_html

LEVELS = ["Beginner", "Intermediate", "Advanced", "Master"]


def guide_html(g):
    """g: dict(name, lang, topics=[dict(level,title,text,code?,lang?,mistakes?,interview?,exercises?)],
    interview=[(q,a)], projects=[str])"""
    topics = g["topics"]
    h = [f"<h1>{html.escape(g['name'])} &mdash; Zero to Master</h1>",
         f'<div class="meta">{len(topics)} topics, grouped as Beginner &rarr; Intermediate &rarr; Advanced &rarr; Master. '
         "Work through the topics in order; type every code example yourself and finish the practice tasks.</div>",
         "<h2>Contents</h2>"]
    n = 0
    toc = ""
    for lvl in LEVELS:
        items = [t for t in topics if t["level"] == lvl]
        if not items:
            continue
        toc += f'<div class="lvl" style="background:{LEVEL_COLORS[lvl]}">{lvl} ({len(items)} topics)</div><table class="road">'
        for t in items:
            n += 1
            toc += f"<tr><td class='n'>{n:02d}</td><td>{html.escape(t['title'])}</td></tr>"
        toc += "</table>"
    h.append(toc)
    n = 0
    cur = None
    for t in topics:
        n += 1
        if t["level"] != cur:
            cur = t["level"]
            h.append(f'<div class="lvl" style="background:{LEVEL_COLORS[cur]};page-break-before:always">'
                     f"{cur} Level</div>")
        h.append(f'<h2>{n:02d}. {html.escape(t["title"])}</h2>')
        h.append('<p class="lab">Definition</p>' + paras(t["text"]))
        lang = t.get("lang", g["lang"])
        if t.get("syntax"):
            h.append('<p class="lab">Syntax</p>' + code_block(t["syntax"], t.get("syntax_lang", lang)))
        if t.get("code"):
            h.append('<p class="lab">Example</p>' + code_block(t["code"], lang))
        if t.get("real_en"):
            h.append('<p class="lab">Real-World Example (English + தமிழ்)</p>' + realworld_html(t))
        for title, body in lists_html(t):
            h.append(f'<p class="lab">{title}</p>{body}')
        if t.get("mistakes"):
            h.append("<p><b>Common mistakes</b></p><ul>" + "".join(f"<li>{inline(m)}</li>" for m in t["mistakes"]) + "</ul>")
        if t.get("interview"):
            h.append("<p><b>Interview questions</b></p>" + "".join(
                f'<div class="qa"><div class="q">Q{i}. {inline(q)}</div><div>{inline(a)}</div></div>'
                for i, (q, a) in enumerate(t["interview"], 1)))
        if t.get("exercises"):
            h.append("<p><b>Practice</b></p><ol>" + "".join(f"<li>{inline(e)}</li>" for e in t["exercises"]) + "</ol>")
        elif t.get("practice"):
            h.append(f"<p><b>Practice:</b> {inline(t['practice'])}</p>")
    h.append('<div class="lvl" style="background:#37474f;page-break-before:always">Interview Question Bank</div>')
    for i, (q, a) in enumerate(g.get("interview", []), 1):
        h.append(f'<div class="qa"><div class="q">Q{i}. {inline(q)}</div><div>{inline(a)}</div></div>')
    h.append('<div class="lvl" style="background:#37474f">Capstone Project Ideas</div><ol>'
             + "".join(f"<li>{inline(p)}</li>" for p in g.get("projects", [])) + "</ol>")
    return page("\n".join(h))
