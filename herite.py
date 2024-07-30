#coding:utf-8
import os
os.system("cls")

class vehicule:

    def __init__(self, nom, reservoire):
        self.nom = nom
        self.reservoire = reservoire

    def marque_vehicule(self):
        return self.nom

    def deplacer(self):
        print("Le vehicule {} se deplace très bien...".format(self.nom))

class voiture(vehicule):
    def __init__(self, nom, reservoire, puissance):
        vehicule.__init__(self, nom, reservoire)
        self.puissance = puissance
    
    def deplacer(self):
        print("La voiture {} se roule très bien...".format(self.nom))

class avion(vehicule):
    def __init__(self, nom, reservoire, mrchdises):
        vehicule.__init__(self, nom, reservoire)
        self.marchandises = mrchdises
    
    def deplacer(self):
        print("L'avion {} survole très bien les airs...".format(self.nom))

c1 = voiture("Mercedes 23 C7", 2400, 24)
print(c1.nom)
c1.deplacer()

a1 = avion("CORSAIR", 3199, 231)
print(a1.nom)
a1.deplacer()
