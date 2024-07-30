#coding:utf-8
import os
import pickle
os.system("cls")

class player:
    def __init__(self, name, level):
        self.name= name
        self.level = level
    
    def whoami(self):
        print("Nom: {}, Niveau: {}".format(self.name, self.level))

player1 = player("Tyoma", 7)
player2 = player("Douglou", 4)

with open("fichier/fichier.txt", "wb") as fic:
    record = pickle.Pickler(fic)
    record.dump(player1)

with open("fichier/fichier.txt", "ab") as fic:
    record = pickle.Pickler(fic)
    record.dump(player2)

with open("fichier/fichier.txt", "rb") as fic:
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load()

print(type(player_one))

player_one.whoami()
