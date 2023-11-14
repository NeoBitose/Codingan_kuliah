# print("\na. Fungsi sorted")

# kata = ["apel", "mangga", "jeruk", "nanas", "pisang"]
# kata_terurut = sorted(kata)
# print(kata_terurut)

# print("\nb. For Biasa")

list_nilai = ["apel", "mangga", "jeruk", "nanas", "pisang"]
print(list_nilai)
ulang = 0

while ulang < len(list_nilai) :
  
  indeks_tmp = ulang
  indeks_tukar = ulang
  
  for cek in range(ulang+1, len(list_nilai)):
      if list_nilai[cek] < list_nilai[indeks_tukar]: #pengurutan dari terkecil ke terbesar
          indeks_tukar = cek
          
  (list_nilai[indeks_tmp], list_nilai[indeks_tukar]) = (list_nilai[indeks_tukar], list_nilai[indeks_tmp])
  ulang += 1
  
print(list_nilai)