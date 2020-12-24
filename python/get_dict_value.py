# Récupérer la valeur de la clé "prenom", contenue dans le dictionnaire "employes"
# i.e. on doit avoir "Pierre"

employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}

# Version 1
print(employes["01"]["identite"]["prenom"])

# Version 2 
print(employes.get("01").get("identite").get("prenom"))

# Pour aller plus loin : aucune erreur si les clés du dict sont modifiées
print(employes.get("01", {}).get("identgggite", {}).get("prenom", "value inconnue"))
