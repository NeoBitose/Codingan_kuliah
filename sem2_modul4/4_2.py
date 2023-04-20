import os
os.system('cls')

def cariSelisih(nilai, selisih):
    for i in range(len(nilai)):
        for j in range(i+1, len(nilai)):
            if abs(nilai[i] - nilai[j]) == selisih:
                print(f"{nilai[i]} - {nilai[j]} = {selisih}")

datalist = [1, 2, 2, 5, 9, 13, 15, 17]

print(f"List data : {datalist}")

selisih = int(input("\nMasukkan nilai selisih yang diinginkan: "))
print("Data selisih : ")

cariSelisih(datalist, selisih)