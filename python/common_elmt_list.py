# Renvoyer une liste des éléments communs aux 2 listes

liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]

# Premiere version
common_list = []

for elmt1 in liste_01 : 
    for elmt2 in liste_02 : 
        if elmt1 == elmt2 : 
            common_list.append(elmt1)

print(common_list)

# Deuxieme version 
print([elmt1 for elmt1 in liste_01 for elmt2 in liste_02 if elmt2 == elmt1])

# Troisieme version 
print([elmt for elmt in liste_01 if elmt in liste_02])

# Quatrieme version : SOLUTION
print(list(set(liste_01).intersection(set(liste_02))))