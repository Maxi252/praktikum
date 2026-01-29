liste = []



while True:
    zahl = input("Eine ganze Zahl eingeben: ")

    if(str(zahl) == "x"):
        print(liste)
        print(len(liste))
        break
    elif isinstance(int(zahl), int):
        liste.append(int(zahl))
        liste.sort()

