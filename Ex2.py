n=int(input("n="))
m=int(input("m="))
if n <5:
    n=int(input("n="))
if m <5:
    m=int(input("m="))

t1=[0]*n
t2=[0]*m
p=0
for i in range (n):
        t1[i]=int(input("donner t1"))
        if t1[i]<0:
            t1[i]=int(input("donner t1"))


for j in range (m):
    t2[j] = int(input("donner t2"))
    if t2[j] < 0:
        t2[j] = int(input("donner t2"))

for i in range(n):
    for j in range(m):
        p=p+t1[i]+t2[i]

print(t1)
print(t2)
print(p)

