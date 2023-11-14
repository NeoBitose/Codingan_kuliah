# sorting bubblesort

def pindah_nilai(x,y):
    return y, x
  
def cek_nilai(list_angka,a):
  if a == len(list_angka) - 1:
    return list_angka
  if list_angka[a] > list_angka[a+1]:
    list_angka[a], list_angka[a+1] = pindah_nilai(list_angka[a], list_angka[a+1])
  return cek_nilai(list_angka, a+1)
    
def bubble_rekursive(list_angka,b):
  if b == 0:
    return list_angka
  list_angka = cek_nilai(list_angka, 0)
  return bubble_rekursive(list_angka, b-1)
  
def bubble(list_angka):
  if len(list_angka) <= 1:
    return list_angka
  else:
    return bubble_rekursive(list_angka, len(list_angka))

list_angka = [1,4,7,2,5,8,3,6,9]
hasil_sorting = bubble(list_angka)
print(hasil_sorting)
  