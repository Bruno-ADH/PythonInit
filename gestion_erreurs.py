#coding:utf-8
"""Types d'exceptions: ValueError
                        NameError
                        TypeError
                        ZeroDivisionError
                        OSError
                        AssertionError
"""
age = input("Ton âge: ")

try:
    age = int(age)
    print("Tu as",age,"ans")
    assert age >= 18
except AssertionError:
    print("Tu es majeur")
except:
    print("Un nombre")
else:
    print("Super")


