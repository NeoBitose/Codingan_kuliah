import os
os.system("cls")

panjang=int(input("Masukkan Panjang Array: "))

A=[]
for i in range(panjang):
    A.append(int(input(f"Masukkan Angka ke {i+1}: ")))

varK =int(input("Masukkan key (k):"))

def BF(dimensi_A, key):
    Hasil = 0
    i = 0
    for i in range(len(dimensi_A)):
        if dimensi_A[i] == key:
            Hasil += 1
    return Hasil

print(f"Banyaknya anggota dimensi A yang memiliki nilai sama dengan K adalah: {BF(A,varK)}")         