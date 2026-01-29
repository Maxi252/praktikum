from tkinter import *
import random

doorCar = random.randint(0, 2)


def showA():
    showZiege(0)
def showB():
    showZiege(1)
def showC():
    showZiege(2)

def showZiege(door):
    round = 0
    round += 1
    if door == doorCar and round==1:
        print("Auto")

        liste = [0, 1, 2]
        liste.remove(doorCar)

        randomZiege = random.choice(liste)

        türliste = [doorA, doorB, doorC]
        türliste[randomZiege].configure(background="red")
    elif round==1:
        print("Ziege")

        liste = [0, 1, 2]
        liste.remove(doorCar)
        liste.remove(door)

        türliste = [doorA, doorB, doorC]
        türliste[liste[0]].configure(background="red")
    elif round==2:
        if door == doorCar:
            türliste = [doorA, doorB, doorC]
            türliste[doorCar].configure(background="green")
        




window = Tk()
window.geometry("500x300")
window.title("Monty Hall Problem")

doorA = Button(window, text="Tür A", width=40, height=2, command=showA)
doorA.pack(pady=20)

doorB = Button(window, text="Tür B", width=40, height=2, command=showB)
doorB.pack(pady=20)

doorC = Button(window, text="Tür C", width=40, height=2, command=showC)
doorC.pack(pady=20)


window.mainloop()