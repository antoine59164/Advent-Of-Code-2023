import re
# only 12 red cubes, 13 green cubes, and 14 blue cubes
ans = 0

f = open("adventofcode.com_2023_day_2_input.txt", "r")

for l in f:

    gameId = int(re.search(r'\d+', l.split(":")[0]).group())

    splitL = l.split(":")
    splitL.pop(0)

    red, blue, green = 0, 0, 0
    for set in splitL[0].split(";"):
        countOfSet = len(splitL[0].split(";"))
        for cubes in set.split(","):
            if cubes.split()[1] == "red":
                red += int(cubes.split()[0])
            if cubes.split()[1] == "blue":
                blue += int(cubes.split()[0])
            if cubes.split()[1] == "green":
                green += int(cubes.split()[0])
    print(green)
    exit()



    exit()