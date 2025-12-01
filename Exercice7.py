nombres = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# j'initialise les compteurs
compteurpaire = 0  # Compteur pour les nombres pairs
compteurimpaire = 0   # Compteur pour les nombres impairs

# je parcours chaque nombre de la série
for num in nombres:
    if num % 2 == 0:  # Si le reste de la division par 2 est 0  pair
        compteurpaire += 1
    else:             # Sinon  impair
        compteurimpaire += 1

# Affichage des résultats
print("Nombre de nombres pairs :", compteurpaire)
print("Nombre de nombres impairs :", compteurimpaire)
