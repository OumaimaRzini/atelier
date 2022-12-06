#convert decimal to binaire
def covert(n):
    binaire=""
    while(n !=0):
        binaire+= str(n % 2) #renvoyer le nombre binaire dans une chaîne de caractére
        n=n//2
    return binaire[::-1] #inverser le nombre binaire

n=int(input("entrez un nombre:"))
print("le nombre",n ,"en binaire est:",covert(n))