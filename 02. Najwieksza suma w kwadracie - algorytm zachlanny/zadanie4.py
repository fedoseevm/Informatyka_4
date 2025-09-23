M = []

with open('macierz.txt', 'r') as file:
    for wiersz in file:
        wiersz = list(map(int, wiersz.split()))
        M.append(wiersz)
    
n = len(M)
i = 0
j = 0    
suma = M[i][j]
indeksy = []

while i < n - 1 or j < n - 1:
    if i == n - 1:
        j += 1
    elif j == n - 1:
        i += 1
    elif M[i + 1][j] > M[i][j + 1]:
        i += 1
    else:
        j += 1
    suma += M[i][j]
    
print(suma)
    