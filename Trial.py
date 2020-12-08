# -*- coding: utf-8 -*-

def pgcd(a,b) :  
   while (a*b !=0):
      if(a>b):
         a=a-b
      else:
         b=b-a
   if(a==0):
      return b
   else:
      return a


def ppcm(a,b) :
   m = a
   while (m%a != 0 or m%b !=0):
      m = m + 1
   return m


def premier(a) :
   nb=0
   for i in range (1,n//2+1):
      if n % i ==0 :
         nb=nb+i
   if nb==1 :
      return True
   else :      
      return False 

def Facteur_premier(n):
   t , j = [], 2
   while n > 1:
      if (n % j) == 0:
         t.append(j)
         n //= j
      else:
         j += 1
   return t

def parfait(n):
   S=0
   for i in range (1,n//2+1):
      if n % i ==0 :
         S=S+i
   if S==n :
      return True
   else :      
      return False  


def Saisir():
   ch=input("donner un chaine majuscul ")
   while(ch.isupper()==False):
      ch=input("donner un chaine majuscul ")
   return ch




def nb_voyelle(ch):
   vowels= {'A','E','Y','U','I','O'}
   number_vowels = 0
   for i in ch:
      if(i in vowels):
         number_vowels = number_vowels + 1
   return number_vowels 



def inverse(ch):
   ch1 = ch[::-1]
   return ch1


def palindrome(ch):
   ch2 = ch[::-1]
   if (ch==ch2):
      return True
   else:
      return False


# Corps du programme
global ch
global ch1
global ch2
while True :
   print ("""MENU :\n
    1 - Calculer le PGCD de deux nombres\n
    2 - Calculer le PPCM de deux nombres\n
    3 - Déterminer si un nombre est premier\n
    4 - Donner la décomposition en facteur premier d'un nombre\n
    5-  Tester un nombre parfait ou non\n
    6-  Manipulation chaine de caractères (contient un sous menu :)) \n
    q - Quitter\n""")

   choix =input("\nVotre choix :")
   # Quitter
   if (choix == 'q' or choix =='Q') :
      break       
   # choix 1 : pgcd
   elif (choix == '1') :
      print ("\nSaisissez 2 entiers :")
      entier1 = int(input("1er : "))
      entier2 = int(input(" 2eme  :") )
      print ("le pgcd de  ", entier1, " et ", entier2, " est ", pgcd(entier1,entier2))
   # choix 2 : ppcm
   elif (choix == '2') :
      print ("\nSaisissez 2 entiers: ")
      entier1 = int(input("1er : "))
      entier2 = int(input(" 2eme  :") )
      print( "le ppcm de ", entier1, " et ", entier2, " est ", ppcm(entier1,entier2))
   elif (choix == '3') :
      entier =  int(input(" Saisissez un entier: "))
      if premier(entier) :
         print (entier, " est premier")
      else :
         print (entier, " n'est pas premier")
   elif (choix == '4') :
      entier = int(input(" Saisissez un entier: "))
      print ("La décomposition de ", entier, "e n premiers est", Facteur_premier(entier))
   elif (choix == '5') :
      entier =  int(input(" Saisissez un entier: "))
      if parfait(entier) :
         print (entier, " est parfait")
      else :
         print (entier, " n'est pas parfait")    

   elif (choix == '6') :
      print ("\n Traitement d'une chaine de caractere : ")
      while True :
         print ("""MENU :\n
             A.  Saisir une chaine majuscule\n
             B.  Calculer le nombre voyelle \n
             C.  Inverser la chaine\n
             D.  Tester le palindrome\n
             (Q, q )- Quitter\n""")

         choix =input("\nVotre choix :")
         # Quitter
         if (choix == 'q' or choix =='Q') :      
            break 
         elif (choix == 'A') :
            ch=Saisir()
            print('ch=',ch)   
         elif (choix == 'B') :
            print('nb_voyelle=',nb_voyelle(ch))
         elif (choix == 'C') :
            print(ch,' inverser =',inverse(ch))
         elif (choix=='D'):
            yes=palindrome(ch)
            if yes==True:                 print(ch,' est palindrome.')
            else:
               print(ch,' est non palindrome. ')