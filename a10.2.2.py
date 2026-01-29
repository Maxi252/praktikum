import math

a = int(input("a*x² -> a:"))
b = int(input("b*x -> b:"))
c = int(input("c:"))

print(str(a)+"x² + " + str(b)+"x + " + str(c)) # Gleichung


if (a>0 and c>0) or (a<0 and c<0):
    print("Es gibt keine Nullstellen.")
else:
    b = b/a
    c = c/a
    a = a/a  # a muss zuletzt sein

    print(str(a) + " " + str(b) + " " + str(c))

    x1 = -b/2 + math.sqrt((b/2)**2 - c)
    x2 = -b/2 - math.sqrt((b/2)**2 - c)

    if x1 == x2:
        print("Die Gleichung hat eine Nullstelle bei x = " + str(x1))
    else:
        print("Die Gleichung hat zwei Nullstellen an den Stellen x = " + str(x1) + " und x = " + str(x2))
