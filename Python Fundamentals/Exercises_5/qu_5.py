no_rooms = int(input())
free_chairs = 0
chairs_needed = False

for room_no in range(1, no_rooms + 1):
    info_lst = input().split(" ")

    available_chairs = len(info_lst[0])
    visitors = int(info_lst[1])

    if available_chairs < visitors:
        chairs_needed = True
        print(f"{visitors - available_chairs} more chairs needed in room {room_no}")
    elif visitors < available_chairs:
        free_chairs += (available_chairs - visitors)

if not chairs_needed:
    print(f"Game On, {free_chairs} free chairs left")
