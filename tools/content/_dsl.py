"""Compact helpers for the combined guides."""
LV = {"B": "Beginner", "I": "Intermediate", "A": "Advanced", "M": "Master"}


def topics(rows):
    """rows: (level_letter, title, text, code='') tuples."""
    return [{"level": LV[r[0]], "title": r[1], "text": r[2], "code": r[3] if len(r) > 3 else ""} for r in rows]


def G(name, lang, rows, interview, projects):
    return {"name": name, "lang": lang, "topics": topics(rows), "interview": interview, "projects": projects}
