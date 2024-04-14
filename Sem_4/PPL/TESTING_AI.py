# Impor library yang diperlukan
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Data gejala penyakit dan labelnya
gejala = [
    'demam tinggi',
    'batuk',
    'sakit tenggorokan',
    'pilek',
    'sesak napas',
    'diare',
    'mual',
    'pusing',
    # tambahkan gejala lainnya sesuai kebutuhan
]

label = [
    'flu',
    'flu',
    'flu',
    'flu',
    'flu',
    'gastroenteritis',
    'gastroenteritis',
    'migrain',
    # tambahkan label lainnya sesuai kebutuhan
]

# Konversi teks menjadi vektor fitur menggunakan TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(gejala)

# Bagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.2, random_state=42)

# Latih model klasifikasi (misalnya, SVM)
classifier = SVC(kernel='linear')
classifier.fit(X_train, y_train)

# Prediksi label untuk data uji
predictions = classifier.predict(X_test)

# Evaluasi performa model
accuracy = accuracy_score(y_test, predictions)
print("Akurasi:", accuracy)
print("\nLaporan Klasifikasi:\n", classification_report(y_test, predictions))
