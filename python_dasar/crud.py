#====================================
list = [1,2,3,4,5,6,7,8,9,0]
#====================================
def tambah(value):
    list.append(int(value))
    print("\n", list)

def edit(index, value):
    list[int(index)] = value
    print("\n", list)

def hapus(index):
    list.pop(int(index))
    print("\n", list)

def getRange(index1, index2):
    print(f'\n{list[int(index1):int(index2)]}')
#====================================
while True:

    print(f'\n{list}')
    print("\n1. tambah\n2. edit\n3. hapus\n4. range list")
    pil = input("\nmasukkan pilihan : ")

    if pil == "1":

        inValue = input("masukkan valuenya: ")
        
        try:
            tambah(inValue)
        except:
            print("ada yang error ges, coba lagi aja.")

    elif pil == "2":

        inIndex = input("masukkan index : ")
        inValue = input("masukkan valuenya: ")

        try:
            edit(inIndex, inValue)
        except:
            print("ada yang error ges, coba lagi aja.")  

    elif pil == "3":

        inIndex = input("masukkan index : ")

        try:
            hapus(inIndex)
        except:
            print("ada yang error ges, coba lagi aja.") 
    
    elif pil == "4":

        firstIndex = input("masukkan index awal : ")
        lastIndex = input("masukkan index akhir: ")

        try:
            getRange(firstIndex, lastIndex)
        except:
            print("ada yang error ges, coba lagi aja.")

    else :
        print("yang gaada gausah dimasukin")
    
#====================================

    while True:

        pilcl = input("\nIngin input lagi ? [y/t] ")

        if pilcl == "y" or pilcl == "Y" or pilcl == "t" or pilcl == "T":
            break

        else:
            print("input nya salah ya")
            
    if pilcl == "t" or pilcl == "T":
            break
            import os
            os.system('CLS')

#====================================
    