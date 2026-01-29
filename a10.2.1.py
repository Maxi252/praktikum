
summe = 0

for i in range(0, 10001):
    if i%7 == 0  and  i%5 != 0:
        summe += i

print("Die Summe ist " + str(summe))
