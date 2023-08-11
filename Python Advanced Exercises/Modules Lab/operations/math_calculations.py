def operation(*args):
    a, sign, b = args
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Please enter numbers only!")

    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        if a == 0 or b == 0:
            print("Cannot perform zero division or division by zero!")
        else:
            return a / b

    elif sign == "^":
        return a**b
    else:
        print("Operation not defined!")

# her operasyon icin fonksiyon yazdi return a + b

# mapper = {"+": fnct_adi,...} ama call etmeden yani () olmadan
# def execution fnc(expression):
    # a, sign, b = expression.split(" ")
    # return mapper[key](a, b) artik burada call ediyor icine a b koyarak
