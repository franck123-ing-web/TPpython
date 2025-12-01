a = int(input("Entre le nombre 1: "))
b = int(input("Entre le nombre 2: "))
c = int(input("Entre le nombre 3: "))

nombres = [a, b, c]   # On met les trois nombres dans une liste, on trie,
nombres.sort() # la médiane sera l'élément du milieu (index 1)

mediane = nombres[1]  # l'élément du milieu après tri

print("Mediane -")
print(mediane)
