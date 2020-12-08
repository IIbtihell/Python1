n=int(input("Saisir le nombre des lignes:"))
m=int(input("Saisir le nombre des colonnes:"))
t1=[[0for i in range (n)]for j in range(m)]

for i in range (n):
    for j in range (m):
t1[i][j]=int(input("Saisir le nombre des élément T1  :" ))

S=0
for i in range(n):
    for j in range (m):
S =S+t1[i][j]
print(S)
