# coding:utf-8
import copy
import includes.second_fonction as second_fonction 

# commentaire
""" comm
ffkff
ffffff
ffff
"""
jeu = True

# while jeu:
#     choix = input("> ")

#     if choix == "encore":
#         continue
#     elif choix == "quitter":
#         jeu = False
#     else: 
#         print("introuvable")

# print("A plus")

x = [1, 2, 5, 12]
y= [ 3, 5, 2]
x.extend(y)
print(x)

second_fonction.mon_liste("Bruno")
second_fonction.personne("Bruno","Ilove U")