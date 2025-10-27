# Programme pour calculer le PGCD de deux nombres

# Lecture des deux nombres
A = int(input("Entrez le premier nombre A : "))
B = int(input("Entrez le deuxième nombre B : "))

# Algorithme d'Euclide
while B != 0:
    R = A % B
    A = B
    B = R

# Affichage du résultat
print("Le PGCD est :", A)
