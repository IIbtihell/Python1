def saisir(n):
        while n < 10 and n > 20:
            n = int(input("n"  ,))
        return n
def remplir(t,n):
    for i in range (n):
        ch=str(t[i])
        a=t[i]%10
        while len(ch): 3 and a= 0 :
            t[i]=int(input("donner element"))
    return t[i]
def afficher(t,n):
    for i in range :
        print(t[i])

def tri(t,n) :
    for i in range(n-1) :
        Posmin=i

        aux=T[i]
        t[i] = T[Posmin]
        t[Posmin]=aux

def trie_element(t,n):
    for i in range (n):
        a=t[i]//100
        b=(t[i]%100)//10
        if (a<b):
            t[i]=b*100+a*10

def inverser(t,n):
    i=0
    j=n-1
    while(i<j):
        aux=t[i]
        t[i]=t[j]
        t[j]=aux
        i=i+1
        j=j-1

#print(afficher(t,n))

print(n)
remplir()
trie_element()
inverser()
