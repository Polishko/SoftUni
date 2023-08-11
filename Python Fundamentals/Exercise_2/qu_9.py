snow_ball_count = int(input())
current_weight, current_time, current_quality = 0, 0, 0
max_value = 0

for _ in range(1, snow_ball_count + 1):
    weight_ball = int(input())
    time_to_target = int(input())
    quality_ball = int(input())

    value = int((weight_ball / time_to_target) ** quality_ball)
    if value > max_value:
        max_value = value
        current_weight = weight_ball
        current_time = time_to_target
        current_quality = quality_ball

print(f"{current_weight} : {current_time} = {max_value} ({current_quality})")
