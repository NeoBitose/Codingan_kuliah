import multiprocessing
import time

# Fungsi yang akan dijalankan oleh setiap proses
def fungsi_proses(nama, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("Proses", nama, "di jalankan")

if __name__ == "__main__":
    # Membuat objek proses
    proses1 = multiprocessing.Process(target=fungsi_proses, args=("Proses 1", 1))
    proses2 = multiprocessing.Process(target=fungsi_proses, args=("Proses 2", 2))

    # Memulai proses
    proses1.start()
    proses2.start()

    # Menunggu proses selesai
    proses1.join()
    proses2.join()

    print("Selesai.")