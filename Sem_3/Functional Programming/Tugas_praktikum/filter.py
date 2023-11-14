# bilangan kelipatan 2

def kelipatandua(a):
  if a % 2 == 0 :
    return a
  
list_angka = [1,2,3,4,5,6,7,8,9,10]

filter_list = list(filter(kelipatandua, list_angka))
print(filter_list)
