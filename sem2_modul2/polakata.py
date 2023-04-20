import os
os.system("cls")

kalimat =input("Masukkan Kalimat : ")
polakata = input("Masukkan Kata : ")

print(f"\n{kalimat}")

def Pola(idx, idkata, ulang):
        
    if kalimat[idx:idkata] == polakata :
        print(str(ulang*' ') + polakata)
        print(f"\nberada di index {idx}, dan melakukan pengulangan sebanyak {ulang+1}x")
    elif ulang == len(kalimat) :
        print("Tidak ditemukan")
    else :
        print(str(ulang*' ') + polakata)
        Pola(idx+1, idkata+1, ulang+1)

Pola(0,len(polakata),0)
