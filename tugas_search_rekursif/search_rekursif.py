import os
os.system("cls")

kalimat = "Lorem ipsum dolor >sit amet consec'tetur adipi\sicing elit. Error, debitis omnis. Eos perspiciatis veritatis, odit quae ipsum duci'mus aliquid, culpa nesciunt quia exerci`tationem #aperiam voluptates. Optio facere nobis porro adi~pisci."
kata = ""
listkata = []

def search_string(indeks):
    if indeks >= len(cari):
        print("Program pencarian selesai\n")
    else:
        for i in range(len(listkata)):
            if cari[indeks] == listkata[i]:
                print(f"Pencarian kata {cari[indeks]} ditemukan di urutan {i+1} pada kalimat")
                break
            elif i == len(listkata) - 1 and cari[indeks] != listkata[i]:
                print(f"Pencarian kata {cari[indeks]} tidak ditemukan pada kalimat")      
        search_string(indeks+1)
            

for i in range(len(kalimat)):
    if  (65 <= ord(kalimat[i]) <= 90) or (97 <= ord(kalimat[i]) <= 122) or (ord(kalimat[i]) == 39) or (ord(kalimat[i]) == 32):
        if ord(kalimat[i]) == 32:
            listkata.append(kata)
            kata = ""
        else : 
            kata += kalimat[i]

print("Kalimat tersedia :")
print(f"{' '.join(listkata)}\n")
cari = ["omnis", "duci'mus", "adipisci"]
search_string(0)