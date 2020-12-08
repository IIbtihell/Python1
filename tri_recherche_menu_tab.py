def saisir():
    N=int(input("Donner N :"))
    return N   

def remplir(T,N):
  T=[0]*N
  for i in range(N):
    T[i]=int(input("Saisir l'élement {0} : ".format(i+1)))
  return T
def afficher(T,N):

    for i in range(N):
       print(" ",T[i])
   
    return T

#fonction tri_selection
def tri_selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1, len(tab)):
         if tab[min] > tab[j]:
          min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab

#fonction recherche dichotomie
def recherche_dichotomique( x,tab,N ):
    a = 0
    b = len(tab)-1
    m = (a+b)//2
    while a < b and tab[m] != x:
        if tab[m] >x :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
        
    if tab[m] == x :
        print(x,' existe dans t a la position :',m)
    else:   
        print(x,' non existe dans t ')


def premier(n):
  S=0  
  for i in range (1,n+1,1):
      if n % i ==0 :
         S=S+1
  if S==1 :
      return True
  else :
      return False

def elements_premier(T,N):
   for i in range(N):
      test=premier(T[i])
      if test == True:
             print(T[i],end=", ")
    
       


# Programme principale pour tester le code ci-dessus
global N

while True :
    print ("""MENU :\n
    1 - Saisir la taille de tableau :\n
    2 - Remplir le tableau :\n
    3 - Affichage le tableau :\n
    4 - Trier le tableau par selection :\n
    5 - les nombres premiers dans le tableau   :\n
    6 - recherche_dichotomique dans le tableau :\n
    q - Quitter\n""")
    
    choix=input("\nVotre choix :")
    
    
   
    if (choix =='q' or choix =='Q') :
        break
          
    elif (choix =='1'):
      N=saisir()
       
    elif (choix =='2'):
      T=[]*N
      print(' remplissage de T')
      T=remplir(T,N)
           
    elif (choix =='3'):
      print(' affichage de T')
      print(T)
      
    elif (choix =='4'):
      tri_selection(T)
      print (" tableau_trié ",T) 

    elif (choix =='5'):
      print (" les nombres premiers dans le tableau ",elements_premier(T,N))
    elif (choix =='6'):
      print (" rechercher X dans le tableau ")
      x=int(input('donner x a rechercher :'))
      recherche_dichotomique( x,T,N)







