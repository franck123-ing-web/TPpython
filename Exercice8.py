# je parcours les entiers de 1 à 50 inclus
for i in range(1, 51):
    # Vérifie  si le nombre est multiple de 3 et 5
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    # Vérifie si le nombre est multiple de 3
    elif i % 3 == 0:
        print("fizz")
    # Vérifie si le nombre est multiple de 5
    elif i % 5 == 0:
        print("buzz")
    # Sinon on affiche le nombre
    else:
        print(i)
