möglichkeit = ["(1) Umrechnung von Celsius nach Kelvin",
               "(2) Umrechnung von Celsius nach Fahrenheit",
               "(3) Umrechnung von Kelvin nach Celsius",
               "(4) Umrechnung von Kelvin nach Fahrenheit",
               "(5) Umrechnung von Fahrenheit nach Celsius",
               "(6) Umrechnung von Fahrenheit nach Kelvin"]

for i in range(0, 6):
    print(möglichkeit[i])

wahl = int(input("Bitte wähle eine Möglichkeit aus: "))
wert = int(input("Gebe nun einen Wert ein: "))

ABS_NP_C = -273.15

def Celsius_Kelvin(t):
    return str(t) + "°C sind: " + str(t-ABS_NP_C) + "°K"
def Celsius_Fahrenheit(t):
    return str(t) + "°C sind: " + str(t* 9/5 + 32) + "°F"
def Kelvin_Celius(t):
    return str(t) + "°K sind: " + str(t+ABS_NP_C) + "°C"
def Kelvin_Fahrenheit(t):
    return str(t) + "°K sind: " + str((t+ABS_NP_C)* 9/5 + 32) + "°F"
def Fahrenheit_Celsius(t):
    return str(t) + "°F sind: " + str((t-32)* 5/9) + "°C"
def Fahrenheit_Kelvin(t):
    return str(t) + "°F sind: " + str((t-32)* 5/9 - ABS_NP_C) + "°K"



if wahl == 1:
    print(Celsius_Kelvin(wert))
elif wahl == 2:
    print(Celsius_Fahrenheit(wert))
elif wahl == 3:
    print(Kelvin_Celius(wert))
elif wahl == 4:
    print(Kelvin_Fahrenheit(wert))
elif wahl == 5:
    print(Fahrenheit_Celsius(wert))
elif wahl == 6:
    print(Fahrenheit_Kelvin(wert))