cobaLagi = True

while cobaLagi == True :
    try:
        nilai = float(input("masukkan nilai : ")) 
        cobaLagi = False

    except:
        print("input salah, harus angka\n")
        cobaLagi = True

# nilai = float(input("masukkan nilai : "))

if nilai >= 0 and nilai <= 69 :
    print("anda mendapat nilai D")

elif nilai >= 70 and nilai <= 79 :
    print("anda mendapat nilai C")

elif nilai >= 80 and nilai <= 89 :
    print("anda mendapat nilai B")

elif nilai >=90 and nilai <= 100 :
    print("anda mendapat nilai A")

else : 
    print("invalid input")

    