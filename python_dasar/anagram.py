# menginputkan kalimat 1 dan kalimat 2 untuk nantinya dicek kedua kalimat adalah anagram atau tidak
kalimat1 = input("masukkan kalimat pertama : ") # varibel kalimat1 yang nilainya di input
kalimat2 = input("masukkan kalimat kedua : ") # varibel kalimat2  yang nilainya di input

# mengurutkan karakter kalimat1 dan  kalimat2
# Fungsi sorted() digunakan untuk mengurutkan suatu data dari yang terkecil atatu urutan alphabet terkecil ke terbesar 
# baik secara ascending (naik) atau descending (turun)
ceKalimat1 = sorted(kalimat1)
ceKalimat2 = sorted(kalimat2)

# pengecekan hasil sortir apakah sama atau berbeda
#if else itu buat ngecek suatu kondisi

# kondisi kalimat 1 dan 2 sama
if ceKalimat1 == ceKalimat2 : 
# jika hasil sortir sama / kalimat anagram jalankan kode dibawah
    print("ini kalimat anagram, aku doakan kamu naik haji")

# kondisi kalimat 1 dan 2 berbeda
else :
# jika hasil sortir berbeda / bukan kalimat anagram akan dijalankan kode dibawah
    print("ini bukan kalimat anagram, coba banyak sadaqah")