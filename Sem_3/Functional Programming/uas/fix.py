from tabulate import tabulate

# database data pengguna
database_pengguna = [
  {'username': 'user1', 'password': 'pass1'},
  {'username': 'user2', 'password': 'pass2'},
]

# Fungsi untuk mencari pengguna berdasarkan username
def cari_user(username, data_pengguna):
    return next((user for user in data_pengguna if user['username'] == username), None)

# Fungsi untuk memverifikasi kata sandi
def verify_password(user, password):
  if user and user['password'] == password :
    return True
  else:
    return False

# Fungsi login
def login(username, password, data_pengguna):
    user = cari_user(username, data_pengguna)
    if verify_password(user, password):
        return True
    else:
        return False

# Fungsi form login
def form_login(): 
  username_input = input('Masukkan username: ')
  password_input = input('Masukkan password: ')
  result = login(username_input, password_input, database_pengguna)
  if result == True :   
    print("Login Berhasil!\n")
  else:
    print("username atau password salah\n")
    form_login()
    
# form_login()
    
# ============================================================

# Data awal
database_kesehatan = [
  {'id': 1, 'nama_pasien': 'Toni', 'detak_jantung': 80, 'kadar_darah': 15, 'kadar_gula': 180, 'tekanan_darah': 100},
  {'id': 2, 'nama_pasien': 'Budi', 'detak_jantung': 90, 'kadar_darah': 10, 'kadar_gula': 150, 'tekanan_darah': 120}
]

# Fungsi untuk menambahkan data kesehatan (Create)
def tambah(data):
  return database_kesehatan + data

#fungsi untuk menampilkan data kesehatan
def tampil(data):
  print(f"jumlah data : {len(data)}")
  print(tabulate([tuple(d.values()) for d in data], headers=data[0].keys(), tablefmt='grid'))

# Fungsi untuk membaca data kesehatan (Read)
def detail(data, id_data):
    return next((data_kesehatan for data_kesehatan in data if data_kesehatan['id'] == id_data), None)
  
# Fungsi untuk memperbarui data kesehatan (Update)
def edit(data, id_data, data_baru, data_detail):
  return [{**data_detail, **data_baru} if data_detail['id'] == id_data else data_detail for data_detail in data]

# Fungsi untuk menghapus data kesehatan (Delete)
def hapus(data, id_data, data_detail):
    return [data_kesehatan for data_kesehatan in data if data_kesehatan['id'] != id_data]

# Contoh penggunaan fungsi-fungsi CRUD
# new_users = add_user(users, {'id': 3, 'name': 'Alice', 'age': 28})
# print(new_users)

# user_to_update = get_user_by_id(new_users, 1)
# updated_users = update_user(new_users, 1, {'age': 26})
# print(updated_users)

# user_to_delete = get_user_by_id(updated_users, 2)
# users_after_deletion = delete_user(updated_users, 2)
# print(users_after_deletion) 

def form_tambah() : 
  return [{
          'id': len(database_kesehatan)+1, 
          'nama_pasien': input("Masukkan nama pasien: "), 
          'detak_jantung': int(input("Masukkan detak jantung (bpm): ")), 
          'kadar_darah': int(input("Masukkan kadar darah (g/dL): ")), 
          'kadar_gula': int(input("Masukkan kadar gula (mg/dL): ")), 
          'tekanan_darah': int(input("Masukkan tekanan darah (mmHg): "))
          }]

def form_edit() :
  return {
          'nama_pasien': input("Masukkan nama pasien: "), 
          'detak_jantung': int(input("Masukkan detak jantung (bpm): ")), 
          'kadar_darah': int(input("Masukkan kadar darah (g/dL): ")), 
          'kadar_gula': int(input("Masukkan kadar gula (mg/dL): ")), 
          'tekanan_darah': int(input("Masukkan tekanan darah (mmHg): "))
          }
  
def program() :
  print("\n===== Aplikasi Pencatatan Kesehatan =====")
  print("1. Tambah Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Keluar")
  pilihan = input("Pilih operasi (1/2/3/4/5): ")
  if pilihan == '1':
    print()
    tampil(database_kesehatan)
    tampil(tambah(form_tambah()))
    program()
  elif pilihan == '2':
    tampil(database_kesehatan)
    program()
  elif pilihan == '3':
    tampil(database_kesehatan)
    ids = int(input("\nPilih nomor data yang akan di update: "))
    if detail(database_kesehatan, ids) :
      tampil(edit(database_kesehatan, ids, form_edit(), detail(database_kesehatan, ids)))
    else : 
      print("data tidak ada")
    program()
  elif pilihan == '4':
    tampil(database_kesehatan)
    ids = int(input("\nPilih nomor data yang akan di hapus: "))
    if detail(database_kesehatan, ids) :
      tampil(hapus(database_kesehatan, ids, detail(database_kesehatan, ids)))
    else : 
      print("data tidak ada")
    program()
    hapus()
  elif pilihan == '5':
    print("Terima Kasih")
  else:
    print("Pilihan tidak ada")
    program()

program()


