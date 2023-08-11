def cache(function):
    log = {}

    def wrapper(arg):
        n = function(arg)
        if arg not in log:
            log[arg] = n

        return log[arg]

    wrapper.log = log

    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# alternative solution from lecture
# def cache(function):

#     def wrapper(arg):
#         if not wrapper.log.get(arg):
#             wrapper.log[arg] = function(arg)

#         return wrapper.log[arg]

#     wrapper.log = {}


# @cache
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

