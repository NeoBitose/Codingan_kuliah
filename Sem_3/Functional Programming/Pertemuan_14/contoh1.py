class Penduduk:
  
  def __init__ (self, nama, umur, kategori_usia = "", memiliki_ktp = "") :
    self.nama = nama
    self.umur = umur
    self.kategori_usia = ""
    self.memiliki_ktp = ""
  
  def tambah_kategori(self, umur):
    if umur >= 0 and umur <= 9 :
      self.kategori_usia = "anak-anak"
    elif umur > 9 and umur <= 17 :
      self.kategori_usia = "remaja"
    elif umur > 17 :
      self.kategori_usia = "dewasa"
    else:
      self.kategori_usia = "tidak terdefinisi"
    return self
  
  def kepemilikan_ktp(self, kategori_usia):
    if kategori_usia == "dewasa" :
      self.memiliki_ktp = "sudah bisa memiliki ktp"
    else:
      self.memiliki_ktp = "belum bisa memiliki ktp"
    return self

penduduk = Penduduk("Alif Ramadhan", 19)

print(f"Sebelum di proses \nNama : {penduduk.nama} \nUmur : {penduduk.umur} \nKategori Usia : {penduduk.kategori_usia} \nStatus KTP : {penduduk.memiliki_ktp}")

setelah_proses = penduduk.tambah_kategori(penduduk.umur).kepemilikan_ktp(penduduk.kategori_usia)

print(f"\nSetelah di proses \nNama : {setelah_proses.nama} \nUmur : {setelah_proses.umur} \nKategori Usia : {setelah_proses.kategori_usia} \nStatus KTP : {setelah_proses.memiliki_ktp}")
