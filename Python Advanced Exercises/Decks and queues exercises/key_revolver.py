from collections import deque


def load_barrel(gun_bullets, gun_barrel, size):
    for _ in range(size):
        if not gun_bullets:
            break
        gun_bullet = gun_bullets.pop()
        gun_barrel.appendleft(gun_bullet)


bullet_cost = int(input())
barrel_size = int(input())
barrel = deque()
bullets = list(map(int, input().split(" ")))
initial_bullets = len(bullets)
locks = deque(map(int, input().split(" ")))
intelligence = int(input())

load_barrel(bullets, barrel, barrel_size)

while locks:
    if barrel:
        current_lock = locks.popleft()
        current_bullet = barrel.pop()

        if current_bullet <= current_lock:
            print("Bang!")
        else:
            print("Ping!")
            locks.appendleft(current_lock)

    else:
        if bullets:
            print("Reloading!")
            load_barrel(bullets, barrel, barrel_size)
        else:
            break

if not locks:
    bullets_left = len(bullets) + len(barrel)
    bullet_cost = (initial_bullets - bullets_left) * bullet_cost
    earned = intelligence - bullet_cost
    print(f"{bullets_left} bullets left. Earned ${earned}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
