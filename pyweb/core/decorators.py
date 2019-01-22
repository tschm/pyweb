import functools

from flask import Response


def csv(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return Response(value, mimetype="text/csv")

    return wrapper_decorator


def json(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)

        # Do something after
        r = Response(value, mimetype="application/json")
        return r

    return wrapper_decorator

