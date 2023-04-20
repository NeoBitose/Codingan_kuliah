import os

def binarySearch(data, listdata) :
    
    panjang_list = len(listdata)
    median = int((panjang_list) // 2)
        
    if data < listdata[median] :
        indeks = median - 1
        while indeks >= 0:
            if data == listdata[indeks]:
                print(f"Data yang anda cari ditemukan, {listdata[indeks]} pada index ke {indeks}")
                break
            elif data != listdata[indeks] and indeks == 0:
                print("Data yang anda cari tidak ditemukan!, coba kata kunci lain")
                break
            indeks -= 1
            
    elif data >= listdata[median] :
        indeks = median - 1
        while indeks < panjang_list:
            if data == listdata[indeks]:
                print(f"Data yang anda cari ditemukan, {listdata[indeks]} pada index ke {indeks}")
                break
            elif data != listdata[indeks] and indeks == panjang_list-1:
                print("Data yang anda cari tidak ditemukan!, coba kata kunci lain")
                break
            indeks += 1
            
while True :
     
    os.system("cls")
    
    database = [0,1,2,3,4,5,6,7,8,9]
    kata_kunci = int(input("Data yang ingin dicari : "))

    binarySearch(kata_kunci, database)

    print("\nApakah anda ingin mengulang kembali ? ")
    lagi = input("(Y/y untuk lanjut) :  ")
    if lagi.lower() != "y": break