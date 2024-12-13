import time


# Part 1
def filter_map(value: list):
    len_map = len(value)
    if value != sorted(value) and value != sorted(value, reverse=True):
        return None
    for i in range(len_map):
        if i >= (len_map - 1):
            continue
        if abs(value[i] - value[i + 1]) not in range(1, 4):
            return None
    return True


with open('input.txt', 'r') as file:
    st = time.perf_counter()
    reports = len(list(filter(None, map(lambda x: filter_map(list(map(int, x.split()))), file.readlines()))))
    print(reports)
    print(time.perf_counter() - st)
