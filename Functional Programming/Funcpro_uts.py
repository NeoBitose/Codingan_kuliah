data_kesehatan = []

def create():
  nama_pasien = input("Masukkan nama pasien: ")
  detak_jantung = int(input("Masukkan detak jantung: "))
  kadar_darah = int(input("Masukkan kadar darah: "))
  kadar_gula = int(input("Masukkan kadar gula: "))
  tekanan_darah = int(input("Masukkan tekanan darah: "))
  data = {
    'nama_pasien': nama_pasien,
    'detak_jantung': detak_jantung,
    'kadar_darah': kadar_darah,
    'kadar_gula': kadar_gula,
    'tekanan_darah': tekanan_darah
  }
  data_kesehatan.append(data)
  print("Data kesehatan berhasil ditambahkan.\n")
  print(data_kesehatan)


def read(arry=data_kesehatan, a=0):

  if len(arry) == 0:
    print("data masih kosong")
    return arry
  
  if a == len(arry)-1:
    print(f"\nData ke-{a+1}:")
    print(f"Nama Pasien: {arry[a]['nama_pasien']}")
    print(f"Detak Jantung: {arry[a]['detak_jantung']}")
    print(f"Kadar Darah: {arry[a]['kadar_darah']}")
    print(f"Kadar Gula: {arry[a]['kadar_gula']}")
    print(f"Tekanan Darah: {arry[a]['tekanan_darah']}")
    print("")
    return arry[a]
  else:
    print(f"Data ke-{a}:")
    print(f"Nama Pasien: {arry[a]['nama_pasien']}")
    print(f"Detak Jantung: {arry[a]['detak_jantung']}")
    print(f"Kadar Darah: {arry[a]['kadar_darah']}")
    print(f"Kadar Gula: {arry[a]['kadar_gula']}")
    print(f"Tekanan Darah: {arry[a]['tekanan_darah']}")
    print("")
    return read(arry, a+1)

def update():
    
    if not data_kesehatan:
      print("Tidak ada data untuk diupdate.")
      return

    read()
    nomor_data = int(input("Pilih nomor data yang akan diupdate: "))
    if nomor_data > 0 and nomor_data <= len(data_kesehatan):
      data = data_kesehatan[nomor_data - 1]
      print(f"Data saat ini:")
      print(f"Nama Pasien: {data['nama_pasien']}")
      print(f"Detak Jantung: {data['detak_jantung']}")
      print(f"Kadar Darah: {data['kadar_darah']}")
      print(f"Kadar Gula: {data['kadar_gula']}")
      print(f"Tekanan Darah: {data['tekanan_darah']}")
      print("")

      nama_pasien = input("Masukkan nama pasien: ")
      detak_jantung = int(input("Masukkan detak jantung baru: "))
      kadar_darah = int(input("Masukkan kadar darah baru: "))
      kadar_gula = int(input("Masukkan kadar gula baru: "))
      tekanan_darah = int(input("Masukkan tekanan darah baru: "))

      data['nama_pasien'] = nama_pasien
      data['detak_jantung'] = detak_jantung
      data['kadar_darah'] = kadar_darah
      data['kadar_gula'] = kadar_gula
      data['tekanan_darah'] = tekanan_darah

      print("Data berhasil diupdate.")
    else:
      print("Nomor data tidak valid.")


def delete():
    if not data_kesehatan:
      print("Tidak ada data untuk dihapus.")
      return
    read()
    nomor_data = int(input("Pilih nomor data yang akan dihapus: "))
    if nomor_data > 0 and nomor_data <= len(data_kesehatan):
      del data_kesehatan[nomor_data - 1]
      print("Data berhasil dihapus.")
    else:
      print("Nomor data tidak valid.")


while True:
    print("\n===== Aplikasi Pencatatan Kesehatan =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")

    pilihan = input("Pilih operasi (1/2/3/4/5): ")

    if pilihan == '1':
      create()
    elif pilihan == '2':
      read(data_kesehatan)
    elif pilihan == '3':
      update()
    elif pilihan == '4':
      delete()
    elif pilihan == '5':
      break
    else:
      print("Pilihan tidak ada")