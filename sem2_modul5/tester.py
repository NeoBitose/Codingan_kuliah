import os
os.system('cls')

def cariSelisihTerbesar(A):
    n = len(A)
    if n <= 1:
        return 0
    elif n == 2:
        return abs(A[0] - A[1]), A[0], A[1]
    else:
        mid = n // 2
        selisih_kiri = cariSelisihTerbesar(A[:mid])
        selisih_kanan = cariSelisihTerbesar(A[mid:])
        selisih_tengah = abs(A[mid-1] - A[mid])

        return max(selisih_kiri, selisih_kanan, selisih_tengah)

A = [1,2,4,8,113]
hasil = cariSelisihTerbesar(A)
print(hasil)

