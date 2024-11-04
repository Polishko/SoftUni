from collections import deque


def word_cruncher(pieces, target, result, combinations):
    # base cases
    if len(''.join(result)) > len(target):
        return

    if ''.join(result) == target:
        combinations.add(' '.join(result))
        return

    for _ in range(len(pieces)):
        piece = pieces.popleft()
        result.append(piece)

        # continue searching if match
        if target.startswith(''.join(result)):
            word_cruncher(pieces, target, result, combinations)

        # backtracking
        result.pop()
        pieces.append(piece)


def rotate_words(pieces, target):
    combinations = set()
    for _ in range(len(pieces)):
        pieces.rotate(-1)
        word_cruncher(deque(pieces), target, [], combinations)

    for combination in combinations:
        print(''.join(combination))


pieces = deque(input().split(', '))
target = input()

rotate_words(pieces, target)
