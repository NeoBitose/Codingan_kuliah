class papanskor :
  
  def __init__(self):
    self.skor1 = 0
    self.skor2 = 0
    self.tim1 = "Garuda"
    self.tim2 = "Elang"

  def reset(self):
    self.skor1 = 0
    self.skor2 = 0
  
  def up1(self):
    self.skor1 += 1
    
  def up2(self):
    self.skor2 += 1
  
  def down1(self):
    if self.skor1 <= 0 :
      print("skor tidak bisa dikurangi")
    else:
      self.skor1 -= 1
  
  def down2(self):
    if self.skor2 <= 0 :
      print("skor tidak bisa dikurangi")
    else:
      self.skor2 -= 1
  
  def peek1(self):
    return self.skor1
  
  def peek1(self):
    return self.skor2
  
# ========
  
objek = papanskor()

print(f"Pertandingan {objek.tim1} vs {objek.tim2}")

print("Di menit ke 10 tim garuda menyarangkan gol")
objek.up1()
print(f"skor {objek.tim1} {objek.skor1} : {objek.skor2} {objek.tim2}")

print("Di menit 40 tim elang menyarangkan gol")
objek.up2()
print(f"skor {objek.tim1} {objek.skor1} : {objek.skor2} {objek.tim2}")

print("Di menit 70 tim elang menyarangkan gol")
objek.up2()
print(f"skor {objek.tim1} {objek.skor1} : {objek.skor2} {objek.tim2}")

print("Gol di menit 70 dianulir wasit")
objek.down2()
print(f"skor {objek.tim1} {objek.skor1} : {objek.skor2} {objek.tim2}")

print("Di menit 87 tim garuda menyarangkan gol")
objek.up1()
print(f"skor {objek.tim1} {objek.skor1} : {objek.skor2} {objek.tim2}")


