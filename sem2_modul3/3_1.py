    
import pandas as pd
import os
from tabulate import tabulate

file_kamus = "datakamus.csv"
tabel = ['Bhs Inggris','Bhs Indonesia']

while True:
    dataframe = pd.read_csv(file_kamus)
    df = dataframe.values.tolist()

    def bubble():
        
        if kata_kunci == 1 :
            for x in range(len(df)-1,0,-1):
                for y in range(x):
                    if df[y][0] > df[y+1][0]:
                        (df[y+1], df[y]) = (df[y], df[y+1])
                        
        elif kata_kunci == 2 :
            for x in range(len(df)-1,0,-1):
                for y in range(x):
                    if df[y][1] > df[y+1][1]:
                        (df[y+1], df[y]) = (df[y], df[y+1])
                        
    def selection():
        
        if kata_kunci == 1 :
            ulang = 0
            
            while ulang < len(df) :
                indeks_tmp = ulang
                indeks_tukar = ulang 
                for cek in range(ulang+1, len(df)):  
                    if df[cek][0] < df[indeks_tukar][0]: 
                        indeks_tukar = cek         
                (df[indeks_tmp], df[indeks_tukar]) = (df[indeks_tukar], df[indeks_tmp])
                ulang += 1
                
        elif kata_kunci == 2 :
            ulang = 0
            
            while ulang < len(df) :
                indeks_tmp = ulang
                indeks_tukar = ulang 
                for cek in range(ulang+1, len(df)):  
                    if df[cek][1] < df[indeks_tukar][1]: 
                        indeks_tukar = cek         
                (df[indeks_tmp], df[indeks_tukar]) = (df[indeks_tukar], df[indeks_tmp])
                ulang += 1
        
    def insertion():
        
        if kata_kunci == 1 :
            for ulang in range(len(df)-1) :
                nilai_tmp = df[ulang+1]
                nilai_kata = df[ulang+1][0]
                while ulang >= 0 and nilai_kata < df[ulang][0] :
                    df[ulang+1] = df[ulang]
                    ulang -= 1
                df[ulang+1] = nilai_tmp
                
        elif kata_kunci == 2 :
            for ulang in range(len(df)-1) :
                nilai_tmp = df[ulang+1]
                nilai_kata = df[ulang+1][1]
                while ulang >= 0 and nilai_kata < df[ulang][1] :
                    df[ulang+1] = df[ulang]
                    ulang -= 1
                df[ulang+1] = nilai_tmp
              
    os.system('cls')

    print("=================================")
    print("|   Selamat Datang Di Program   |")
    print("|         Sorting Kamus         |")
    print("=================================\n\n")

    print("Urutan Berdasarkan :")
    print("1. Kata bahasa inggris")
    print("2. Terjemahan Kata bahasa indonesia")
    print("3. Keluar")

    while True :
        kata_kunci = int(input("\nMasukkan pilihan : "))
        if kata_kunci == 1 or kata_kunci == 2:
            break 
        elif kata_kunci == 3:
            print("Terima Kasih")
            exit()            

    print("\nPilihan sorting : ")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Keluar")

    while True:
        
        pilihan = int(input("\nMasukkan pilihan : "))
        
        if pilihan == 1:
            bubble()
            break
        elif pilihan == 2:
            selection()
            break
        elif pilihan == 3:
            insertion()
            break
        elif pilihan == 4:
            exit()
    
    print(tabulate(df,headers=tabel,tablefmt='fancy_grid'))
    
    print("\nApakah anda ingin mengulang kembali ? ")
    lagi = input("(Y/y untuk lanjut) :  ")
    if lagi.lower() != "y": break