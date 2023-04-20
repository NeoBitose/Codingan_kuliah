print("=================================")
print("| 1. Sapi Warior  : 690 hari     |")
print("| 1. Sapi Mage    : 420 hari     |")
print("| 1. Sapi Assasin : 530 hari     |")
print("| 1. Sapi Nolep   : 330 hari     |")
print("=================================\n")

batas = int(input("\nBanyak input : "))
a = 1
b = 0
total = 0
waktu = 0

listValue = []

while a <= batas :

    inputValue = int(input(f"input {a} : "))
    listValue.insert(a, inputValue)
    a+=1

while b < batas :

    if listValue[b] == 1 :
        waktu = 690

    elif listValue[b] == 2 :
        waktu = 420

    elif listValue[b] == 3 :
        waktu = 530

    elif listValue[b] == 4 :
        waktu = 330

    total = total + waktu
    b+=1

tahun = int(round(total / 365))
bulan = int(round(total % 365 / 30))
hari = int(round(total % 365 % 30))

print(f"\njumlah hari yang diperlukan ialah : {tahun} Tahun, {bulan} Bulan, dan {hari} Hari")


# pertama ditampilkan sapi apa saja yang akan di ternak
# menentukan berapa sapi yang akan dimasuk dimasukkan ke variable batas 
# lalu input sapi apa saja yang akan diternak dimasukkan ke variable inputValue
# lalu memasukkan data sapi yang akan diternak di list "list_sapi" menggunakan perulangan while yang diulang sebanyak variabel "batas" / banyak sapi yang diternak 
# lalu menghitung total hari sesuai kode sapi yang diinputkan menggunakan perulangan while yang diulang kurang dari sebanyak variabel "batas" / banyak sapi yang diternak
# lalu menghitung taun bulan dan hari yang dibutuhkan untuk merawat sapi sapi tersebut