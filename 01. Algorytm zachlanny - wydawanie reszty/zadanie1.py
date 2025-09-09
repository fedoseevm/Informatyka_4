with open('nominaly.txt', 'r') as file:
    nominaly = list(map(int, file.readline().split()))

kwota = int(input("Podaj resztę do wydania: "))

count = [0] * len(nominaly)
for i in range(len(nominaly)):
    count[i] = kwota // nominaly[i]
    kwota %= nominaly[i]
    print(f"{count[i]}x{nominaly[i]}")
    