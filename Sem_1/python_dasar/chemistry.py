import random
inputLagi = True

print("=================================")
print("|   Selamat Datang Di Program   |")
print("|  Presentase Chemistry Antara  |")
print("|       Eluwh dan Bliaw         |")
print("=================================")

while inputLagi == True : 

    loopItem = True

    eluwh = input("\nMasukkan Nama Eluwh : ")
    bliaw = input("Masukkan Nama Bliaw : ")

    persenEluwh = random.randint(0, 100)
    persenBliaw = 100 - persenEluwh

    print(f"\nEluwh, {eluwh}, [{persenEluwh}%]")
    print(f"Bliaw, {bliaw}, [{persenBliaw}%]")

    if persenEluwh < persenBliaw :
        print("Wah ternyata eluwhnya ngga peka >_< bliawnya malah peka")

    elif persenEluwh > persenBliaw :
        print("Wah ternyata eluwhnya peka >_< bliawnya gak peka")

    elif persenEluwh == persenBliaw :
        print("Wah ternyata eluwhnya sama bliaw sama effort buat bersatu")
    
    while loopItem == True:
    

        cekItemBaru = input("\nApakah anda ingin input lagi ? [y]/[t] ")

        if cekItemBaru == "y" or cekItemBaru == "Y":

            inputLagi = True
            loopItem = False

        elif cekItemBaru == "t" or cekItemBaru == "T":

            print("Selesai")
            inputLagi = False
            loopItem = False

        else:
            print("input nya salah")
            loopItem = True

