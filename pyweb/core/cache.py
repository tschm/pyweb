from pyweb.exts.exts import cache


def read_cache(name, fct=None):
    """ read from cache """
    frame = cache.get(name)
    if frame is None:
        frame = fct()
        cache.set(name, frame)
    return frame
