def mencari_sisi(keliling):
  sisi = keliling/4
  return sisi

def mencari_luas(sisi):
  luas = sisi*sisi
  return luas

keliling_persegi = 48
print(f"sebuah persegi memiliki keliling : {keliling_persegi}")
print(f"diketahui dia memiliki luas sebesar : {int(mencari_luas(mencari_sisi(keliling_persegi)))}")