
A = int(input("Entrez le premier nombre A : "))
B = int(input("Entrez le deuxième nombre B : "))

while B != 0:
    R = A % B
    A = B
    B = R

print("Le PGCD est :", A)