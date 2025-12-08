def minimalna_liczba_nominalow(nominaly, n, k):
    max = k + 1
    LN = [max] * max
    LN[0] = 0
    prev = [-1] * max

    for i in range(1, k + 1):
        for nominal in nominaly: 
            if i >= nominal:
                if LN[i - nominal] + 1 < LN[i]:
                    LN[i] = LN[i - nominal] + 1
                    prev[i] = i - nominal
    if LN[k] == max:
        return -1
    
    counter = [0] * n
    current = k
    while current > 0:
        used_nominal = current - prev[current]
        counter[nominaly.index(used_nominal)] += 1
        current = prev[current]

    for i in range(n):
        if counter[i] != 0:
            print(f"{counter[i]}x{nominaly[i]}")
    
    return LN[k]




with open("nominaly.txt", "r") as file:
    nominaly = list(map(int, file.readline().split()))

k = int(input("Podaj kwote reszty k: "))
n = len(nominaly)

print(minimalna_liczba_nominalow(nominaly, n, k))