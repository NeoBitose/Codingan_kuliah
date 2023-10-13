def reverse_list(arry, hasil = []):
  
  if len(arry) > 0 :
    hasil.append(arry[-1])
    return reverse_list(arry[:-1])
  else :
    return hasil

array_huruf = ['abc', 'def', 'efg']
print(reverse_list(array_huruf))
