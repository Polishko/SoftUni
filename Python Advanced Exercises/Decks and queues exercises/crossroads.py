from collections import deque

green_duration = int(input())
free_window = int(input())

cars_waiting = deque()
cars_in_crossroad = deque()
passed_safely = 0
crash = False

while not crash:
    line = input()

    if line == "END":
        break

    if line != "green":
        cars_waiting.append(line)
    else:
        time_left = green_duration
        while cars_waiting:
            current_car = cars_waiting.popleft()
            cars_in_crossroad.append(current_car)
            time_left -= len(current_car)
            if time_left <= 0:
                break

        time_left = green_duration + free_window
        while cars_in_crossroad:
            current_car = cars_in_crossroad.popleft()
            if len(current_car) <= time_left:
                passed_safely += 1
                time_left -= len(current_car)
            else:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[-(len(current_car) - time_left)]}.")
                crash = True
                break

if not crash:
    print("Everyone is safe.")
    print(f"{passed_safely} total cars passed the crossroads.")
