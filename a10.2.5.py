def quersumme_dritter_potenzen(n):
    länge = int(len(str(n)))
    summe = 0

    for i in range(0, länge):
        summe += int(str(n)[i])**3
    
    return summe


zahl = 86145333
reps = 0

print(zahl)

while zahl != 153:
    zahl = quersumme_dritter_potenzen(zahl)
    reps += 1
else:
    print(str(zahl) + " (" + str(reps) + " Wiederholungen)")