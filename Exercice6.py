n=int(input("Saisir la nomber des lignes:"))
m=int(input("Saisir la nomber des colonne:"))
t1=[[for i in range (n)]for j in range(m)]

for i in range (n):
    for j in range (m):
t1[i][j]=int(input("Saisir le nombre des élément  T1  :" ))

max=0
for i in range(n):
    for j in range (m):
if (t1[i][j]>max):
           max =t1[i][j]

min=0
for i in range(n):
    for j in range (m):
if (t1[i][j]<min):
min =t1[i][j]

print(t1)
print(max)
rint(min)
n=int(input("Saisir le nombre des lignes:"))
m=int(input("Saisir le nombre des colonnes:"))
t1=[[for i in range (n)]for j in range(m)]

for i in range (n):
    for j in range (m):
t1[i][j]=int(input("Saisir le nombre des éléments T1  :" ))

S=0
for i in range(n):
    for j in range (m):
S =S+t1[i]
print(S)
n=int(input("Saisir le nombre des lignes:"))
m=int(input("Saisir le nombre des colonnes:"))
t1=[[for i in range (n)]for j in range(m)]

for i in range (n):
    for j in range (m):
t1[i][j]=int(input("Saisir le nombre des éléments T1  :" ))

S=0
for i in range(n):
    for j in range (m):
           S =S+t1[j]
Print(S)
n=int(input("Saisir le nombre des lignes:"))
m=int(input("Saisir le nombre des colonnes:"))
t1=[[0for i in range (n)]for j in range(m)]

for i in range (n):
    for j in range (m):
t1[i][j]=int(input("Saisir le nombre des éléments T1  :" ))
X=int(input("Saisir le nombre des recherches:"))

e=0
for i in range(n):
    for j in range (m):
if T[i] [j] = X
   e=e+1
print(e)
def multX() :
X=int(input("Saisir le nombre multiplié:"))
for i in range(n):
    for j in range(m):
for k in range(p):
            C[i][j] += A[i][k] * X
def som() :
for i in range(n):
    for j in range(m):
for k in range(p):
C[i][j] += A[i][k] + B[k][j]
def mult() :
for i in range(n):
    for j in range(m):
for k in range(p):
C[i][j] += A[i][k] * B[k][j]
