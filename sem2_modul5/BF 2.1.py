import os
os.system("cls")

def BF(A):
    n = len(A)
    selisih_terbesar = 0
    for i in range(n-1):
        for j in range(i+1, n):
            selisih = abs(A[j] - A[i])
            if selisih > selisih_terbesar:
                selisih_terbesar = selisih
    return selisih_terbesar

panjang =int(input("Masukkan Banyak Array: "))

A=[]
for i in range(panjang):
    A.append(int(input(f"Masukkan angka ke {i+1}: ")))

print(f"Selisih nilai Terbesar dan Terkecil dalam List adalah :{BF(A)}") 
    