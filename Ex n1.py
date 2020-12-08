#Proc Saisir
def Saisir():
      global n
      n=int(inpu("Veuillez saisir un nombre"))
      ch=str(n)

#Proc Traiter
def Traiter(n):
      S=0
      ch=str(n)
      for i in range (len(ch)):
          x=int(ch[i])
          if i%2==0:
              x=x*2
              if x>10:
                  x=(x//10)+(x%10)

         S=S+x

       if s%10==0:
           print(n, "est LIHN")
       else:
           print(n, "n'est pas LIHN")



#P.P
Saisir()
Traiter(n)
           
      
