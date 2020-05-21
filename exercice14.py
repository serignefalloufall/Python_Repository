def estBissextile(annee):

    if(annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0):
        return True
    else:
        return False


#Appel de la fonction

print("Saisir jour : ")
jour = int(input())

print("Saisir mois : ")
mois = int(input())

print("Saisir annee : ")
annee = int(input())

if(estBissextile(annee)):
    print("L'annee est bissextile")
else:
    print("L'annee est non bissextile")
