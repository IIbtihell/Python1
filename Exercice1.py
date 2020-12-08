while (n>5) :
         n=int(input("Saisir le nombre des lignes:"))
while (m>5) :
         m=int(input("Saisir le nombre des colonnes:"))
t1=[[0for i in range (n)]for j in range(m)] 
t2=[[0for i in range (n)]for j in range(m)]
t3=[[0for i in range (n)]for j in range(m)]
for i in range (n):
for j in range (m):
while (t1[i][j]>0) :
        t1[i][j]=int(input("Saisir le nombre des éléments T1  :" ))
for i in range (n):
        for j in range (m):
while (t2[i][j]>0) :
            t2[i][j]=int(input("saisir la nomber des éléments  T2: "))
for i in range (n):
                for j in range (m):
t3[i][j]=t1[i][j]+t2[i][j]

print(t1)
print(t2)
print(t3)
