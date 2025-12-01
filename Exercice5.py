# je parcours tous les nombres de 1500 à 2700 inclus
for x in range(1500, 2701):
    # je vérifie si le nombre est divisible par 7 et multiple de 5
    if x % 7 == 0 and x % 5 == 0:
        print(x, end=",")  # Affiche tous les nombres sur la même ligne, séparés par des virgules
