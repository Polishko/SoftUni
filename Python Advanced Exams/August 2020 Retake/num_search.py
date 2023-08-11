def numbers_searching(*args):
    nums = list(args)
    all_range = set(range(min(nums), max(nums) + 1))
    missing = sorted(list(all_range.difference(nums)))

    duplicates = {}
    for num in nums:
        if num not in duplicates:
            duplicates[num] = 0
        duplicates[num] += 1

    return [missing[-1], sorted([num for num in duplicates if duplicates[num] > 1])]
