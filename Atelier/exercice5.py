#la somme des nombres de 1 a n
def somme(n):
    s=0
    for i in range(1,n+1):
        s+=i
        i+=1
    return s
n=int(input("enter a number:"))
print("la somme des nombres est" ,somme(n))