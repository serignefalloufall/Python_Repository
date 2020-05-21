prix = 200
som = 0
#print ("la valeur de a et b est :",a,b)
while(prix != 0):
    print("Saisir le prix d'un article et si vouz voulez arreter la saisie taper 0")
    prix = int(input())
    som = som + prix

print ("la sommme des prixs saisie est :",som)