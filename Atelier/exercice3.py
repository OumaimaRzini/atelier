def fact(nb):
    if nb==0:
        return 1
    else:
        return nb*fact(nb-1)
def somme():
    s= 0
    for i in range(1,6):
        s += (fact(i)/i)
    return s

print("la somme est:",somme())