def print_increment(arry, a=0, hasil=0) :
  
  if a == len(arry)-1:
    return hasil + arry[a]
  else :
    hasil += arry[a]
    return print_increment(arry, a+1, hasil)

array_angka = [1,2,3,4]
print(print_increment(array_angka))