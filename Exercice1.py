def nombresdifferents(numbers):
    
    # On transforme la liste numbers en set (ensemble)
    # Un set ne garde qu'une seule occurrence de chaque élément
    # si la taille change, c'est qu'il y avait des doublons
    return len(numbers) == len(set(numbers))


# Tests
print(nombresdifferents([1, 5, 7, 9]))      # Tous différents = True
print(nombresdifferents([2, 4, 5, 5, 7, 9])) # Ici il y a deux "5" = False
