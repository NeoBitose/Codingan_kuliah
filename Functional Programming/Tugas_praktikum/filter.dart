// bilangan kelipatan 2

void main(){
  List<int> listAngka = [1,2,3,4,5,6,7,8,9,10];
  final kelipatanDua = listAngka.where((listAngka) => listAngka % 2 == 0);
  print(kelipatanDua);
}
