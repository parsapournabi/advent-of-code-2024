from collections import defaultdict
from math import ceil

# Part One
with open("input.txt", "r") as file:
    data = file.read().split()
    pairs = defaultdict(list)
    for d in data:
        if "|" in d:
            k, v = d.split("|")
            pairs[k].append(v)
    pages = [d.split(",") for d in data if "," in d]

    ans = 0
    for i in range(len(pages)):
        len_page = len(pages[i])
        al = 0
        for j in range(len_page):
            if all(pages[i][k] in pairs[pages[i][j]] for k in range(j + 1, len_page)):
                al += 1
        if al >= len_page:
            ans += int(pages[i][ceil(len(pages[i]) // 2)])

    print(ans)
# Part Two
with open("input.txt", "r") as file:
    data = file.read().split()
    pairs = defaultdict(set)
    for d in data:
        if "|" in d:
            k, v = d.split("|")
            pairs[k].add(v)
    pages = [d.split(",") for d in data if "," in d]
    ans = 0
    for i in range(len(pages)):
        len_page = len(pages[i])
        al = False
        for j in range(len_page):
            k = j + 1
            while k < len_page:
                if pages[i][k] not in pairs[pages[i][j]]:
                    pages[i][k], pages[i][j] = pages[i][j], pages[i][k]
                    al = True
                k += 1
        if al:
            ans += int(pages[i][ceil(len(pages[i]) // 2)])

    print(ans)