# j'initialise les deux premiers nombres de la suite
a, b = 0, 1

# Tant que le nombre ne dépasse pas 50, on continue
while b <= 50:
    print(b)      # j'affiche le nombre actuel
    a, b = b, a+b # je calcule le suivant
