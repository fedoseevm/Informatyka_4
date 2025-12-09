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
    k = D[i][j]
    return k
    

with open("pary.txt", "r") as file:
    slowa = []
    for line in file:
        para = list(line.split())
        slowa.append(para)

print(*slowa, sep="\n")

maxlen = 0
for para in slowa:
    if maxlen < longestString(para[0], para[1]):
        maxlen = longestString(para[0], para[1])

for para in slowa:
    if maxlen == longestString(para[0], para[1]):
        print(*para)
