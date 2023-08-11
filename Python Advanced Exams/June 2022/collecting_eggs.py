from collections import deque


eggs = deque(int(x) for x in input().split(", "))
paper_pieces = deque(int(x) for x in input().split(", "))

boxes = 0
while eggs and paper_pieces:
    egg = eggs.popleft()

    if egg <= 0:
        continue
    if egg == 13:
        paper_pieces[0], paper_pieces[-1] = paper_pieces[-1], paper_pieces[0]
        continue

    paper = paper_pieces.pop()

    if egg + paper <= 50:
        boxes += 1

print(f"Great! You filled {boxes} boxes.") if boxes >= 1 else print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if paper_pieces:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_pieces)}")
