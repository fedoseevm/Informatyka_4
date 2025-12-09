def longestString(X, Y):
    n = len(X)
    m = len(Y)

    k = 0
    D = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1])

    i = n
    j = m
    k = D[n][m]
    wynik = ""

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            wynik = X[i - 1] + wynik
            k -= 1
            i -= 1
            j -= 1
        elif D[i - 1][j] >= D[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return wynik


X = input()
Y = input()
print(longestString(X, Y))