# Trouver l'erreur de syntaxe et la corriger 

liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]

resultat = [i*(i+1%(i*5)) for i in sorted(list(set(liste)))]
print(resultat)