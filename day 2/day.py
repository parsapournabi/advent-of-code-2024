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


# Part 2
def safe(report):
    return all(abs(report[i] - report[i + 1]) in range(1, 4) for i in range(len(report) - 1)) and (
                all(report[i] > report[i + 1] for i in range(len(report) - 1)) or all(
            report[i] < report[i + 1] for i in range(len(report) - 1)))


with open('input.txt', 'r') as file:
    st = time.perf_counter()
    reports = list(map(lambda x: list(map(int, x.split())), file.readlines()))
    ans = 0
    for r in reports:
        if any(safe(r[:i] + r[i + 1:]) for i in range(len(r))):
            ans += 1
    print(ans)
    print(time.perf_counter() - st)
