def make_bold(function):

    def wrapper(*arg):
        return f"<b>{function(*arg)}</b>"

    return wrapper


def make_italic(function):
    def wrapper(*arg):
        return f"<i>{function(*arg)}</i>"

    return wrapper


def make_underline(function):
    def wrapper(*arg):
        return f"<u>{function(*arg)}</u>"

    return wrapper


# test
@make_bold
@make_italic
@make_underline
def greet_all(*args):
 return f"Hello, {', '.join(args)}"
print(greet_all("Peter", "George"))
