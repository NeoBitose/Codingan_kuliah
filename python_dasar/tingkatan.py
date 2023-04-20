
cekUmur = int(input("masukkan cekUmur : "))

if cekUmur > 0 and cekUmur < 7 :
    print("Tingkat sekolah anda TK")

elif cekUmur >= 7 and cekUmur <= 12 :
    print("Tingkat sekolah anda SD")

elif cekUmur >= 13 and cekUmur <= 15 :
    print("Tingkat sekolah anda SMP")

elif cekUmur >=16 and cekUmur <= 18 :
    print("Tingkat sekolah anda SMA")

elif cekUmur >=19 and cekUmur <= 23 :
    print("Tingkat sekolah anda KULIAH")
 
else : 
    print(" udah kerja / belum lahir ")
