# Part One
with open("input.txt", "r") as file:
    words = file.read().split()
    len_rows = len(words)
    len_columns = len(words[0])
    print(len_rows, len_columns)
    ans = 0
    valid = ["XMAS", "SAMX"]
    for row in range(len_rows):
        for column in range(len_columns):
            if row + 3 < len_rows and words[row][column] + words[row + 1][column] + words[row + 2][column] + \
                    words[row + 3][column] in valid:
                ans += 1
            if column + 3 < len_columns and words[row][column] + words[row][column + 1] + words[row][column + 2] + \
                    words[row][column + 3] in valid:
                ans += 1
            if row + 3 < len_rows and column + 3 < len_columns and words[row][column] + words[row + 1][column + 1] + \
                    words[row + 2][column + 2] + words[row + 3][column + 3] in valid:
                ans += 1
            if row - 3 >= 0 and column + 3 < len_columns and words[row][column] + words[row - 1][column + 1] + \
                    words[row - 2][column + 2] + words[row - 3][column + 3] in valid:
                ans += 1
    print(ans)
