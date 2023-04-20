import os
os.system("cls")

database = ["faris islam","aril noah","moh aril","alif ramadhan","andhika", "alifia", "alfin andhika", "aril mukminin", "vivin"]
kata_kunci = input("Data yang ingin dicari : ")
result = []

def Pola(idx, idkata, ulang, kalimat):
        
    if kalimat[idx:idkata] == kata_kunci :
        return True
    elif ulang == len(kalimat) :
        return False
    else :
        return Pola(idx+1, idkata+1, ulang+1, kalimat)
    
def linearSearch(data, listdata) :
    
    for i in range(len(listdata)):
        hasil = Pola(0,len(data),0,str(listdata[i]))
        if hasil == True:
            result.append(str(listdata[i]))

linearSearch(kata_kunci, database)

if len(result) > 0:
    print(f"Sekitar {len(result)} hasil ditemukan, {result}")
else:
    print("Data yang anda cari tidak ditemukan!, coba kata kunci lain")