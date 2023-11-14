
# inputkan kalimat yang akan di hitung karakternya lalu ditampung di variable "karakter"
kalimat = input("masukkan kalimat : ") 

# casefold() fungsinya buat ngubah semua huruf jadi huruf kecil karena di soal minta case insesitive (besar kecil sama aja)
# jadi nanti semua huruf dijadikan kecil biar semua setara
# variable "kalimatKecil" itu untuk menampung kalimat yang di input yang sudah jadi kecil
kalimatKecil = kalimat.casefold() 

# membuat dictionary yang namanya "jumlahChar"
jumlahChar = {}

# membuat dictionary yang namanya "hasil"
hasil = {}

# membuat variable yang namanya "jumlahCharLebihDari1" sebagai penampung nilai, 
# ada berapa karakter yang muncul lebih dari satu kali misal aaliff nah itu ada 2 karakter yang mucul lebih dari satu
# dan 2 itu tadi nantinya ditampung di variable ini
jumlahCharLebihDari1 = 0

# perulangan untuk menampilkan setiap karakter di variable "kalimatKecil" trus ditampung di variable "karakter"
for karakter in kalimatKecil:

# pengkondisian jika ada karakter yang sama di "jumlahChar" maka banyak dari karakter itu ditambah lagi 1
    if karakter in jumlahChar:
        jumlahChar[karakter] += 1

# pengkondisian jika ada karakter di "jumlahChar" maka banyak dari karakter itu diberi nilai 1
    else: 
        jumlahChar[karakter] = 1

# pengulangan sebanyak "jumlahChar" lalu dimasukkan ke variabel "jumlah"
for index in jumlahChar:

# pengkondisian jika ada karakter dari list "jumlahChar" urutan ke "index" lebih dari satu,
# maka jumlah karakter yang lebih dari 1 bertambah 1 dan ditampung di variable "jumlahCharLebihDari1"
    if jumlahChar[index] > 1: 
        jumlahCharLebihDari1 += 1

#lalu munculkan berapa banyak karakter yang muncul lebih dari 1 kali
# jika mau munculin banyaknya aja sampai sini cukup dausah diterusin codingannya
print(f"karakter yang lebih dari 1 ada {jumlahCharLebihDari1} yaitu")

# pengulangan sebanyak karakter yang sudah diinputkan dan di perkecil tulisannya,
# lalu dimasukkan ke variabel "karakter"
for karakter in kalimatKecil:

# jika di list "jumlahChar" pada key yang sama dengan variabel "karakter" lebih dari 1 
# maka masukkan kedalam list "hasil" dengan key sama dengan "karakter" dan value sama dengan value list "jumlahChar" 
# urutan ke "karakter"
    if jumlahChar[karakter] > 1: 
        hasil[karakter] = jumlahChar[karakter]

# menampilkan hasil dari perulangan dan pengkondisian diatas yagn ditampung pada list "hasil"
# yang berisi data karakter yang muncul lebih dari 1 kali
print(hasil) 