def T(name, level, en, ta, code="", yt_q=None, refs=()):
    return dict(name=name, level=level, en=en, ta=ta, code=code, yt=yt_q or name + " tutorial", refs=list(refs))
B, I, A = "Beginner", "Intermediate", "Advanced"
