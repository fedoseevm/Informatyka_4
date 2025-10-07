M = []

with open('macierz.txt', 'r') as file:
    for wiersz in file:
        wiersz = list(map(int, wiersz.split()))
        M.append(wiersz)
    
n = len(M)
i = 0
j = 0    
suma = M[i][j]
indeksy = [[0, 0]]

while i < n - 1 or j < n - 1:
    if i == n - 1:
        j += 1
        indeksy.append([i, j])
    elif j == n - 1:
        i += 1
        indeksy.append([i, j])
    elif M[i + 1][j] > M[i][j + 1]:
        i += 1
        indeksy.append([i, j])
    else:
        j += 1
        indeksy.append([i, j])
    suma += M[i][j]
    
print(suma)
for para in indeksy:
    print(para[0], para[1], sep=" ")