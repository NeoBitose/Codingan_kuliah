# perkalian setiap elemen

from functools import reduce

list_angka = [1,2,3,4,5]
hasil = reduce(lambda a,b: a*b, list_angka )
print(hasil)