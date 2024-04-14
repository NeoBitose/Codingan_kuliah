import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 1. Muat dataset JSON
with open('D:\codingan\python\github_connect\Sem_4\PPL\datasets.json', 'r') as file:
    data = json.load(file)

print(data)
# 2. Persiapkan data
X = [' '.join(d['gejala']) for d in data]
y = [d['nama_penyakit'] for d in data]

# 3. Praproses data
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# 4. Bagi data
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# 5. Latih model
model = MultinomialNB()
model.fit(X_train, y_train)

# 6. Evaluasi model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi:", accuracy)