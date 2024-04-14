# Pipelining

arry = [1,2,3,4,5,6,7,8,9,10]
hasil = sum([x for x in arry if x % 2 != 0])
print("Total penjumlahan bilangan ganjil pada array :", hasil)


# Vektorisasi

import numpy as np 

arry = np.array([10, 20, 30, 40, 50])
data = 3

hasil = arry * data
print("Hasil akhir array setelah dikali 3 : ", hasil)
