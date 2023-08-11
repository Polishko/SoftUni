def read_next(*args):
    for ele in args:
        for sub_ele in ele:
            yield sub_ele
