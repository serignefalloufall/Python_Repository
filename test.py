"""

def my_function(nbr):
 
  return nbr*2
x = my_function(5)
print("x",x)
----------------------------------------------------
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print(thislist[-1])


---------------------------------------------------------
xs=[5,3,2,5,6,1,0,5]
minimum = xs[0];
for i in xs:
    if i < minimum:
        minimum = i ;
print(minimum)
----------------------------------------------------------

i = 1
while i < 6:
  print(i)
  i += 1
  -------------------------------------------------

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


----------------------------------------------
Compare element liste

def est_croissant(liste):
    for i in range(len(liste)-1):
        if not liste[i] <= liste[i+1]:
            return False
    return True
 
print(est_croissant([1,2,3,4,5]))#True

"""

"""
print("Avant tri")
print(my_liste)
print('\n')

my_liste.sort()

print("Apres tri croissant")
print(my_liste)
print('\n')

my_liste.sort(reverse=True)

print("Apres tri dcroissant")
print(my_liste)
print('\n')

print("Sorted")
sorted(my_liste)
print(my_liste)


if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else


annee = int(input("Entrez l annee a verifier:"))
if(annee%4==0 and annee%100!=0 or annee%400==0):
    print("L'annee est une annee bissextile!")
else:
    print("L'annee n'est pas une annee bissextile!")




t = [0, 1, 2, 3, 4]
N = 5
moy = 0
for i in range(1, N + 1):      # de 1 à N+1 exclu --> de 1 à N inclus
    moy += t[i - 1]           # le premier indice est 0 et non 1
moy /= N
print(moy)
"""