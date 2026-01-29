
def verschlüsselung(text):
    #text = input("Folgenden Text codieren: ")
    schlüssel = int(input("Verschiebung der Buchstaben: "))

    bigLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerLetter = "abcdefghijklmnopqrstuvwxyz"
    sonderzeichen = " .!?-+/*,;:%&()="

    codedText = ""
    for i in range(0, len(text)):
        if text[i].isupper():
            pos = bigLetter.index(text[i])
            if pos + schlüssel <= len(bigLetter)-1:
                codedText += bigLetter[pos+schlüssel]
            else:
                codedText += bigLetter[pos+schlüssel-26]
        elif text[i].islower():
            pos = lowerLetter.index(text[i])
            if pos + schlüssel <= len(lowerLetter)-1:
                codedText += lowerLetter[pos+schlüssel]
            else:
                codedText += lowerLetter[pos+schlüssel-26]
        elif text[i] in sonderzeichen:
            pos = sonderzeichen.index(text[i])
            codedText += sonderzeichen[pos]

    print(codedText)

    with open("test.txt", "a", encoding="utf-8") as file:
        file.write("\n\n" + codedText)


with open("test.txt", "r", encoding="utf-8") as file:
    inhalt = str(file.read())

    verschlüsselung(inhalt)
