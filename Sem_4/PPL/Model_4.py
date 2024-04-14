import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import json

with open('D:\codingan\python\github_connect\Sem_4\PPL\dataset.json', 'r') as file:
    dataset = json.load(file)
    
# Fuzzyfikasi gejala
gejala = ctrl.Antecedent(np.arange(0, 11, 1), 'gejala')  # Skala 0-10 untuk tingkat keparahan gejala

# Variabel output
penyakit = ctrl.Consequent(np.arange(len(dataset)), 'penyakit')  # Angka penyakit sesuai urutan dalam dataset

# Fuzzyfikasi gejala
gejala.automf(3, names=['rendah', 'sedang', 'tinggi'])

# Fuzzyfikasi penyakit
penyakit.automf(len(dataset), names=[d['nama_penyakit'] for d in dataset])

# Aturan fuzzy
rules = []
for idx, penyakit_data in enumerate(dataset):
    rule = ctrl.Rule(gejala['rendah'] | gejala['sedang'], penyakit[penyakit_data['nama_penyakit']])
    rules.append(rule)

# Membuat kontrol sistem fuzzy
penyakit_ctrl = ctrl.ControlSystem(rules)
penyakit_deteksi = ctrl.ControlSystemSimulation(penyakit_ctrl)

# Menampilkan gejala yang tersedia
print("Gejala yang tersedia:")
for idx, penyakit_data in enumerate(dataset):
    print(idx+1, ".", penyakit_data['nama_penyakit'])

# Meminta input gejala dari pengguna
pilihan_gejala = int(input("Masukkan nomor gejala yang ingin Anda gunakan: "))
input_gejala = dataset[pilihan_gejala - 1]['gejala']

# Memasukkan input
penyakit_deteksi.input['gejala'] = input_gejala

# Melakukan perhitungan
penyakit_deteksi.compute()

# Mendapatkan output
hasil = penyakit_deteksi.output['penyakit']
nama_penyakit = dataset[int(hasil)]['nama_penyakit']

print("Berdasarkan gejala yang Anda pilih, kemungkinan tanaman terkena penyakit:", nama_penyakit)
