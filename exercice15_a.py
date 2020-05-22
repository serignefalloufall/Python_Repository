print("Saisir un nombre")
nombre = int(input())

som = 0

for i in range(1,nombre+1):
    som = som + i
    #print("som = ",som)
print("la somme des chiffre jusqua ce nombre est : ",som)