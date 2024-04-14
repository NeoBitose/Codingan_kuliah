# Impor library yang diperlukan
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Data gejala penyakit dan labelnya
gejala = [
    "Bercak pada tangkai",
    "Bercak muda berbentuk bulat kecil berwarna coklat gelap ",
    "Bercak pada daun berbentuk oval",
    "Pada kulit gabah bercak berwarna hitam",
    "Ukuran bercak bisa mencapai 1cm",
    "Daun dan pelepah terdapat bercak",
    "Bercak daun dan pelepah berbentuk belah ketupat",
    "Kehampaan malai padi",
    "Tangkai mulai membusuk dan patah",
    "Bercak pada daun berwarna keputih-putihan/keabu-abuan",
    "Banyak anakan menyerupai rumput",
    "Daun Sempit",
    "Daun Kaku",
    "Malai yang dihasikan sedikit bahkan tidak sama sekali",
    "Daun bercak berwarna coklat",
    "Daun yang terserang mengering mulai ujung",
    "Tanda bercak pada pelepah daun dan helai daun",
    "Gabah tidak terisi penuh/hampa",
    "Tanaman mulai rebah",
    "Pertumbuhan tanama kerdil",
    "Pelepah daun memendek",
    "Daun menguning sampai jingga dari pucuk",
    "Tanaman menjadi kerdil",
    "Daun tua ada bintik-bintik bekas tusukan serangga penular",
    "Berkurangnya jumlah anakan",
    "Umumnya menyerang pada tanaman muda (1-2 minggu)",
    "Serangan terjadi pada daun yang luka berupa bercak kebasahan",
    "Warna bercak hijau keabu-abuan",
    "Daun menggulung, mengering warna abu-abu keputihan"
]

label = [
    'Bercak Coklat',
    'Bercak Coklat',
    'Bercak Coklat',
    'Bercak Coklat',
    'Bercak Coklat',
    'Penyakit Blast',
    'Penyakit Blast',
    'Penyakit Blast',
    'Penyakit Blast',
    'Penyakit Blast',
    'Kerdil Rumput',
    'Kerdil Rumput',
    'Kerdil Rumput',
    'Kerdil Rumput',
    'Kerdil Rumput',
    'Hawar Pelepah Daun',
    'Hawar Pelepah Daun',
    'Hawar Pelepah Daun',
    'Hawar Pelepah Daun',
    'Tungro',
    'Tungro',
    'Tungro',
    'Tungro',
    'Tungro',
    'Tungro',
    'Kresek',
    'Kresek',
    'Kresek',
    'Kresek'
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
