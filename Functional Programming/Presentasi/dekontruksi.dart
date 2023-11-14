List<int> rekursiveFilter(List<int> arry, List<int> genap, int a){
  if(a == arry.length - 1){
    genap += [arry[a]];
    return genap;
  }
  else{
    if(arry[a] % 2 == 0){
      genap += [arry[a]];
    }
  }
  return rekursiveFilter(arry, genap, a+1);
}

void main(){
  List<int> angka = [1,4,7,2,5,8,3,6,9,10];
  List<int> hasil = rekursiveFilter(angka, [], 0);
  print(hasil);
}