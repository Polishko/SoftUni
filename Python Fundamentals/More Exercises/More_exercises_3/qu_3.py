from math import ceil
from decimal import Decimal

input_string = input()
input_list = input_string.split(" ")
num_list = [int(num) for num in input_list]

length = len(num_list)
mid = ceil(len(num_list) / 2)
total_time_left, total_time_right = 0, 0

for step in range(0, mid - 1):
    time_left = num_list[step]

    if time_left == 0:
        total_time_left *= 0.80

    total_time_left += time_left

for step in range(length - 1, mid - 1, -1):
    time_right = num_list[step]

    if time_right == 0:
        total_time_right *= 0.80

    total_time_right += time_right

if total_time_left < total_time_right:
    winner = "left"
    time_winner = total_time_left
else:
    winner = "right"
    time_winner = total_time_right

print(f"The winner is {winner} with total time: {time_winner:.1f}")
