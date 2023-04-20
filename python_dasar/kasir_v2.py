
# deklarasi variabel inputLagi dan total belanja
inputLagi = True
total = 0

# perulangan inputLagi untuk menghitung belanjaan, jika true maka jalankan penghitungan belanjaan. jika false hentikan perulangan dan menampilkan total belanjaan di akhir
while inputLagi == True : 

# deklarasi variabel loopItem yang digunakan untuk mengulang memasukkan belanjaan baru
    loopItem = True

# memasukkan jumlah barang dan harganya

    jumlah = int(input("\nEntrikan jumlah barang yang dibeli : "))
    harga = int(input("Entrikan harga satuan barang : "))

# proses menghitung total belanja pertama dan seterusnya
    total = total + jumlah * harga

# perulangan loopItem untuk bertanya apakah mau input lagi, jika yang dinputkan selain y atau t maka akan mengulang secara otomatis
    while loopItem == True:

# deklarasi variabel cekItemBaru untuk input pertanyaan ingin mengulang atau tidak
        cekItemBaru = input("\nApakah ada lagi item barang yang akan dientrikan atau tidak ? [y]/[t] ")

# pengkondisian jawaban pertanyaan diatas. jika y maka akan mengulang perulangan inputLagi untuk menghitung belanjaan kembali
        if cekItemBaru == "y" or cekItemBaru == "Y":
            bfj 
            inputLagi = True
            loopItem = False

# jika t maka perulangan inputLagi tidak dijalankan lagi dan akan keluar total belanjaan keseluruhan
        elif cekItemBaru == "t" or cekItemBaru == "T":

            print("Total Pembayaran Rp.", total , "\n")
            inputLagi = False
            loopItem = False

# jika menjawab selain y atau t maka akan mengeluarkan peringatan input salah dan akan mengulang perulangan loopItem
        else:
            print("input nya salah")
            loopItem = True


