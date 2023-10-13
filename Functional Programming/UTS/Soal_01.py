def print_increment(arry, a=0) :
  
  if a == len(arry)-1:
    return arry[a]
  else :
    print(arry[a])
    return print_increment(arry, a+1)

array_angka = [1,12,3,14,5,16,7,18,9,10]
print(print_increment(array_angka))