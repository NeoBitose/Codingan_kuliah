import os
os.system("cls")

tot_menu = int(input("Total Menu : "))
list_menu = []

for i in range(tot_menu):
    i+=1
    id_menu = int(input(f"\nMasukkan Id Menu {i} : "))
    parent = int(input(f"Masukkan Parent {i} : "))
    label = input(f"Masukkan Label Menu {i} (contoh : menu_{i}) : ")
    list_value = [id_menu, parent, label.replace('_',' ')]
    list_menu.append(list_value)

print("")
def olah(x,y):
    for i in list_menu :
        if int(i[1]) == x :
            print(('...'*y)+i[2])
            olah(int(i[0]),y+1)
olah(0,0)
print("")