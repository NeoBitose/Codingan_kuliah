angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def rekursiveFilter(arry, genap, a=0) :
  if a == len(arry)-1:
    genap += [arry[a]]
    return genap
  else :
    if arry[a] % 2 == 0 :
      genap += [arry[a]]
    return rekursiveFilter(arry, genap, a+1)

hasil = rekursiveFilter(angka, [])
print(hasil)
