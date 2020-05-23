my_liste = []

print("Saisir le nombre d'element de la liste")
n = int(input())

for i in range(1,n+1):
    print("Saisir un entier : ")
    my_liste.append(int(input())) # Remplissage de la liste


print(my_liste) # Affichage de la liste
resultat = False
elementPrecedent = my_liste[0] # Recuperation de la premier element de la liste
for element in my_liste:
    if(elementPrecedent > element):
        resultat=True
        elementPrecedent=element  

    else:
        resultat=False
        elementPrecedent=element  

#print("prece : ",elementPrecedent,"elem : ",element)
if (resultat == True):
    print("Est croissant")
elif (resultat == False):
     print("Est dcroissant")
else: 
    print("Est quelconque")
