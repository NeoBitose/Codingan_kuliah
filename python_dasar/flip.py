import random
import time

bold = '\33[1m'
esc = '\33[0m'
italic = '\33[3m'

i=0
skor = 0
koin = ["gambar", "angka"]

print("=================================")
print(f"|   {bold}Selamat Datang Di Program   |")
print(f"|          {bold}Tebak Koin{esc}           |")
print("=================================")
print(">>>   Pil. Gambar dan Angka   <<<")

kesepatanMain = int(input("\nMain berapa kali : "))

while i < kesepatanMain:

    jawaban = random.choice(koin)
    print("\nNgeflip koin...")
    time.sleep(2)

    while True :

        tebakan = input("\nTebak koinnya : ")
            
        if tebakan == jawaban :
            skor += 1 
            print(f"\n>>> Lo betul Skor lu {skor} <<<")
            i += 1
            break

        elif tebakan != jawaban :

            if tebakan != "gambar" and tebakan != "angka":
                print("\nPilihannya hanya gambar dan angka")
            else :
                print(f"\n>>> Lo salah skor lu {skor} <<<")
                i += 1
                break

print("\nPermainan Selesai\n")





