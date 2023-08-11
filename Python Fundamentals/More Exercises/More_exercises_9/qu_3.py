import re
n = int(input())
pattern_decrypt = re.compile(r"[starSTAR]")
pattern_info = re.compile(r"@(?P<planet>[A-Za-z]+)([^@\-!:>])*:(?P<population>[\d+)([^@\-!:>])*!"
                          r"(?P<attack>[AD])!([^@\-!:>])*->(?P<count>\d+)")

attacked_planets = []
destroyed_planets = []
decrypted_lines = []

for _ in range(n):
    line = input()

    count = len(re.findall(pattern_decrypt, line))

    decrypted_line = ""
    for char in line:
        decrypted_line += chr(ord(char) - count)

    decrypted_lines.append(decrypted_line)

    planets = re.finditer(pattern_info, decrypted_line)

    for planet in planets:
        if planet.group("attack") == "A":
            attacked_planets.append(planet.group("planet"))
        elif planet.group("attack") == "D":
            destroyed_planets.append(planet.group("planet"))

attacked_planets = list(sorted(attacked_planets))
destroyed_planets= list(sorted(destroyed_planets))

print(f"Attacked planets: {len(attacked_planets)}")
for item in attacked_planets:
    print(f"-> {item}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for item in destroyed_planets:
    print(f"-> {item}")
