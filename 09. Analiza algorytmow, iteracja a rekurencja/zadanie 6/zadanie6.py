with open("./dane6.txt", "r") as file:
    numbers = list(map(str, file.readlines()))

podstawy = [0 for _ in range(11)]
n = 100
for number in numbers:
    max = 2
    for i in range(100):
        if (int(number[i]) >= max):
            max = int(number[i]) + 1
    podstawy[max] += 1