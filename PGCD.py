# Lire les deux nombres
a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))

# Sauvegarder les valeurs originales
x, y = a, b

print(f"\n--- Calcul du PGCD({a}, {b}) et des coefficients de Bézout ---\n")

# Variables pour l'algorithme d'Euclide étendu
u1, u2 = 1, 0
v1, v2 = 0, 1
etape = 1

# Tant que b n'est pas nul
while b != 0:
    q = a // b   # quotient
    r = a % b    # reste
    
    print(f"Étape {etape}: {a} = {b} * ({q}) + {r}")
    
    # Mise à jour des valeurs
    a, b = b, r
    
    # Mise à jour des coefficients de Bézout
    u1, u2 = u2, u1 - q * u2
    v1, v2 = v2, v1 - q * v2
    
    etape += 1

# Quand b = 0 → a est le PGCD
pgcd = a

print(f"\n✅ Le PGCD de {x} et {y} est : {pgcd}")
print(f"🧮 Coefficients de Bézout : u = {u1}, v = {v1}")
print(f"➡️ Vérification : {x}*({u1}) + {y}*({v1}) = {x*u1 + y*v1}")

# Vérifier si les deux nombres sont premiers entre eux
if pgcd == 1:
    print("🟢 Les deux nombres sont premiers entre eux.")
