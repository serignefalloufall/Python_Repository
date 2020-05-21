print("Saisir la valeur de a")
a = int(input())

print("Saisir la valeur de b")
b = int(input())
pgcd = 0


#print ("la valeur de a et b est :",a,b)
while(a!=b):
    if(a>b):
        a = a-b         
    else:
         b = b-a
       
pgcd = a
print ("le pgcd de a et b est :",pgcd)