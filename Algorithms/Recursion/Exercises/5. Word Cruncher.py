from collections import deque


def word_cruncher(pieces, target, result, combinations):
    if len(''.join(result)) > len(target):
        return

    if ''.join(result) == target and ' '.join(result) not in combinations:
        combinations.append(' '.join(result))
        return

    for _ in range(len(pieces)):
        piece = pieces.popleft()
        result.append(piece)

        if target.startswith(''.join(result)):
            word_cruncher(pieces, target, result, combinations)

        result.pop()
        pieces.append(piece)


def rotate_words(pieces, target):
    combinations = []
    for _ in range(len(pieces)):
        pieces.rotate(-1)
        word_cruncher(pieces, target, [], combinations)

    for combination in combinations:
        print(''.join(combination))


pieces = deque(input().split(', '))
target = input()

rotate_words(pieces, target)
