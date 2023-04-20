import os #Import library os
os.system("cls") #menggunakan fungsi clear screen untuk membersihkan terminal

def pencarianMerge(listdata, nilai_cari): # membuat fungsi  pencarianMerge() dengan parameter listdata dan nilai_cari
    n = len(listdata)
    if n == 0:
        return 0
    elif n == 1:
        return 1 if listdata[0] == nilai_cari else 0
    else:
        nilai_tengah = n // 2
        nilai_kiri = pencarianMerge(listdata[:nilai_tengah], nilai_cari)
        nilai_kanan = pencarianMerge(listdata[nilai_tengah:], nilai_cari)
        return nilai_kiri + nilai_kanan

panjang_array = int(input("Masukkan Panjang Array A: "))
array_a = []

for i in range(panjang_array):
    array_a.append(int(input(f"Masukkan nilai array ke {i+1}: ")))

anggota = int(input("\nMasukkan nilai anggota yang dicari (K):"))
print(f"Banyaknya anggota dimensi A yang memiliki nilai sama dengan nilai {anggota} adalah sebanyak {pencarianMerge(array_a,anggota)}")