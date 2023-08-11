def list_manipulator(*args):
    input_list = args[0]
    nums = list(args[3:])

    if args[1] == "add" and args[2] == "end":
        input_list.extend(nums)
        return input_list

    elif args[1] == "add" and args[2] == "beginning":
        nums.extend(input_list)
        return nums

    elif args[1] == "remove" and args[2] == "beginning":
        return input_list[nums[0]:] if nums else input_list[1:]

    elif args[1] == "remove" and args[2] == "end":
        return input_list[:-nums[0]] if nums else input_list[:-1]
