# from collections import deque
#
#
# class Stations:
#     def __init__(self, number, fuel_capacity, dist_to_next):
#         self.number = number
#         self.fuel_capacity = fuel_capacity
#         self.dist_to_next = dist_to_next
#
#
# n = int(input())
# stations = deque()
#
# for i in range(n):
#     line = input().split(" ")
#     arg_1, arg_2 = float(line[0]), float(line[1])
#     station = Stations(i, arg_1, arg_2)
#     stations.append(station)
#
# first_station_found = False
# while not first_station_found:
#     available_fuel = 0
#
#     for station in stations:
#         first_station = stations[0].number
#
#         current_station = station.number
#         current_fuel = station.fuel_capacity
#         available_fuel += current_fuel
#         distance_to_cover = station.dist_to_next
#
#         if available_fuel < distance_to_cover:
#             stations.rotate(-1)
#             break
#
#         else:
#             available_fuel -= distance_to_cover
#             if stations.index(station) == n - 1:
#                 first_station_found = True
#                 print(first_station)
#                 break


from collections import deque


class Stations:
    def __init__(self, number, fuel_capacity, dist_to_next):
        self.number = number
        self.fuel_capacity = fuel_capacity
        self.dist_to_next = dist_to_next


number_stations = int(input())
stations = deque()

for station_no in range(number_stations):
    petrol, distance = [int(num) for num in input().split(" ")]
    station = Stations(station_no, petrol, distance)
    stations.append(station)

stations_copy = stations.copy()
available_fuel = 0
first_station = 0

while stations_copy:
    station = stations_copy.popleft()
    first_station = stations[0].number

    available_fuel += station.fuel_capacity

    if available_fuel >= station.dist_to_next:
        available_fuel -= station.dist_to_next
    else:
        stations.rotate(-1)
        available_fuel = 0
        stations_copy = stations.copy()

print(first_station)

### Diyan Kalaidjiev###

# from collections import deque
#
#
# stations = int(input())
# pump_data = deque([int(num) for num in input().split(" ")] for i in range(stations))
#
# pumps_data_copy = pump_data.copy()
# gas_in_tank = 0
# index = 0
#
# while pumps_data_copy:
#     petrol, distance = pumps_data_copy.popleft()
#
#     gas_in_tank += petrol
#
#     if petrol >= distance:
#         gas_in_tank -= distance
#     else:
#         pump_data.rotate(-1)
#         pumps_data_copy = pump_data.copy()
#         index += 1
#         gas_in_tank = 0
#
# print(index)

