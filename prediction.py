import joblib
#from sklearn.feature_extraction.text import TfidfVectorizer

#charger le modèle
model = joblib.load('./prediction.pkl')
vector = joblib.load('./vectorizer.pkl')

#récupérer les données dans le fichier txt
with open('comment.txt', 'r') as f:
    texte = f.read()

X = vector.transform([texte])
 
#prédiction
prediction = model.predict(X)

#affichage du résultat
if prediction == 1:
    print("positive")
elif prediction == 0:
    print("neutre")
elif prediction == -1:
    print("negative")