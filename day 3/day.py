import re

# Part One
with open("input.txt", 'r') as file:
    txt = file.read()
    ans = 0
    methods = re.findall(r"mul\(\d+,\d+\)", txt)

    for method in methods:
        a, b = map(int, (method.strip("mul()").split(",")))
        ans += a * b
    print(ans)

# Part Two
with open("input.txt", 'r') as file:
    txt = file.read()
    ans = 0
    methods = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", txt)
    enabled = True
    for method in methods:
        if "do()" in method:
            enabled = True
            continue
        elif "don't()" in method:
            enabled = False
            continue
        if enabled:
            a, b = map(int, method.strip("mul()").split(","))
            ans += a * b
    print(ans)
