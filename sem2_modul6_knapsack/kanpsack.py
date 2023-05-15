jenis_barang = int(input("masukkan banyaknya jenis barang: "))
nilai = []
berat = []

for i in range(jenis_barang):
    nilai.append(int(input(f"Masukkan harga barang ke {i+1}: ")))
    
for x in range(jenis_barang):
    berat.append(int(input(f"Masukkan berat barang ke {x+1}: ")))

dayatampung = int(input("Masukkan berat maksimal: "))
n = len(nilai)

def knapSack(dayatampung, berat, nilai, n):
    
   if n == 0 or dayatampung == 0 :
      return 0
   if (berat[n-1] > dayatampung):
      return knapSack(dayatampung, berat, nilai, n-1)
   else:
      return max(nilai[n-1] + knapSack(dayatampung-berat[n-1], berat, nilai, n-1), knapSack(dayatampung, berat, nilai, n-1))
      
print(f"harga maksimal yang terdapat di dalam truk adalah {knapSack(dayatampung, berat, nilai, n)}")


