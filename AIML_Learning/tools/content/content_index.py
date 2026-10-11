import importlib, pkgutil, os
def load():
    d = os.path.dirname(os.path.abspath(__file__))
    names = sorted(n for _, n, _ in pkgutil.iter_modules([d]) if n.startswith("m"))
    return [importlib.import_module(n) for n in names]
