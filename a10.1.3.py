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

if wahl == 1:
    print(str(wert) + "°C sind: " + str(wert+273.15) + "°K")
elif wahl == 2:
    print(str(wert) + "°C sind: " + str(wert* 9/5 + 32) + "°F")
elif wahl == 3:
    print(str(wert) + "°K sind: " + str(wert-273.15) + "°C")
elif wahl == 4:
    print(str(wert) + "°K sind: " + str((wert-273.15)* 9/5 + 32) + "°F")
elif wahl == 5:
    print(str(wert) + "°F sind: " + str((wert-32)* 5/9) + "°C")
elif wahl == 6:
    print(str(wert) + "°F sind: " + str((wert-32)* 5/9 + 273.15) + "°K")
else:
    print("Kein gültiger Eingabewert")