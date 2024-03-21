import multiprocessing

name_list = []
num = 0
# Fungsi untuk menambahkan nama ke dalam list
def add_name(num, name, name_list):
    print("proses menambah nama", name," pada index", num, "ditambahkan ke dalam list baru")
    name_list.append(name)

if __name__ == "__main__":
    # Membuat manager untuk mengelola list yang dibagikan antar proses
    manager = multiprocessing.Manager()
    names = manager.list()
    
    # Daftar nama yang ingin ditambahkan
    new_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    
    # Membuat proses untuk setiap nama dan menambahkannya ke dalam list
    processes = []
    for name in new_names:
      
        # Membuat proses baru untuk menambahkan nama
        process = multiprocessing.Process(target=add_name, args=(new_names.index(name), name, names))
        processes.append(process)
        # Memulai proses
        process.start()
    
    # Menunggu semua proses selesai
    for process in processes:
        process.join()

    # Mencetak list nama setelah semua proses selesai
    print("List nama setelah ditambahkan secara paralel:", names)
