import os

for i in range(1, 26):
    os.mkdir(f'day {i}')
    input_file = open(f'day {i}/input.txt', 'w')
    input_file.close()
    day_file = open(f'day {i}/day.py', 'w')
    day_file.close()