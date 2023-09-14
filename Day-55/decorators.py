

def make_bold(function):
    def wrapper():
        result = function()
        return f"<b>{result}</b>"

    return wrapper


def make_italics(function):
    def wrapper():
        result = function()
        return f"<em>{result}</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        result = function()
        return f"<u>{result}</u"

    return wrapper

