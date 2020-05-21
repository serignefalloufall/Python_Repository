print("Saisir la valeur de a")
a = int(input())

print("Saisir la valeur de b")
b = int(input())
q=0

#print ("la valeur de a et b est :",a,b)
while(a>=b):
    a = a-b
    q = q+1
print ("le quotient entier  est :",q)