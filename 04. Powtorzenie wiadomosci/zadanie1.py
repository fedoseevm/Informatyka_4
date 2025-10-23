with open('dane.txt', 'r') as file:
    nominaly = list(map(int, file.readline().split()))
    kwoty = list(map(int, file.readlines()))
print(nominaly)
print(kwoty)

minimum = float('inf')
result = []

for kwota in kwoty:
    iloscNominalow = 0
    tmp_kwota = kwota
    for i in range(len(nominaly)):
        iloscNominalow += tmp_kwota // nominaly[i]
        tmp_kwota %= nominaly[i]
    
    if iloscNominalow < minimum:
        minimum = iloscNominalow
        result = [kwota]
    elif iloscNominalow == minimum:
        result.append(kwota)
        
print(*result, sep=" ")