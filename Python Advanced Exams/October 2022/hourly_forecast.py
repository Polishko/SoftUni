def forecast(*args):
    sunny, rainy, cloudy = [], [], []
    result = []

    for arg in args:
        if arg[1] == "Sunny":
            sunny.append(f"{arg[0]} - Sunny")
        elif arg[1] == "Rainy":
            rainy.append(f"{arg[0]} - Rainy")
        if arg[1] == "Cloudy":
            cloudy.append(f"{arg[0]} - Cloudy")

    result += sorted(sunny) + sorted(cloudy) + sorted(rainy)
    return "\n".join(result)
