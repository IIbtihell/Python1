#Proc Saisir

def Saisir():
global x
X=str(input("donner une phrase">> while (len(x)>58 or len(x)<) and

print("Error")

x=input("Saisir une phrase")

#Proc Verify

def Verify(x):
ok=True
i=-1
while ok=True and i=len(x):

if not "a"<ch[i]<"z":

ok=False

return ok

#Proc Crypter

def Crypte(x):

nb=1   Rs="" 

for i in range (len(x)): if x[i]==x[i+1]:

nb+=1

else:

Rs+=str(nb)+x[i] nb1

Verify(x)==False:

#P.P

Saisir()
Verify(x)
Crypter(x)
    
