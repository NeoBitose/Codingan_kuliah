void main(){
  List<int> listAngka = [1,4,7,2,5,8,3,6,9,10];
  List<int> hasil = listAngka.where((listAngka) => listAngka % 2 == 0).toList();
  print(hasil);
}