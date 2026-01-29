from tkinter import *

fenster = Tk()
fenster.geometry("500x300")
fenster.title("Temperatur Umwandler")

variable = StringVar(fenster)
variable.set("Celius") # default value


w = OptionMenu(fenster, variable, "Celsius", "Fahrenheit", "Kelvin")
w.pack()

eingabe = Text(fenster, height=1, width=50)
eingabe.pack()


fenster.mainloop()