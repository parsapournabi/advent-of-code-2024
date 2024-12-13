import time

# Part 1
list_left = []
list_right = []
result = 0
with open('input.txt', 'r') as file:
    st = time.perf_counter()
    tuple(map(lambda x: (list_left.append(int(x.split()[0])), list_right.append(int(x.split()[1]))), file.readlines()))
    list_left.sort()
    list_right.sort()
    for left, right in zip(list_left, list_right):
        result += abs(left - right)
    print('Answer is:', result)
    print(time.perf_counter() - st)

# Part 2
list_left = []
list_right = []
with open('input.txt', 'r') as file:
    st = time.perf_counter()
    tuple(map(lambda x: (list_left.append(int(x.split()[0])), list_right.append(int(x.split()[1]))), file.readlines()))
    result = sum([num * list_right.count(num) for num in list_left])
    print('Answer is:', result)
    print(time.perf_counter() - st)