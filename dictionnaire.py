#coding:UTF-8

"""
"""

import os
os.system("cls")

dico = {"chat":"C'est un félin"}
dico2 = {"chimpanze":"C'est un singe"}
dico["chien"] = "Un bon chien"

print(dico2)

for k,v in dico.items():
    print(k,":",v)


def maFonctionBizarre(**parametres):
    print(parametres)

maFonctionBizarre(prenom= "Bruno", a="ADEN HOUESSOU")