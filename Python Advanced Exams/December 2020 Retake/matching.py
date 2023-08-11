from collections import deque


def take_person(a, gender):
    person_found = False
    person = ""

    while not person_found and a:
        if gender == "males":
            person = a.pop()
        else:
            person = a.popleft()
        if person <= 0:
            person = ""
            continue
        if person % 25 == 0 and a:
            person = ""
            if gender == "males":
                a.pop()
            else:
                a.popleft()
            continue
        else:
            person_found = True

    return person


def print_group(a, gender):
    insert = "Males" if gender == "males" else "Females"
    b = list(reversed(a)) if gender == "males" else a

    if not a:
        print(f"{insert} left: none")
    else:
        print(f"{insert} left: {', '.join(str(b[i]) for i in range(len(b)))}")


males = deque(int(x) for x in input().split(" "))
females = deque(int(x) for x in input().split(" "))
matches = 0

while males and females:
    male = take_person(males, gender="males")
    female = take_person(females, gender="females")

    if not female or not male:
        if not male and female:
            females.appendleft(female)
        elif not female and male:
            males.append(male)
        break

    if male == female:
        matches += 1
    else:
        males.append(male - 2)

print(f"Matches: {matches}")
print_group(males, gender="males")
print_group(females, gender="females")
