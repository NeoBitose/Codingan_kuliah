import threading
import time

str1 = "" 
str2 = ""

# Fungsi yang akan dijalankan oleh setiap thread
def fungsi_thread(nama, delay):
    count = 0
    global str1
    global str2 
    while count < 5:
        time.sleep(delay)
        count += 1
        if(nama == "Thread 1"):
          str1 += "*"
          str2 += "-"
        if(nama == "Thread 2"):
          str1 += "-"
          str2 += "*"
        print("Thread", nama, "di jalankan")
        

# Membuat objek thread
thread1 = threading.Thread(target=fungsi_thread, args=("Thread 1", 1))
thread2 = threading.Thread(target=fungsi_thread, args=("Thread 2", 2))

# Memulai thread
thread1.start()
thread2.start()

# Menunggu thread selesai
thread1.join()
thread2.join()

print(str1)
print(str2)
print("Selesai.")