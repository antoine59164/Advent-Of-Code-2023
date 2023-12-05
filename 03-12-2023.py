import re

f = open("adventofcode.com_2023_day_3_input.txt", "r")

data = []
ans = 0
for row in f:
    data.append([x for x in row.split()])

for row in data:
    print(row)
