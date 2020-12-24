# Renvoyer la liste triée selon le numéro

from operator import itemgetter

liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]

# Trier la liste ici

liste.sort(key=itemgetter(1))
print(liste)