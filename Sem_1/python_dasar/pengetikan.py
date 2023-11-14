listKiri = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"] # membuat list "listKiri" untuk menampung alphabhet yang diketik menggunakan tangan sebelah kiri
listKanan = [ "y", "u", "i", "o", "p", "h", "j", "k","l","n","m"] # membuat list "listKanan" untuk menampung alphabhet yang diketik menggunakan tangan sebelah kanan

kata = input("\nInput : \n") # menginput kata yang ingin di cek
listTangan = [] #membuat list "listTangan" untuk menampung data tangan apa saja yang digunakan saat ada karakter yang menggunakan tangan yang sama
listChar = [] # menampung karakter pada kata yang di inputkan
listFalse = [] # menampung karakter yang pengetikannya menggunakan tangan yang sama
hasilBool = True # kondisi apakah pengetikan karakter nyaman atau tidak dinilai dari true and false
index = 0 # variabel index sebagai acuan index perulangan

for karakter in kata: # pengulangan sebanyak karakter pada variabel "kata" yang ditampung di variabel karakter

    listChar.append(karakter) # manambahkan value variabel "karakter" pada list "listChar"
    
    # pengkondisian jika karakter berada di list "listKiri" maka tambahkan value kiri pada list "listTangan"
    if karakter in listKiri :
        listTangan.append("kiri")
    # pengkondisian jika karakter berada di list "listKanan" maka tambahkan value kanan pada list "listTangan"
    elif karakter in listKanan :
        listTangan.append("kanan")

#perulangan sebanyak karakter pada list "listChar" yang ditampung di variabel index
while index < len(listChar) :

    # jika variabel "index" sama dengan panjang "listChar" dikurangi 1 maka hentikan perulangan jika tidak maka lanjut
    if index == len(listChar) - 1 : 
        break
    else :
        # pengkondisian jika tangan yang digunakan untuk mengetik karakter satu dengan karakter sesudahnya sama maka "hasilBool" bernilai False 
        if listTangan[index] == listTangan[index+1] :
            hasilBool = False

            # dan menentukan karakter apa yang diketik dengan tangan yang sama dan tangan apa yang digunakan
            if listChar[index] in listKanan :
                listFalse.append(f"{listChar[index]} dan {listChar[index+1]} berada di tangan kanan" )
            elif listChar[index] in listKiri :
                listFalse.append(f"{listChar[index]} dan {listChar[index+1]} berada di tangan kiri" )

    index += 1 # nilai "index" selalu bertambah setiap looping

# menampilkan hasil output berupa "hasilBool", karakter berurutan yang diketik dengan tangan yang sama, dan tangan yang digunakan untuk mengetik karakter tersebut 
print("\nOutput : ")
print(hasilBool)
if hasilBool == True:
    print("Penjelasan Setiap karakter selalu bergantian tangan\n")
elif hasilBool == False:
    print(f"Penjelasan karakter yang berdempetan yakni {listFalse}\n")
