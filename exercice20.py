#declaration liste my_liste
my_liste = []
plus_grand = 0

for i in range(1,11):
    print("saisir un entier")
   # val = int(input())
    my_liste.append(int(input()))
#Remplissage Liste

plus_grand = my_liste[0]
#je recuper le premier element de la liste
#Parcour Liste
for elem in my_liste:
    if(elem > plus_grand):
        plus_grand = elem 

#Affichage de la liste
print(my_liste)
#Affichage de l'element le plus grand
print("Le plus grand est : ",plus_grand)
