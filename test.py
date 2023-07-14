#récupérer les données dans le fichier txt
with open('comment.txt', 'r') as f:
    texte = f.read()

print(texte)
print(type(texte))