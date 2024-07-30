#coding:utf-8
import os
os.system("cls")

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(self.nom, "mange bien...")

class Reptile(Animal):
    def __init__(self, nom, regime_alimentaire):
        Animal.__init__(self, nom)
        self.regime = regime_alimentaire
    
    def manger(self):
        print("Le reptile mange sussus...")

#Code principal
checo = Reptile("checo", "mouche")
print(issubclass(Reptile, Animal))
