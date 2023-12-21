class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            if len(self.items) <= 2:
                print("batas minimal adalah 2 barang")
            elif len(self.items) > 2 :  
                return self.items.pop(0) 
        else:
            return None
        # if not self.is_empty():
        #     if self.items[0] == "celana" :
        #         self.items.append("celana")
        #         return self.items.pop(0)    
        #     else :
        #         return self.items.pop(0) 
        # else:
        #     return None

    def size(self):
        return len(self.items)


class SistemPengiriman:
    
    def __init__(self):
        self.antrian_pengiriman = Queue()

    def tambah_pengiriman(self, paket):
        self.antrian_pengiriman.enqueue(paket)
        print(f"Paket {paket} telah ditambahkan ke dalam antrian pengiriman.")

    def proses_pengiriman(self):
        if not self.antrian_pengiriman.is_empty():
            paket = self.antrian_pengiriman.dequeue()
            print(f"Paket {paket} sedang dalam proses pengiriman.")
        else:
            print("Antrian pengiriman kosong.")

    def cek_antrian(self):
        if not self.antrian_pengiriman.is_empty():
            print("Antrian pengiriman saat ini:")
            for paket in self.antrian_pengiriman.items:
                print(f"- {paket}")
        else:
            print("Antrian pengiriman kosong.")


sistem_pengiriman = SistemPengiriman()

while True:
    print("\nMenu:")
    print("1. Tambah Pengiriman")
    print("2. Proses Pengiriman")
    print("3. Cek Antrian Pengiriman")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        paket = input("Masukkan nama paket: ")
        sistem_pengiriman.tambah_pengiriman(paket)
    elif pilihan == "2":
        sistem_pengiriman.proses_pengiriman()
    elif pilihan == "3":
        sistem_pengiriman.cek_antrian()
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
