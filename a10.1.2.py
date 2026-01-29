import math

bogenmass = float(input("Bitte einen Winkel im Bogenmass eingeben: "))


gradmass = bogenmass * (180/math.pi)
bogenminuten = gradmass * 60
bogensekunden = bogenminuten * 60


for i in [str(bogenmass) + " Bogenmass entspricht: ",
          str(gradmass) + "° (Grad)",
          str(bogenminuten) + "' (Bogenminuten)",
          str(bogensekunden) + "'' (Bogensekunden)"]:
    print(i)
