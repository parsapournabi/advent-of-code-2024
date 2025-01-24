import re

# Part One
with open("input.txt", 'r') as file:
    txt = file.read()
    ans = 0
    methods = re.findall("mul\(\d+,\d+\)", txt)

    for method in methods:
        a, b = map(int, (method.strip("mul()").split(",")))
        ans += a * b
    print(ans)