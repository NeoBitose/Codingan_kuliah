# Sebagai Variabel

def pertambahan(a,b):
  return a + b

variabel = pertambahan
print(variabel(5,5))

# Sebagai Parameter Function

def pertambahan(a,b):
  return a + b

def perkalian(fungsi):
  return 2 * fungsi(5,5)

print(perkalian(pertambahan))

# Sebagai return
def fungsi_tambah(a):
  def hasil_tambah(b):
    return a + b
  return hasil_tambah

variabel = fungsi_tambah(5)
print(variabel(5))

# Sebagai list dan tabel




