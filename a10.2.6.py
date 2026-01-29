
def main():
    grenze = int(input("Geben Sie eine Obergrenze an: "))
    sieb(grenze)

def sieb(n):
    anzahlPrim = 0
    for i in range(2, n+1):
        teiler = 0
        for x in range(1, i+1):
            if i%x == 0:
                teiler += 1
        if teiler <= 2:
            anzahlPrim += 1
            print(i)
    print("Es gibt " + str(anzahlPrim) + " Primzahlen bis " + str(n))

main()
