import re


def part1() -> int:
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    ans = 0

    f = open("adventofcode.com_2023_day_2_input.txt", "r")

    for l in f:

        gameId = int(re.search(r'\d+', l.split(":")[0]).group())

        splitL = l.split(":")
        splitL.pop(0)
        i = 0
        for set in splitL[0].split(";"):
            red, blue, green = 0, 0, 0
            countOfSet = len(splitL[0].split(";"))
            for cubes in set.split(","):
                if cubes.split()[1] == "red":
                    red += int(cubes.split()[0])
                if cubes.split()[1] == "blue":
                    blue += int(cubes.split()[0])
                if cubes.split()[1] == "green":
                    green += int(cubes.split()[0])
            if red > 12 or green > 13 or blue > 14:
                break
            elif i == countOfSet - 1:
                ans += gameId
            i += 1

    return ans

def part2() -> int :

    ans = 0

    f = open("adventofcode.com_2023_day_2_input.txt", "r")

    for l in f:

        gameId = int(re.search(r'\d+', l.split(":")[0]).group())

        splitL = l.split(":")
        splitL.pop(0)

        maxRed, maxBlue, maxGreen = 0, 0, 0
        for set in splitL[0].split(";"):

            for cubes in set.split(","):

                intCube = int(cubes.split()[0])

                if cubes.split()[1] == "red" and intCube > maxRed:
                    maxRed = intCube
                if cubes.split()[1] == "blue" and intCube > maxBlue:
                    maxBlue = intCube
                if cubes.split()[1] == "green" and intCube > maxGreen:
                    maxGreen = intCube

        ans += maxRed * maxGreen * maxBlue

    return ans

print(part2())
