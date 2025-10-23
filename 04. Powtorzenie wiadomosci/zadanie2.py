with open('macierz.txt', 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(map(int, line.split())))
print(*matrix, sep="\n")


sum = matrix[0][0]
path = ""
i = 0
j = 0

