batas = int(input("\nBanyak input : "))
a = 1
b = 0

listValue = []
listChar = []

while a <= batas :

    inputValue = input(f"input {a} : ")
    listValue.append(inputValue)
    a+=1

while b < batas : 
    
    c = 0
    print("\nHasil : ")
     
    for d in listValue[b] :
        
        listChar.append(d)

    while c < len(listChar) : 

        if c == len(listChar) - 1 :
            break
        else :
            jumlahNilai1 = ord(listChar[c])
            jumlahNilai2 = ord(listChar[c+1])
            hasil = jumlahNilai1 - jumlahNilai2

            if jumlahNilai1 < jumlahNilai2 :
                print(f"{listChar[c]} kurang dari {listChar[c+1]}, selisihnya ialah {abs(hasil)}")
            elif jumlahNilai1 > jumlahNilai2 : 
                print(f"{listChar[c]} lebih dari {listChar[c+1]}, selisihnya ialah {abs(hasil)}")
            elif jumlahNilai1 == jumlahNilai2 : 
                print(f"{listChar[c]} sama dari {listChar[c+1]}, selisihnya ialah {abs(hasil)}")
            
        c+=1
    b+=1

    listChar = []


# membuat variabel "batas" untuk menampung banyak input kata  
# menginput kata saja yang mau dihitung nilai ASCII lalu dimasukkan kedalam list inputValue dengan perulangn sebanyak variabel "batas" 
# membuat perulangan sebanyak variabel "batas" untuk memunculkan hasil selisih setiap katanya
# memasukkan setiap karakter pada kata yang diinput kedalam variabel listChar
# lalu di cek selisih antara karakter satu dengan karakter selanjutnya menggunakan perulangan while sebanyak karakter yang ada pada kata tersebut
# lalu mengecek apakah karakter satu lebih kecil atau kebih besar nilai ASCII dibandingkan karakter selanjutnya
# memunculkan hasil perbandingan besar kecil dan menampilkan hasil selisih antara 2 karakter tersebut
# mengulang terus kegiatan oengecekan perbandingan dan selisih nilai ASCII hingga kata habis