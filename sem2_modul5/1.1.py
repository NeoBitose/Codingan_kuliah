import os # Import library os
os.system("cls") # menggunakan fungsi clear screen untuk membersihkan terminal

def pencarianLinear(listdata, nilai_cari): # membuat fungsi  pencarianlinier() dengan parameter listdata dan nilai_cari
    jumlah_kata = 0 # membuat variabel jumlah_kata untuk menghitung jumlah kata yang sama dengan nilai yang ingin dicari 
    for i in range(len(listdata)): # perulangan for dengan penglangan sebanyak panjang parameter listdata
        if listdata[i] == nilai_cari: # mengkondisikan ketika nilai dari listdata sama dengan nilai yang dicari
            jumlah_kata += 1 # variabel jumlah kata bertambah satu ketika kondisi bersifat true
    return jumlah_kata # mengembalikan varabel jumlah kata

panjang_array = int(input("Masukkan Panjang Array A: ")) # menginputkan panjang array A dan dimasukkan kedalam variabel panjang_array
array_a = [] # membuat list dengan nama array_a

for i in range(panjang_array): # mengulang inputan untuk menambah nilai list array_a sebanyak panjang yang diinginkandi variabel panjang_array
    array_a.append(int(input(f"Masukkan nilai array ke {i+1}: "))) # menbuat inputan untuk menambahkan nilai di list array_a

anggota =int(input("\nMasukkan nilai anggota yang dicari (K):")) # memasukkan nilai yang ingin dicari dan dimasukkan kedalam variabel anggota
print(f"Banyaknya anggota dimensi A yang memiliki nilai sama dengan nilai {anggota} adalah sebanyak {pencarianLinear(array_a,anggota)}") # memenculkan output variabel anggota dan output dari fungsi selisihLinear dengan parameter list array_a dan variabel anggota      