def fill_the_box(*args):
    height, length, width, *sub_args = args
    space_for_boxes = height * length * width
    stop_idx = sub_args.index("Finish")

    for i in range(stop_idx):
        sub_arg = sub_args[i]

        if sub_arg > space_for_boxes:
            return f"No more free space!" \
                   f" You have {sub_arg - space_for_boxes + sum(sub_args[i + 1:stop_idx])} more cubes."
        else:
            space_for_boxes -= sub_arg

    return f"There is free space in the box. You could put {space_for_boxes} more cubes."
