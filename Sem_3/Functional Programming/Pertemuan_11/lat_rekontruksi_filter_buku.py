data_buku = [
  {"judul": "Buku 1", "rating": 4.5},
  {"judul": "Buku 2", "rating": 1.2},
  {"judul": "Buku 3", "rating": 3.4},
  {"judul": "Buku 4", "rating": 4.1},
  {"judul": "Buku 5", "rating": 5.6},
  {"judul": "Buku 6", "rating": 6.5},
  {"judul": "Buku 7", "rating": 2.9},
  {"judul": "Buku 8", "rating": 4.7},
  {"judul": "Buku 9", "rating": 3.9},
  {"judul": "Buku 10", "rating": 7.3},
  {"judul": "Buku 11", "rating": 1.6},
  {"judul": "Buku 12", "rating": 3.7},
  {"judul": "Buku 13", "rating": 5.4},
  {"judul": "Buku 14", "rating": 2.4},
  {"judul": "Buku 15", "rating": 4.4} 
]

hasil = list(filter(lambda x: x['rating'] > 4, data_buku))

print("Buku Rating > 4 :")
list(map(lambda y: print(f"Judul: {y['judul']}, Rating: {y['rating']}"), hasil))
