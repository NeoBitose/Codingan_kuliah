angka = int(input("\nmasukkan angka : "))

if angka % 2 == 0 :
    
    if angka >= 0 and angka <= 10 :
        print("bilangan tersebut adalah bilangan genap dan bilangan tersebut termasuk bilangan kecil\n")

    elif angka > 10 and angka <= 50 :
        print("bilangan tersebut adalah bilangan genap dan bilangan tersebut termasuk bilangan sedang\n")

    elif angka >50 :
        print("bilangan tersebut adalah bilangan genap dan bilangan tersebut termasuk bilangan besar\n")

elif angka % 2 == 1 :

    if angka >= 0 and angka <=10 :
        print("bilangan tersebut adalah bilangan gasal dan bilangan tersebut termasuk bilangan kecil\n")

    elif angka > 10 and angka <=50 :
        print("bilangan tersebut adalah bilangan gasal dan bilangan tersebut termasuk bilangan sedang\n")

    elif angka >50 :
        print("bilangan tersebut adalah bilangan gasal dan bilangan tersebut termasuk bilangan besar\n")

else :

    print("salah")

