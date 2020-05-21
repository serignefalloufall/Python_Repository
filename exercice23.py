
nbr_lapin = 2
nbr_mois = 0

for i in range(1,72):
    nbr_lapin = nbr_lapin + 2
 
print("le nombre de lapin est :",nbr_lapin)
print("----------*****----------")

#Au bout de combien de mois dépasse-t’on le milliard de lapins ?

while(nbr_lapin != 1000):
    nbr_lapin = nbr_lapin + 2
    nbr_mois = nbr_mois + 1

print("Au bout de ",nbr_mois," mois, on va depasser",nbr_lapin,"lapin")

