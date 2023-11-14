// perkalian setiap elemen

void main() {
  List<int> listAngka = [1, 2, 3, 4, 5];
  int hasil = listAngka.reduce((a, b) => a * b);
  print(hasil);
}