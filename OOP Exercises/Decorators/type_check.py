def type_check(arg):

    def my_decorator(function):

        def wrapper(args):
            if isinstance(args, arg):
                return function(args)
            return "Bad Type"

        return wrapper

    return my_decorator

#test
@type_check(str)
def first_letter(word):
 return word[0]
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
