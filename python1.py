N=int(input("Saisir le nombre d'éléments : "))
tab=[0]*N ;
for i in range(N):
    tab[i]=int(input("Saisir l'élément{0}: ".format(i+1)))

S=0
for i in range(N):
    S=S+tab[i]
print("La somme est=",S)

P=1
for i in range(N):
    P=P*tab[i]
print("Le produit est=",P)

M=S/P
print("La moyenne est=", M)

if tab[i]<0:
    print("La valeur est négative")

else:
    print("La valeur est positive")


max=tab[0]
for i in range(N):
    if tab[i]>max
    max=tab[i]
print(max)

min=tab[0]
for i in range(N):
    if tab[i]<max
    min=tab[i]
print(max)





    
