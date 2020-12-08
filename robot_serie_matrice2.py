
def saisir():
   
        L=int(input("Entrez le nombre des lignes de Matrice : "))
        C=int(input("Entrez le nombre des colonnes de Matrice: "))
        X=int(input("Entrez la position initial des lignes de Robot: "))
        Y=int(input("Entrez la position initial des colonnes de Robot: : "))
        ch=input("Entrez le mot de parcours: ")
        return (X,Y,L,C,ch)
    
    
def Robot(X,Y,L,C,ch ):
    i=0
    while(X<L and Y<C )and(i<len(ch)):
        if(ch[i]=="D"):
            X=X+1
        if(ch[i]=="G"):
            X=X-1    
        if(ch[i]=="H"):
            Y=Y+1
        if(ch[i]=="B"):
            Y=Y-1
        i=i+1
        
    if(i==len(ch)):
        print('Nouvelle position du Robot est:(',X,',',Y,')')
    else:
        print('attention cas de  dépassement ')
    print('i=',i)    
 
print('programme principale')
#L=19   C=17  X=4   Y=3  ch= "GBBBHDDDDGGHH"  //
(X,Y,L,C,ch)=saisir()
Robot(X,Y,L,C,ch )

