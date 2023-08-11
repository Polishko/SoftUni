# def age_assignment(*args, **kwargs):
#     people = {}
#     results = []
#
#     for name in args:
#         if name[0] in kwargs:
#             people[name] = kwargs[name[0]]
#
#     sorted_people = sorted(people.items())
#
#     for item in sorted_people:
#         results.append(f"{item[0]} is {item[1]} years old.")
#
#     return "\n".join(results)



# iki nested for cycle
##result = []
# for leter, age in dict
    #person_name = ""
    # for name in names:
      # if name.startswith(letter) result append



def age_assignment(*args, **kwargs):
    results = []

    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                results.append(f"{name} is {age} years old.")

    return "\n".join(sorted(results))


print(age_assignment("Peter", "George", G=26, P=19))