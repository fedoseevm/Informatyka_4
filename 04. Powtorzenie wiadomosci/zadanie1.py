with open('dane.txt', 'r') as file:
    nominaly = list(map(int, file.readline().split()))
    kwoty = list(map(int, file.readlines()))
print(nominaly)
print(kwoty)

minimum = 100
result = []

for kwota in kwoty:
    iloscNominalow = 0
    for i in range(len(nominaly)):
        iloscNominalow += kwota // nominaly[i]
        kwota %= nominaly[i]
    
    if iloscNominalow < minimum:
        minimum = iloscNominalow
    elif iloscNominalow == minimum:
        result.append(kwota)
        
print(result)