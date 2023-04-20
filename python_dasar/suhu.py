#=======================================================
cl = True

while cl == True :
    try:
        celcius = int(input('masukkan suhu celcius : '))
        cl = False

    except:
        print("input salah, harus angka\n")
        cl = True

reamur = (4/5)*celcius
farenheit = ((9/5)*celcius)+32        
kelvin = celcius + 273

print(f'\ndalam satuan reamur adalah {reamur}R \ndalam satuan farenheit adalah {farenheit}F \ndalam satuan kelvin adalah {kelvin}K\n')
#=======================================================
