matrix = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
]

print(matrix[1][2])

matrix = [
    ['joão', 8, 7, 6],
    ['pedro', 4.5, 9, 10],
    ['marcos', 6, 6, 8]
]

for line in matrix:
    for col in line:
        print(str(col) + '\t', end=' ')
    print('')