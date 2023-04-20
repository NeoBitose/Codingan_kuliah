import os

while True :
    os.system("cls")

    total = int(input("\nmasukkan banyak input : "))
    datalist = []
    print("")

    for i  in range(total):
        datalist.append(input(f"masukkan input {i+1} : "))

    def palindrom(index1, index2):
        if index2 == total :
            print("List Merupakan Palindrom")
        else : 
            if datalist[index1] == datalist[-index2] :
                palindrom(index1+1, index2+1)
            else : 
                print("List Bukan Palindrom")

    print("")
    palindrom(0, 1)
    print("\nApakah anda ingin mengulang kembali ? ")
    lagi = input("(Y/y untuk lanjut) :  ")
    if lagi.lower() != "y": break
    
        