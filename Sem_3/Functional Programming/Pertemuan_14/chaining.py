def tambahkan_angka(x):
    return x + 5

def kali_dengan_dua(x):
    return x * 2

def kurangi_angka(x):
    return x - 3

# Rantai fungsi
nilai_awal = 10
hasil_rantai = tambahkan_angka(nilai_awal).kali_dengan_dua().kurangi_angka()

print("Hasil rantai fungsi:", hasil_rantai)