
prüfungsnote = float(input("Prüfungsnote(1.0-6.0) mit Halbpunkten: "))
augenfarbe = int(input("Augenfarbe (dunkel=1, hell=0): "))
frisur = int(input("Frisur (kurze Haare=1, lange Haare=0): "))
wetter = int(input("Schönes Wetter=1, nicht schönes Wetter=0: "))

endnote = 0

if augenfarbe==1: ### dunkle Augen
    if frisur==1: # kurz
        endnote = min(6, prüfungsnote*1.1)
    elif frisur==0: # lang
        endnote = max(1, prüfungsnote*0.9)
elif augenfarbe==0: ### helle Augen
    if frisur==1: # kurz
        endnote = max(1, prüfungsnote*0.9)
    elif frisur==0: # lang
        endnote = min(6, prüfungsnote*1.1)

if wetter==1:
    endnote = max(1, endnote-1)

endnote = round(endnote*2) / 2

print("Die Abschlussnote ist: " + str(endnote))