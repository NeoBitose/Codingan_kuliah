
import os
os.system('cls')

def interpolasi_search(listdata, cari) :
    
    awal = 0
    akhir = len(listdata)-1
    
    while awal <= akhir and cari >= listdata[awal] and cari <= listdata[akhir] :
        
        hasil = awal + ((cari - listdata[awal]) * (akhir - awal)) // (listdata[akhir] - listdata[awal])
        
        if listdata[hasil] == cari:
            print(f"Posisinya ada di index : {hasil}")
            
        if listdata[hasil] < cari:
            awal = hasil + 1
        else :
            akhir = hasil - 1 
            
    return -1

datalist = [1,2,3,4,5,6,7,8,9,10,11]

print(f"List data : {datalist}")

cari = int(input("\nMasukkan yang ingin di cari : "))
interpolasi_search(datalist, cari)
    
    