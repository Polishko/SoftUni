from collections import deque

n = int(input())
stations = deque()
fuel = deque()
distance = deque()

for i in range(n):
    line = input().split(" ")
    arg_1, arg_2 = float(line[0]), float(line[1])
    stations.append(i)
    fuel.append(arg_1)
    distance.append(arg_2)

first_station_found = False
first_station = 0
while not first_station_found:
    available_fuel = 0

    for i in range(n):
        current_station = stations.popleft()
        current_fuel = fuel.popleft()
        available_fuel += current_fuel
        distance_to_next = distance.popleft()

        stations.append(current_station)
        fuel.append(current_fuel)
        distance.append(distance_to_next)

        if available_fuel < distance_to_next:
            first_station += 1

            while True:
                if stations[0] == first_station:
                    break
                stations.rotate(-1)
                fuel.rotate(-1)
                distance.rotate(-1)
            break

        else:
            available_fuel -= distance_to_next

        if i == n - 1:
            first_station_found = True
            print(first_station)
            break
