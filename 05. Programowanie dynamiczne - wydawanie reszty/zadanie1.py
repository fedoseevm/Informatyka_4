def minimalna_liczba_nominalow(nominaly, n, k): 
    max = k + 1
    LN = [0] * (k + 1)
    for i in range(k + 1):
        LN[i] = max
    
    LN[0] = 0
    for i in range(1, k + 1):
        for nominal in nominaly:
            if i >= nominal:
                if LN[i - nominal] + 1 < LN[i]:
                    LN[i] = LN[i - nominal] + 1
    if LN[k] != max:
        return LN[k]
    else:
        return -1
                    

with open("nominaly.txt", "r") as file:
    nominaly = list(map(int, file.readline().split()))

k = int(input("Podaj kwote reszty k: "))
n = len(nominaly)

print(minimalna_liczba_nominalow(nominaly, n, k))
