
for i in range(100, 1000):
    first = int(str(i)[0])
    second = int(str(i)[1])
    third = int(str(i)[2])

    if first**3 + second**3 + third**3 == i:
        print(i)