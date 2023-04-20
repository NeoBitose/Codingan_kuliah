import os
import pandas as pd
from tabulate import tabulate

os.system('cls')

file_mahasiswa = "sem2_modul3&4/datamahasiswa.csv"
tabel = ["Kelas", "NIM", "Nama", "Nilai"]

dataframe = pd.read_csv(file_mahasiswa)
df = dataframe.values.tolist()

print("Data Nilai Mahasiswa")
print("=================================")
print(tabulate(df,headers=tabel,tablefmt='fancy_grid'))

ulang = 0

while ulang < len(df) :
    
    indeks_tmp = ulang
    indeks_tukar = ulang 
    
    for cek in range(ulang+1, len(df)):  
        if df[cek][3] > df[indeks_tukar][3]: 
            indeks_tukar = cek
                
    (df[indeks_tmp], df[indeks_tukar]) = (df[indeks_tukar], df[indeks_tmp])
    ulang += 1
    
# print(tabulate(df,headers=tabel,tablefmt='fancy_grid'))

for ulang in range(len(df)-1) :
    
    tmp_data = df[ulang+1]
    tmp_nilai = df[ulang+1][3]
    tmp_nama = df[ulang+1][2]
    
    while ulang >= 0 and tmp_nilai == df[ulang][3] and tmp_nama < df[ulang][2] :
        df[ulang+1] = df[ulang]
        ulang -= 1
    df[ulang+1] = tmp_data
    
print("\nData Nilai Mahasiswa Setelah Diurutkan")
print("=================================")
print(tabulate(df,headers=tabel,tablefmt='fancy_grid'))