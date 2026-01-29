import time

def main():
    grenze = int(input("Geben Sie eine Obergrenze an: "))
    sieb(grenze)

def sieb(n):
    start = time.perf_counter()
    anzahlPrim = 0
    for i in range(2, n+1):
        teiler = 0
        for x in range(1, i+1):
            if i%x == 0:
                teiler += 1
        if teiler <= 2:
            anzahlPrim += 1
            print(i)
    ende = time.perf_counter()
    print("Es gibt " + str(anzahlPrim) + " Primzahlen bis zur " + str(n) + " (" + str(ende-start) + " Sekunden)")

main()
