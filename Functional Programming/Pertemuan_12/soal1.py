# print("\na. Fungsi sorted")

# angka = [5, 2, 9, 1, 5, 6]
# angka_terurut = sorted(angka)  # Mengurutkan dari terkecil ke terbesar
# print(angka_terurut)

# angka_terurut_terbalik = sorted(angka, reverse=True)  # Mengurutkan dari terbesar ke terkecil
# print(angka_terurut_terbalik)

# print("\nb. For Biasa")

list_nilai = [5, 2, 9, 1, 5, 6]
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

list_nilai = [5, 2, 9, 1, 5, 6]
ulang = 0

while ulang < len(list_nilai) :
  
  indeks_tmp = ulang
  indeks_tukar = ulang
  
  for cek in range(ulang+1, len(list_nilai)):
      if list_nilai[cek] > list_nilai[indeks_tukar]: #pengurutan dari terbesar ke terkecil
          indeks_tukar = cek
          
  (list_nilai[indeks_tmp], list_nilai[indeks_tukar]) = (list_nilai[indeks_tukar], list_nilai[indeks_tmp])
  ulang += 1
  
print(list_nilai)



