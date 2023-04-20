import os
os.system('cls')

def selisihMerge(listdata):
    tmp = len(listdata)
    n = len(listdata)
    if n == 1:
        return 0
    elif n == 2:
        return abs(listdata[0] - listdata[1])
    else:
        nilai_tengah = n // 2
        kiri = selisihMerge(listdata[:nilai_tengah])
        kanan = selisihMerge(listdata[nilai_tengah:])
        
        if n == tmp:
            cross = abs(listdata[nilai_tengah-1] - listdata[nilai_tengah])
        else:
            cross = 0
        data = max([kiri,kanan,cross])
        return data 

panjang_array = int(input("Masukkan Panjang Array A: "))
array_a = []

for i in range(panjang_array):
    array_a.append(int(input(f"Masukkan nilai array ke {i+1}: ")))

print(f"\nNilai array A : {array_a}")
print(selisihMerge(array_a))