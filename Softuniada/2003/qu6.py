nums = [int(num) for num in input().split(' ')]


def select_piece(pieces_list):
    max_sum = float('-inf')
    max_start = max_end = 0
    current_sum = 0
    current_start = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum > max_sum or (current_sum == max_sum and i - current_start > max_end - max_start):
            max_sum = current_sum
            max_start = current_start
            max_end = i

        if current_sum < 0: #avoid negative sum and restart sequence
            current_sum = 0
            current_start = i + 1

    return f'{max_sum} {max_start} {max_end}'


print(select_piece(nums))

# nums = [int(num) for num in input().split(' ')]
#
# split_length = len(nums) // 2
# mid_element = nums[split_length] if len(nums) % 2 != 0 else None
#
# left = nums[:split_length]
# right = nums[split_length:]
#
# lst = [nums, left, right]
# select = sorted(lst, key=lambda x: -sum(x))[0]
#
# if mid_element:
#     select = select.append(mid_element) if mid_element > 0 else select
#
# print(select)

# nums = [int(num) for num in input().split(' ')]
# selected = []
#
#
# def sort_key(x):
#     return -x[0], -(x[2] - x[1]), x[1]
#
#
# def find_most_desirable(pieces):
#     return sorted(pieces, key=sort_key)
#
#
# def select_piece(pieces_list):
#     for i in range(len(nums)):
#         for k in range(len(nums)):
#             piece = nums[i:k + 1]
#             selected.append((sum(piece), i, k + 1))
#
#     most_desired = find_most_desirable(selected)[0]
#
#     return f'{most_desired[0]} {most_desired[1]} {most_desired[2] - 1}'
#
#
# print(select_piece(nums))
#
#
#
# nums = [int(num) for num in input().split(' ')]
#
#
# def select_piece(pieces_list):
#     curr_biggest = (0, 0, 0)
#
#     for i in range(len(nums)):
#         for k in range(i, len(nums)):
#             piece_boundaries = nums[i:k + 1]
#             piece = (sum(piece_boundaries), i, k + 1)
#
#             sum_piece, size_piece, start_idx_piece = piece[0], piece[2] - piece[1], piece[1]
#             sum_curr, size_curr, start_idx_curr = curr_biggest[0], curr_biggest[2] - curr_biggest[1], curr_biggest[1]
#
#             if sum_piece < sum_curr or sum_piece > sum_curr:
#                 curr_biggest = piece if sum_piece > sum_curr else curr_biggest
#             elif size_piece < size_curr or size_piece > size_curr:
#                 curr_biggest = piece if size_piece > size_curr else curr_biggest
#             else:
#                 curr_biggest = piece if start_idx_piece < start_idx_curr else curr_biggest
#
#     return f'{curr_biggest[0]} {curr_biggest[1]} {curr_biggest[2] - 1}'
#
#
# print(select_piece(nums))


# nums = [int(num) for num in input().split(' ')]
#
#
# def select_piece(pieces_list):
#     max_sum = float('-inf')
#     max_length = 0
#     selected_piece = None
#
#     for start in range(len(nums)):
#         current_sum = 0
#         for end in range(start, len(nums)):
#             current_sum += nums[end]
#             current_length = end - start + 1
#
#             if current_sum > max_sum or (current_sum == max_sum and current_length > max_length):
#                 max_sum = current_sum
#                 max_length = current_length
#                 selected_piece = (current_sum, start, end)
#
#     return f'{selected_piece[0]} {selected_piece[1]} {selected_piece[2]}'
#
#
# print((select_piece(nums)))

