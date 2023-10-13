def print_decrement(arry, a=1) :
  
  if a == len(arry) :
    return arry[0]
  else :
    print(arry[-a])
    return print_decrement(arry, a+1)

array_angka = [1,2,3,4,5,6,7,8,9,10]
print(print_decrement(array_angka))
