# Install library scikit-learn jika belum terinstall
# pip install scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.tree import export_text

# Membaca data dari CSV
data = pd.read_csv('ai.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV Anda

# Mengidentifikasi kolom dengan tipe data string
string_columns = data.select_dtypes(include=['object']).columns

# Mengonversi data string menjadi numerik menggunakan LabelEncoder
label_encoder = LabelEncoder()
for column in string_columns:
    data[column] = label_encoder.fit_transform(data[column])

# Pisahkan atribut (X) dan label (y)
X = data.drop('Cancer', axis=1)  # Gantilah 'Cancer' dengan nama kolom label Anda
y = data['Cancer']

# Bagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi model Decision Tree
model = DecisionTreeClassifier()

# Melatih model pada data latih
model.fit(X_train, y_train)

# Membuat prediksi pada data uji
y_pred = model.predict(X_test)

# Menghitung akurasi model
accuracy = accuracy_score(y_test, y_pred)
print(f'Akurasi: {accuracy}')

# Menampilkan struktur decision tree
tree_rules = export_text(model, feature_names=list(X.columns))
print(tree_rules)
