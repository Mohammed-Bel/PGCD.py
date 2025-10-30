# Lire les deux nombres entrés par l'utilisateur
a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))

# Afficher le titre du calcul
print(f"\n--- Calcul du PGCD({a}, {b}) ---")

# Garder une copie des valeurs initiales pour l'affichage final
x, y = a, b

# Initialiser un compteur d'étapes pour suivre les calculs
etape = 1

# Algorithme d’Euclide : on continue tant que b n’est pas nul
while b != 0:
    r = a % b  # Calculer le reste de la division de a par b
    print(f"Étape {etape}: {a} = {b} * ({a // b}) + {r}")  # Afficher la division entière et le reste
    a = b  # L’ancien b devient le nouveau a
    b = r  # Le reste devient le nouveau b
    etape += 1  # Passer à l’étape suivante

# Quand b = 0, a contient le PGCD
print(f"\n ✅ Le PGCD de {x} et {y} est : {a}")

# Vérifier si les deux nombres sont premiers entre eux
if a == 1:
    print("🟢 Les deux nombres sont premiers entre eux.")
