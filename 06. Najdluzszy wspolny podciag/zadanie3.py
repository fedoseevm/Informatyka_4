def longestString(X, Y):
    n = len(X)
    m = len(Y)
    
    k = 0   # dlugosc podciagu
    D = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1])
    
    i = n
    j = m
    k = D[n][m]     # dlugosc podciagu
    wynik = [0] * (k + 1) # podciag
    
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            wynik[k] = X[i - 1]
            k -= 1
            i -= 1
            j -= 1
        elif D[i - 1][j] >= D[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return wynik[1:]
    
    
    
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
print(longestString(X, Y))

