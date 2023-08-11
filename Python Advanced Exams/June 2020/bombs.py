from collections import deque


def make_bomb(effects, casings):
    effect, casing = bomb_effects[0], bomb_casings.pop()
    for bomb in bombs:
        if effect + casing == bombs[bomb][0]:
            bombs[bomb][1] += 1
            bomb_effects.popleft()
            break
    else:
        bomb_casings.append(casing - 5)


bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = deque(int(x) for x in input().split(", "))


bombs = {
    "Cherry": [60, 0],
    "Datura": [40, 0],
    "Smoke Decoy": [120, 0]
}

while bomb_effects and bomb_casings:
    if all([bombs[bomb_type][1] >= 3 for bomb_type in bombs]):
        print("Bene! You have successfully filled the bomb pouch!")
        break

    make_bomb(bomb_effects, bomb_casings)

else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}") if bomb_effects else print("Bomb Effects: empty")
print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}") if bomb_casings else print("Bomb Casings: empty")

[print(f"{bomb} Bombs: {bombs[bomb][1]}") for bomb in bombs]
