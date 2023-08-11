from collections import deque


tools = deque(int(x) for x in input().split(" "))
substances = deque(int(x) for x in input().split(" "))
challenges = deque(int(x) for x in input().split(" "))

while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances.pop()
    product = tool * substance

    if product in challenges:
        challenges.remove(product)
    else:
        tools.append(tool + 1)
        substance -= 1
        if substance > 0:
            substances.append(substance)

    if (not tools or not substances) and challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break
    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
