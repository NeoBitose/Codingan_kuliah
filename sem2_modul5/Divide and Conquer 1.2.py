import os
os.system("cls")

panjang=int(input("Masukkan Panjang Array: "))

A=[]
for i in range(panjang):
    A.append(int(input(f"Masukkan Angka ke {i+1}: ")))

varK =int(input("Masukkan key (k):"))

def DaC(A, k):
    n = len(A)
    if n == 0:
        return 0
    elif n == 1:
        return 1 if A[0] == k else 0
    else:
        bagi = n // 2
        kiri = DaC(A[:bagi], k)
        kanan = DaC(A[bagi:], k)
        return kiri + kanan

print(f"Banyaknya anggota dimensi A yang memiliki nilai sama dengan K adalah: {DaC(A,varK)}")