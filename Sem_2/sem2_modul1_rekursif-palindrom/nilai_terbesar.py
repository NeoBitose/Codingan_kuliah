import os

while True :
    os.system("cls")

    total = int(input("\nmasukkan banyak input : "))
    datalist = []

    print("")

    for i in range(total):
        bilangan = int(input(f"masukkan input {i+1} : "))
        datalist.append(bilangan)

    def nilaiBesar(x, max) :
        if x == total:
            print(f"\nBilangan terbesar : {max}")
        else:
            for j in datalist[x:total]:
                if datalist[x] >= j :
                    if datalist[x] > max :
                        max = datalist[x]
                        
            nilaiBesar(x+1, max)

    nilaiBesar(0,0)
    
    print("\nApakah anda ingin mengulang kembali ? ")
    lagi = input("(Y/y untuk lanjut) :  ")
    if lagi.lower() != "y": break
            
        
