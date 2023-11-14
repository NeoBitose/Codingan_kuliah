# print("\na. Fungsi sorted")
# class Orang:
#     def __init__(self, nama, usia):
#         self.nama = nama
#         self.usia = usia

#     def __lt__(self, other):
#         return self.usia < other.usia

# orang1 = Orang("Alice", 25)
# orang2 = Orang("Bob", 30)
# orang3 = Orang("Charlie", 22)

# orang_terurut = sorted([orang1, orang2, orang3])
# for orang in orang_terurut:
#     print(f"{orang.nama}: {orang.usia} tahun")

# print("\nb. For Biasa")
class Orang:
  def __init__(self, nama, usia):
    self.nama = nama
    self.usia = usia

  def __lt__(self, other):
    return self.usia < other.usia

orang1 = Orang("Alice", 25)
orang2 = Orang("Bob", 30)
orang3 = Orang("Charlie", 22)

list_nilai = [orang1, orang2, orang3]
ulang = 0

while ulang < len(list_nilai) :
  
  indeks_tmp = ulang
  indeks_tukar = ulang
  
  for cek in range(ulang+1, len(list_nilai)):
      if list_nilai[cek] < list_nilai[indeks_tukar]: #pengurutan dari terkecil ke terbesar
        indeks_tukar = cek
          
  (list_nilai[indeks_tmp], list_nilai[indeks_tukar]) = (list_nilai[indeks_tukar], list_nilai[indeks_tmp])
  ulang += 1
  
for i in list_nilai:
  print(f"{i.nama} : {i.usia} tahun")
