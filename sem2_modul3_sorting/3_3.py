def merge(datalist):
    
    if len(datalist) > 1 :
        
        # Memecah
        tengah = len(datalist) // 2
        bagian_kiri = datalist[:tengah]
        bagian_kanan = datalist[tengah:]
                
        merge(bagian_kiri)
        merge(bagian_kanan)
        
        # Menggabungkan
        
        i = 0
        j = 0
        k = 0
        
        while i < len(bagian_kiri) and j < len(bagian_kanan):
            if bagian_kiri[i] < bagian_kanan[j]:
                datalist[k] = bagian_kiri[i]
                i+=1
            else:
                datalist[k] = bagian_kanan[j]
                j+=1
            k+=1
        
        while i < len(bagian_kiri):
            datalist[k] = bagian_kiri[i]
            i += 1
            k += 1

        while j < len(bagian_kanan):
            datalist[k] = bagian_kanan[j]
            j += 1
            k += 1
        
    return datalist

datalist = [3, 12, 1, 10, 27, 11, 5, 2, 87, 17, 9]
print(merge(datalist))

