with open('macierz.txt', 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(map(int, line.split())))
print(*matrix, sep="\n")

n = len(matrix)

for i in range(n):
    matrix[i][2], matrix[i][4] = matrix[i][4], matrix[i][2]

for row in matrix:
    for item in row:
        if item < 10:
            print(" ", end="")
        print(item, end=" ")
    print()