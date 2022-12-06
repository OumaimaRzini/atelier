# définition d'une fonction puissance
def puissance(x,n):
    if n==0:
        return 1
    else:
        p=1
        if n>0:
            for i in range(n):
                p*=x
        else: #si la puissance est négative
            for i in range(abs(n)):#la valeur absolue de n
                p*= (1/x)
        return p
x=int(input("entrez le nombre qui vous souhaitez trouver sa puissance:"))
n=int(input("entrez la puissance"))
print("la valeur de",x , "a la puissance",n,"est",puissance(x,n))