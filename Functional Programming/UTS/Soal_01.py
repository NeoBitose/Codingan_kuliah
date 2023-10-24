def print_increment(arry, a=0) :
  
  if a == len(arry)-1:
    return arry[a]
  else :
    print(arry[a])
    return print_increment(arry, a+1)

array_angka = [1,2,3,4,5,6,7,8,9,10]
print(print_increment(array_angka))