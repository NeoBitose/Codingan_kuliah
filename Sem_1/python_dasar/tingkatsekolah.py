# uncomments salah satu (1 atau 2)

# 1 
#==============================================
# cobaLagi = True

# while cobaLagi == True :
#     try:
#         umur = float(input("masukkan umur : ")) 
#         cobaLagi = False

#     except:
#         print("input salah, harus angka\n")
#         cobaLagi = True
#==============================================

# 2
#==============================================
umur = float(input("masukkan umur : "))
#==============================================

if umur > 0 and umur < 7 :
    print("Tingkat sekolah anda TK")

elif umur >= 7 and umur <= 12 :
    print("Tingkat sekolah anda SD")

elif umur >= 13 and umur <= 15 :
    print("Tingkat sekolah anda SMP")

elif umur >=16 and umur <= 18 :
    print("Tingkat sekolah anda SMA")

elif umur >=19 and umur <= 23 :
    print("Tingkat sekolah anda KULIAH")
 
else : 
    print("udah kerja / belum lahir / tutup usia")

    