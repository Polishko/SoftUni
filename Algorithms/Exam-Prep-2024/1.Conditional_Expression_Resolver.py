# Lecturer`s solution: correct detection of nesting
def parse_expression(expression, idx):
    if expression[idx].isdigit():
        return expression[idx]

    if expression[idx] == 't':
        return parse_expression(expression, idx + 2)

    cursor = idx + 2
    conditional_statements_counter = 0
    while True: # nesting detection
        symbol = expression[cursor]
        if symbol == "?": # nested expression
            conditional_statements_counter += 1
        elif symbol == ':': # end of nested expression
            if conditional_statements_counter == 0:
                return parse_expression(expression, cursor + 1)
            conditional_statements_counter -= 1

        cursor += 1

expression = input().split()
print(parse_expression(expression, 0))

# Initial solution
# input_array = input().split()
#
# output = ''
# while input_array:
#     if input_array[0] == 'f':
#         output = input_array[-1]
#         break
#
#     input_array = input_array[2:len(input_array) - 2]
#     if len(input_array) == 1:
#         output = input_array[0]
#
# print(output)

# Second recursive solution
# def conditional_resolver(input_array):
#     if input_array[0] == 'f':
#         return input_array[-1]
#
#     if len(input_array) == 1:
#         return input_array[0]
#
#     return conditional_resolver(input_array[2:len(input_array) - 2])
#
# print(conditional_resolver(input().split()))
