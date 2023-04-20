import time
import os
os.system("cls")

angka = int(input("masukkan angka : "))

def prima(cek,bolean,ulang):
    if bolean == False:
        print(f"bilangan {angka} bukan bilangan prima dengan {ulang}x iterasi")
    else :      
        if cek == angka or cek == 31:
        # if cek == angka :
            if bolean == False :
                print(f"bilangan {angka} bukan bilangan prima dengan {ulang}x iterasi")
            elif bolean == True : 
                print(f"bilangan {angka} adalah bilangan prima dengan {ulang}x iterasi")
        else:
            if angka % cek == 0:
                bolean = False
                prima(cek, bolean,ulang)
            else:
                prima(cek+1,bolean,ulang+1)
 
st = time.perf_counter()        
prima(2,True,1)
nd = time.perf_counter()

print(nd - st)
print(f"Waktu yang dibutuhkan: {nd - st:.7f}")

