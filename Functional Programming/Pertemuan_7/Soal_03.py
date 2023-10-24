def print_genap(arry, a=0, genap=[]) :
  
  if a < len(arry):
    if arry[a] % 2 == 0:
      genap.append(arry[a])
    return print_genap(arry, a+1)
  else :
    return genap

array_angka = [1,2,3,4,5,6,7,8,9,10]
print(print_genap(array_angka))