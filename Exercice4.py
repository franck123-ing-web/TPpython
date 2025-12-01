i = input("Saisissez une chaine : ")

# j'initialise deux compteurs
lettres = 0
chiffres = 0

# On parcourt chaque caractère de la chaîne
for char in i:
    if char.isalpha():     # Vérifie si c'est une lettre
        lettres += 1
    elif char.isdigit():   # Vérifie si c'est un chiffre
        chiffres += 1

# Affichage du résultat
print("Lettres", lettres)
print("Chiffres", chiffres)
