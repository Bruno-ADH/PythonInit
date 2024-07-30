#coding:utf-8
import os
os.system("cls")

class HUMAIN:
    ville= "Cotonou"

    def __init__(self, c_nom, c_prenom):
       self.nom = c_nom
       self.prenom= c_prenom
    def parler(self, message):
        print("{} a dit {}".format(self.prenom, message))
    def changer_ville(cls, nouvelle_ville):
        HUMAIN.ville= nouvelle_ville
    change_city = classmethod(changer_ville) 
    
    def lecon():
        print("Love U is A losing game")

    definition = staticmethod(lecon)



print("Classe en création...")
print("Ta ville est {}".format(HUMAIN.ville))
HUMAIN.change_city("Calavi")
print("Ta ville actuelle est {}".format(HUMAIN.ville))
HUMAIN.definition()