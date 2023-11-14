import os
os.system("cls")

def desbin(angka) :
    tmp_angka = 0
    hasil = 1
    biner = 1
    listhasil = []

    while int(hasil) > 0:
        biner = angka % 2
        if biner == 0:
            tmp_angka = angka
            hasil = angka / 2
            angka = hasil
        elif biner == 1:
            tmp_angka = angka
            hasil = (angka-1) / 2
            angka = hasil
        
        listhasil.append(str(int(biner)))
        print(f"{int(tmp_angka)} : 2 = {int(hasil)} ----> {int(biner)}")

    print(f"\nHasil konversi {' '.join(reversed(listhasil))}\n")
    
    return ''.join(reversed(listhasil))

def bindes(angka) :
    lenangka = len(angka)
    listbiner = []
    hasil = 0

    for i in range(lenangka):
        # print(lenangka)
        listbiner.append(int(angka[lenangka-1]))
        lenangka -= 1
        
    for i in range(len(listbiner)):
        pangkat = 1
        if listbiner[i] == 1 : 
            for j in range(1, i+1):
                pangkat = pangkat * 2
            print(f"{listbiner[i]} => 2 pangkat {i} nilainya {pangkat}")
            hasil = hasil + pangkat
        else :
            print(f"{listbiner[i]} => 2 pangkat {i} binernya 0")
        
    print(f"\nHasil konversi {hasil}\n")
    

print("Pilih menu")
print("1. desimal ke biner")
print("2. biner ke desimal")
pilihan = input("masukkan pilihan : ")

if pilihan == "1" :

    os.system("cls")
    bilangan = int(input("\nMasukkan angka desimal : "))
    # print(desbin(bilangan))
    bindes(desbin(bilangan))


if pilihan == "2" :

    os.system("cls")
    bilangan = input("\nMasukkan angka biner : ")
    bindes(bilangan)
    
    
