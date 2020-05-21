print("-------------------- ********** --------------------")

print("User1 veillez saisir un nombre que user2 doit essaier de le trouver :")
nbr_user1 = int(input())

print("User2 devine le nombre que user1 a saisie:")
nbr_user2 = int(input())

score = 100
while(nbr_user1 != nbr_user2):
    if(nbr_user1 > nbr_user2):
        print("-----ohhhh plus grand-----")
        score = score - 1
     
    else:
        print("-----ohhhhh plus petit-----")
        score = score - 1
     
    print("Saisir un autre nombre:")
    nbr_user2 = int(input()) 
  
print("Bravoooo votre score est : ",score)