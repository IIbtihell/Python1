une_chaine = "Classe Informatique"
compteur_voyelles = 0
compteur_consonnes = 0

for lettre in une_chaine :
    if lettre in "aeiouyAEIOUY":
        print (lettre, "est une voyelle")
        compteur_voyelles = compteur_voyelles + 1
    else :
        print (lettre, "est une consonne")
        compteur_consonnes = compteur_consonnes + 1
print ("Il y a, dans cette phrase,",compteur_voyelles,"voyelle(s),"\
       ,compteur_consonnes,"consonne(s),")
