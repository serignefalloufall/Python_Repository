print("Saisir un nombre")
nombre = int(input())
som = 0
for i in range(1, nombre + 1):      # de 1 à nombre +1 exclu --> de 1 à nombre inclus
    som += i 
moy = som / nombre
print(moy)