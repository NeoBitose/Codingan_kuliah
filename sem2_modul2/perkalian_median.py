import time
import os
os.system("cls")

bil1 = int(input("Bilangan pertama : "))
bil2 = int(input("Bilangan kedua : "))
hasil = 0
iterasi = 0

st = time.perf_counter()
for i in range(bil1):
    iterasi += 1
    hasil += bil2
nd = time.perf_counter()

print(f"hasilnya adalah {hasil} dengan iterasi {iterasi}x")
print(f"Waktu yang dibutuhkan: {nd - st:.7f}")
    
if bil1 % 2 == 0 :
    median = int(bil1 / 2)
    final_bil2 = hasil / median
    
elif bil1 % 2 == 1 :
    median = int((bil1+1) / 2)
    final_bil2 = hasil / median
    
print(f"\nBilangan pertama : ", int(median))
print(f"Bilangan kedua : ", final_bil2)

hasil = 0
iterasi = 0

st = time.perf_counter()
for i in range(median):
    iterasi += 1
    hasil += final_bil2
nd = time.perf_counter()

print(f"hasilnya adalah {hasil} dengan iterasi {iterasi}x")
print(f"Waktu yang dibutuhkan: {nd - st:.7f}")
