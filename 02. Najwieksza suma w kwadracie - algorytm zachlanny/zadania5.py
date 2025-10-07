from random import randint


n = int(input("Podaj liczbe calkowita n: "))
M = [[randint(1,9) for j in range(n)] for i in range(n)]
for linia in M:
    print(linia, end="\n")
    
n = len(M)
i = 0
j = 0    
suma = M[i][j]

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