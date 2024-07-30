#coding:UTF-8
import os
os.system("cls")
"""
"""
class HUMAIN:
    """Cette classe représente un Humain"""
    def __init__(self, nom, prenom, age):
        print("Création d'un humain...")
        self.nom = nom
        self.prenom = prenom
        self._age = age

    def _getage(self):
        try: 
            return self._age
        except AttributeError:
            print("Valeur Inexistante")

    def _setage(self, newage):
        if newage <= 0:
            self._age = 0
        else:
            self._age = newage

    def _delage(self):
        del self._age

    age = property( _getage, _setage, _delage, "Je suis l'âge d'un humain")
    
#Programme Principale
h1 = HUMAIN("GOLLO", "Jordane", 23)

print(h1.age)
del h1.age

print(h1.age)
help(HUMAIN.age)

# print(h1.age)
# del h1.age

# print(h1.age)