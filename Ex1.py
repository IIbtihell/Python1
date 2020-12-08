n=int(input("n="))
if n <5:
    n=int(input("n="))
t1=[0]*n
t2=[0]*n
t3=[0]*n
for i in range (n):
        t1[i]=int(input("donner t1"))
        if t1[i]<0:
            t1[i]=int(input("donner t1"))


for i in range (n):
    t2[i] = int(input("donner t2"))
    if t2[i] < 0:
        t2[i] = int(input("donner t2"))

for i in range (n):
    t3[i] = t1[i]+t2[i]

print(t1)
print(t2)
print(t3)
