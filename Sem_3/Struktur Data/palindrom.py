def palindrom(list_angka) :
  if len(list_angka) < 0 :
    return("list kosong")
  elif len(list_angka) < 2:
    return("list palindrom")
  elif list_angka[0] != list_angka[-1] :
    return("list bukan palindrom")
  return palindrom(list_angka[1:-1])
  
list_angka = [1,2,3,4,4,2,1]
print(palindrom(list_angka))