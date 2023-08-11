def tags(tag):

    def my_decorator(function):

        def wrapper(*args):
            return f"<{tag}>{function(*args)}</{tag}>"

        return wrapper

    return my_decorator

# test case
@tags('p')
def join_strings(*args):
 return "".join(args)
print(join_strings("Hello", " you!"))
