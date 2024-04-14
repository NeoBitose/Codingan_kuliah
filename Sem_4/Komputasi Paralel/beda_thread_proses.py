import threading
import multiprocessing
import time

# Fungsi yang akan dijalankan oleh setiap thread atau proses
def task(nama, delay):
    print(nama, "dimulai")
    time.sleep(delay)
    print(nama, "selesai")

def run_multi_threading():
    threads = []
    for i in range(5):
        t = threading.Thread(target=task, args=(f"Thread {i}", i+1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def run_multi_process():
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=task, args=(f"Proses {i}", i+1))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    print("Multi-threading:")
    start = time.time()
    run_multi_threading()
    print("Waktu eksekusi:", time.time() - start, "detik")

    print("\nMulti-process:")
    start = time.time()
    run_multi_process()
    print("Waktu eksekusi:", time.time() - start, "detik")
