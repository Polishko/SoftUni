from collections import deque
import time
PRODUCT_TIME_INTERVAL = 1


class Robots:
    def __init__(self, name, processing_time, end_processing):
        self.name = name
        self.processing_time = processing_time
        self.end_processing = end_processing


def get_robot_name(item):
    name_item = item.split("-")[0]
    return name_item


def get_robot_process_time(item):
    processing_time = float(item.split("-")[1])
    return processing_time


def start_time(start):
    time_tokens = start.split(":")
    start_secs = int(time_tokens[0]) * 3600 + int(time_tokens[1]) * 60 + int(time_tokens[2])
    return start_secs


robots = []
robot_tokens = input().split(";")
end_working = 0
for robot in robot_tokens:
    name_robot = get_robot_name(robot)
    processing = get_robot_process_time(robot)
    robots.append(Robots(name_robot, processing, end_working))

starting_time = start_time(input())

products = deque()
while True:
    line = input()

    if line == "End":
        break

    products.append(line)

current_process_time = starting_time
while products:
    current_product = products.popleft()
    current_process_time += PRODUCT_TIME_INTERVAL

    for robot in robots:
        if current_process_time >= robot.end_processing and robot.end_processing != 0:
            robot.end_processing = 0

    product_processed = False
    for robot in robots:   # burada neden ikinci ayni sey var yukaridakine ekle bunu ayni cycle bu
        if robot.end_processing == 0:
            product_taken_at = time.strftime("%H:%M:%S", time.gmtime(current_process_time))
            print(f"{robot.name} - {current_product} [{product_taken_at}]")
            product_processed = True
            end_working = current_process_time + robot.processing_time
            robot.end_processing = end_working
            break
    if not product_processed: # ya da break icin else caluse yazilabilir
        products.append(current_product)
