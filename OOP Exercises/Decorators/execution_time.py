from time import time


def exec_time(function):

    def wrapper(*args):
        start = time()
        function(*args)
        end = time()
        execution = end - start

        return f"{execution:.2f}"

    return wrapper

#test case
@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1


print(loop())
