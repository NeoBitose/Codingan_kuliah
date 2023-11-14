import os
os.system("cls")

def selisihLinear(listdata):
    
    n = len(listdata)
    hasil_selisih = 0
    nilai_a = 0
    nilai_b = 0
    
    for a in range(n-1):
        selisih_tmp = abs(listdata[a] - listdata[a+1])
        if selisih_tmp > hasil_selisih:
            hasil_selisih = selisih_tmp
            nilai_a = listdata[a]
            nilai_b = listdata[a+1]
                
    return hasil_selisih, nilai_a, nilai_b

panjang_array = int(input("Masukkan Panjang Array A: "))
array_a = []

for i in range(panjang_array):
    array_a.append(int(input(f"Masukkan nilai array ke {i+1}: ")))

print(f"\nNilai array A : {array_a}")
print(f"Selisih terbesar antara dua bilangan berurutan di array A adalah {selisihLinear(array_a)[0]} antara bilangan {selisihLinear(array_a)[1]} dan {selisihLinear(array_a)[2]}")         