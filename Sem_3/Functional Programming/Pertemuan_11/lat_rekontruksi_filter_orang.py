data_orang = [
  {"nama": "Alice", "usia": 28, "jenis_kelamin": "Perempuan"},
  {"nama": "Bob", "usia": 35, "jenis_kelamin": "Laki-laki"},
  {"nama": "Alif", "usia": 17, "jenis_kelamin": "Laki-laki"},
  {"nama": "William", "usia": 27, "jenis_kelamin": "Laki-laki"},
  {"nama": "Kurniawan", "usia": 20, "jenis_kelamin": "Laki-laki"},
  {"nama": "Dandy", "usia": 18, "jenis_kelamin": "Laki-laki"},
  {"nama": "Fitri", "usia": 15, "jenis_kelamin": "Perempuan"},
  {"nama": "Seno", "usia": 32, "jenis_kelamin": "Laki-laki"},
  {"nama": "Ainol", "usia": 45, "jenis_kelamin": "Laki-laki"},
  {"nama": "Putri", "usia": 21, "jenis_kelamin": "Perempuan"},
  {"nama": "Sherly", "usia": 19, "jenis_kelamin": "Perempuan"},
  {"nama": "Nila", "usia": 66, "jenis_kelamin": "Perempuan"},
  {"nama": "Rafi", "usia": 70, "jenis_kelamin": "Laki-laki"},
  {"nama": "Qisa", "usia": 23, "jenis_kelamin": "Perempuan"},
  {"nama": "Ikbar", "usia": 95, "jenis_kelamin": "Laki-laki"},   
]

hasil = list(filter(lambda x: x['usia'] > 25 and x['jenis_kelamin'] == 'Laki-laki', data_orang))

print("Data orang umur > 25 & jenis kelamin = laki laki:")
list(map(lambda y: print(f"Nama: {y['nama']}, Usia: {y['usia']}, Jenis Kelamin: {y['jenis_kelamin']}"), hasil))


