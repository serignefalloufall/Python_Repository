list_entier = []

for i in range(1,11):
    print("saisir un entier")
    list_entier.append(int(input()))
    while(list_entier[i] <= 1 or list_entier[i] >= 10 ):
         print("saisir un entier")
         list_entier.append(int(input()))

print(list_entier)

