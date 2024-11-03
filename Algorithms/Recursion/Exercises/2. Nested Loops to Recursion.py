

def find_iteration_variables(n, result):
    if len(result) == n:
        print(' '.join(str(x) for x in result))
        return

    for i in range(1, n + 1):
        result.append(i)
        find_iteration_variables(n, result)
        result.pop()


find_iteration_variables(int(input()), [])
