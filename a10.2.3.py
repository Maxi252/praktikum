
a = int(input("Bitte eine Zahl eingeben:"))
b = int(input("Bitte eine größere Zahl eingeben:"))

for i in range(a, b+1):
    reps = 0
    actual = i

    while actual != 0:
        reps += 1

        if actual%3 == 0:
            actual += 4
        elif actual%3 != 0 and actual%4 == 0:
            actual = actual/2
        elif actual%3 != 0 and actual%4 != 0:
            actual -= 1
    
    print(str(i) + " -> " + str(reps))