# def concatenate(*args, **kwargs):
#     concatenation = "" # join ile yapti tek satir if yok text =
#
#     for arg in args:
#         concatenation += arg
#
#     for key in kwargs: # for key, value... text = replace...
#         if key in concatenation:
#             concatenation = concatenation.replace(key, kwargs[key])
#
#     return concatenation
#
# print(concatenate("I", " ", "Love", " ", "Cythons",
# C="P", s="", java='Java'))


def concatenate(*args, **kwargs):
    text = "".join(args)

    for key, value in kwargs.items():
        text = text.replace(key, kwargs[key])

    return text

print(concatenate("Soft", "UNI", "Is", "Grate", "!",
UNI="Uni", Grate="Great"))