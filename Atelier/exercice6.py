# compter les chiffres d'un nombre
def compte(n):
    nb=0
    while(n!=0):
        n=n//10
        nb+=1 # le nombre de quotient est différent de 0
    return nb
n=int(input("entrez un nombre:"))
print("le nombre des chiffres de",n,"est",compte(n))
