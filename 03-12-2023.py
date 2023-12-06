def getNeighboors(array, row_number, colmun_numver):
    print()


f = open("adventofcode.com_2023_day_3_input.txt", "r")

ans = 0
specialChar = ['*', '#', '+', '$']
data = []

for row in f:
    for x in row.split():
        data.append(list(x))

print("Affichage de la matrice : \n")
for row in data:
    print(row)
print("\n")

for i in range(0, len(data), 1):
    print(data[i])
    for j in range(0, len(data[i]), 1):
        if data[i][j] in specialChar:
            getNeighboors(data, i, j)

    if i == 2:
        exit()

