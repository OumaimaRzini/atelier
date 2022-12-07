#programme
list=[1,2,1,3,4]
def moy_list(list):
    s=0
    for i in range (len(list)):
        s+=list[i]
    return s/len(list)
print("la moyenne est:",moy_list(list))

def min_max(list):
    choice = input("pick max or min:")
    if(choice == "max"):
        max=list[0]
        for i in list:
            if i>=max: max=i
        return max
    elif(choice == "min"):
        # min
        min = list[0]
        for i in list:
            if i<= min: min=i
        return min
    else:
        return "wrong choice"
        
print(min_max(list))

def mediane(list):
    l=sorted(list)
    index=len(l)//2
    # si l'ensemble des éléments de list est impair
    if len(list)%2 !=0:
        return l[index]
    #si l'ensemble des éléments de list est pair
    return (l[index-1]+ l[index])/2 
print("le médiane est:", mediane(list))

def mode(list):
    if list==[]:
        return None
    else:
        return max(set(list),key=list.count)
print("le mode est ",mode(list))


