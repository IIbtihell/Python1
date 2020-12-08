from random import*
n=int(input("n"))
m=int(input("m"))
c=int(input("m"))
a=[[ 0 for i in range (m)] for i in range (n)]
b=[[ 0 for i in range (m)] for i in range (n)]

for i in range (n):
    for j in range (m):
        a[i][j]= randint(0,3)
for i in range (n):
    print(a[i])
print("mat b")
for i in range (n):
    for j in range (m):
        b[i][j]=a[i][j]*c
for i in range (n):
    print(b[i])
