karakter_vokal = ["a", "i", "u", "e", "0","A", "I", "U", "E", "O"]

def printvokal(char):
    if char in karakter_vokal:
        print("itu merupakan bilangan vokal\n")
    else:
        print("itu bukan bilangan vokal\n")

vokal = input("\nmasukkkan karakter = ")

printvokal(vokal)

# karakter_vokal = ["a", "i", "u", "e", "o","A", "I", "U", "E", "O"]
# angka = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# vokal = input("\nmasukkkan karakter = ")

# if vokal in karakter_vokal:
#     print("itu merupakan bilangan vokal\n")
    
# elif vokal in angka:
#     print("itu merupakan angka\n")

# else:
#     print("karakter lainnya\n")