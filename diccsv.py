dico=[] #c'est une liste
csv.register_dialect('myDialect', delimiter=';', quotechar='|')
with open('testCSVCopierCollerSite.csv') as myFile:
    reader = csv.DictReader(myFile, dialect='myDialect')
    for row in reader:  #row est un dictionnaire
        print(row)
        print(row['Album']) #affiche l'élément avec la clé Album seulement
        dico.append(row)	# ajoute le dicitionnaire row à la liste 'dico'
print(dico)

print(dico[0]['Album'])  #va afficher 'Master of Puppets'