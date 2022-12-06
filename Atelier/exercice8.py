matrix = [[3, 4, 10, 6],[6, 8, 11, 12],[6, 8, 14, 15]]
# procedure qui affiche l'élément dans la matrice
def element(matrix, value):
    for row in matrix:# parcourir les lignes 
        for element in row:# parcourir les colonnes
            if element == value:
                return print("le nombre",value,"existe dans la matrice") #la matrice contient cet élement
    return print("le nombre",value,"n'existe pas dans la matrice")

value=int(input("Entrez le nombre que vous souhaitez chercher dans la matrice "))   
element(matrix, value)

# procedure qui renvoi sa position
def index(element, matrix):
    for i in range(len(matrix)):# parcourir les lignes 
        for j in range(len(matrix[i])):# parcourir les colonnes
            if matrix[i][j] == element:
                return (i, j)
element=int(input("Entrez l'élement pour afficher sa position dans la matrice ")) 
print("la position de l'element est",index(element,matrix))