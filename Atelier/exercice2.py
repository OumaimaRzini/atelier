# définition d'une fonction factorielle
def fact(nb):
    if nb==0:
        return 1
    else:
        return nb*fact(nb-1)
nb=int(input("entrez un nombre:"))
print("la factorielle de",nb,"est:",fact(nb))