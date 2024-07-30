#coding:UTF-8
import copy
import os
os.system("cls")
"""
    liste.sort() pour trier
    liste.clear() effacer la liste ou liste[:]=[] 
    liste.count(valeur) compter le nombre d'occurence
    "caractère".join(liste) pour rejoindre la liste en chaine
    liste1.extend(liste2)
    liste1 += liste2
"""
inventaire = ["ard", "b", "ee", "uuu", "i", "16"]
inv2 = copy.deepcopy(inventaire)
print(inventaire[:])

phrase = " ".join(inventaire)
print(phrase)