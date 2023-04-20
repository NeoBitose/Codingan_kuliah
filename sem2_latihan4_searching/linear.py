import os

def linearSearch(data, listdata) :
    
    for i in range(len(listdata)) :
        
        if data == str(listdata[i]):
            print(f"Data yang anda cari ditemukan, {listdata[i]} pada index ke {i}")
            break
        
        elif data != str(listdata[i]) and i == len(listdata) - 1:
            print("Data yang anda cari tidak ditemukan!, coba kata kunci lain")
        

while True :
    os.system("cls")
    
    database = [1,2,3,4,5,6,7,8,9,0]
    kata_kunci = input("Data yang ingin dicari : ")

    linearSearch(kata_kunci, database)
    
    print("\nApakah anda ingin mengulang kembali ? ")
    lagi = input("(Y/y untuk lanjut) :  ")
    if lagi.lower() != "y": break