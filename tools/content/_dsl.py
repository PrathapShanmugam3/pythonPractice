"""Compact helpers for the combined guides."""
LV = {"B": "Beginner", "I": "Intermediate", "A": "Advanced", "M": "Master"}


def topics(rows):
    """rows: (level_letter, title, text, code='') tuples."""
    return [{"level": LV[r[0]], "title": r[1], "text": r[2], "code": r[3] if len(r) > 3 else ""} for r in rows]


def G(name, lang, rows, interview, projects):
    return {"name": name, "lang": lang, "topics": topics(rows), "interview": interview, "projects": projects}


def _split(s):
    return [x.strip() for x in s.split(" | ") if x.strip()]


def apply_extras(topic_list, extras):
    """extras: (syntax, real_en, real_ta, pros, cons, new) aligned with topic_list."""
    assert len(topic_list) == len(extras), (len(topic_list), len(extras))
    for t, (syntax, en, ta, pros, cons, new) in zip(topic_list, extras):
        if syntax:
            t["syntax"] = syntax
        t["real_en"] = en
        if ta:
            t["real_ta"] = ta
        t["pros"], t["cons"], t["new"] = _split(pros), _split(cons), _split(new)
    return topic_list
