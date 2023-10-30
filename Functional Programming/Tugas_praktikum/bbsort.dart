// sorting bubblesort

List<int> pindahNilai(int x, int y){
  return [y,x];
}

List<int> cekNilai(List<int> listAngka, int a){
  if(a == listAngka.length - 1){
    return listAngka;
  }
  if (listAngka[a] > listAngka[a+1]){
    listAngka.setAll(a, pindahNilai(listAngka[a], listAngka[a+1]));
  }
  return cekNilai(listAngka, a+1);
}

List<int> bubbleRekursive(List<int> listAngka, int b){
  if(b == 0){
    return listAngka;
  }
  listAngka = cekNilai(listAngka, 0);
  return bubbleRekursive(listAngka, b-1);
} 

List<int> bubble(listAngka){
  if (listAngka.length <= 1){
    return listAngka;
  }
  else{
    return bubbleRekursive(listAngka, listAngka.length);
  }
}

void main(){
  List<int> listAngka = [1,4,7,2,5,8,3,6,9];
  List<int> hasilSorting = bubble(listAngka);
  print(hasilSorting);
}

