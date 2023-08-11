from collections import deque
import time
PRODUCT_TIME_INTERVAL = 1


class Robots:
    def __init__(self, name, processing_time, process_ending_time):
        self.name = name
        self.processing_time = processing_time
        self.process_ending_time = process_ending_time


def start_time(start):
    time_tokens = start.split(":")
    start_secs = int(time_tokens[0]) * 3600 + int(time_tokens[1]) * 60 + int(time_tokens[2])
    return start_secs


robots = deque()
robot_tokens = input().split(";")

for robot in robot_tokens:
    name_robot, processing = robot.split("-")
    robots.append(Robots(name_robot, int(processing), 0))

current_time = start_time(input())
products = deque()

while True:
    line = input()

    if line == "End":
        break

    products.append(line)

while products:
    current_product = products.popleft()
    current_time += PRODUCT_TIME_INTERVAL

    for robot in robots:

        if current_time >= robot.process_ending_time:
            product_taken_at = time.strftime("%H:%M:%S", time.gmtime(current_time))
            print(f"{robot.name} - {current_product} [{product_taken_at}]")
            robot.process_ending_time = current_time + robot.processing_time
            break

    else:
        products.append(current_product)
