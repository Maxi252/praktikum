
vorname = input("Vorname: ")
nachname = input("Nachname: ")
einkommen = float(input("Einkommen: "))
vermögen = float(input("Vermögen: "))

steuersatz = 0


if einkommen <= 10000:
    steuersatz += einkommen*40/100
elif 10000 < einkommen and einkommen <= 30000:
    steuersatz += einkommen*55/100
elif 30000 < einkommen and einkommen <= 70000:
    steuersatz += einkommen*75/100
else:
    steuersatz += einkommen*82/100


if vermögen <= 100000:
    steuersatz += vermögen*5/100
elif 100000 < vermögen and vermögen <= 500000:
    steuersatz += vermögen*8/100
elif 500000 < vermögen and vermögen <= 1000000:
    steuersatz += vermögen*13/100
else:
    steuersatz += vermögen*21/100


print("Der Steuerzahler " + vorname + " " + nachname + " muss für das laufende Jahr " + str(steuersatz) + " Dublonen dem Steueramt bezahlen.")
