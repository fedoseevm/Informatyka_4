with open('macierz.txt', 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(map(int, line.split())))
print(*matrix, sep="\n")

sum = matrix[0][0]
path = ""
i = 0
j = 0

while i != len(matrix) - 1 or j != len(matrix[0]) - 1:
    if i == len(matrix) - 1:
        j += 1
        path += "R"
    elif j == len(matrix[0]) - 1:
        i += 1
        path += "D"
    elif matrix[i + 1][j] >= matrix[i][j + 1]:
        i += 1
        path += "D"
    else:
        j += 1
        path += "R"
    sum += matrix[i][j]

print("Suma:", sum)
print("Sciezka:", path)
