

def my_function(nbr):
    cpt = 0

    for i in range(1,nombre+1):
        if(nombre % i == 0):
            cpt = cpt + 1

    if(cpt == 2):
        print(nombre," Est un nombre premier")
    else:
        print(nombre," N'st un nombre premier")    

print("Saisir un nombre")
nombre = int(input())
#Appel de la fuction my_function
my_function(nombre)  