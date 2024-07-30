# coding:utf-8

def personne(nom, message):
    print("{}, {}".format(nom, message))

# user_name = input("Entrer le nom: ")
# user_send = input("Entrer le message: ")

# personne(user_name, user_send)

# def mon_liste(*items):
#     for item in items:
#         print(item)

# mon_liste("thomas")
# mon_liste(1,'b',"poule")

mon_liste = lambda items: print("bonjour {}".format(items))

if __name__ == "__main__":
    print("Test")
    personne("Bruno", "super")
    personne("Bruno", "super")
    mon_liste("Bob")


