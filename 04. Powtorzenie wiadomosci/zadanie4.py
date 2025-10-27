with open('macierz.txt', 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(map(int, line.split())))

n = len(matrix)
maxColSum = 0
maxSumIndex = 0

for i in range(n):
    tempSum = 0
    for j in range(n):
        tempSum +=matrix[j][i]
    if tempSum > maxColSum:
        maxColSum = tempSum
        maxSumIndex = i

print(maxColSum, maxSumIndex, sep=" ")