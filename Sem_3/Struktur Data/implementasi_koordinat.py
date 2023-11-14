import math

class Koordinat : 
  
  def __init__ (self,x,y):
      self.x = x
      self.y = y

  def geserhz (self,dx,arah):
    if arah == "kiri":
      self.x -= dx
    elif arah == "kanan":
      self.x += dx
      
  def geservc(self,dy,arah):
    if arah == "atas":
      self.y += dy
    elif arah == "bawah":
      self.y -= dy
  
  def hitungjarak(self,a) :
    hasil = (abs(a.x - self.x) ** 2) + (abs(a.y - self.y) ** 2)
    akar = int(math.sqrt(hasil))
    return akar
    
  def getx(self):
    return self.x

  def gety(self):
    return self.y

t1 = Koordinat(2,3)
print(f"Titik t1 memiliki x {t1.getx()} dan y {t1.gety()}")

t2 = Koordinat(4,5)
print(f"Titik t2 memiliki x {t2.getx()} dan y {t2.gety()}")

t1.geserhz(3, "kiri")
print(f"Titik t1 digeser ke kiri sebanyak 3 sekarang x nya {t1.getx()}")

t1.geservc(7, "bawah")
print(f"Titik t1 digeser ke bawah sebanyak 7 sekarang y nya {t1.gety()}")

print(f"Titik t1 di koordinat ({t1.getx()}, {t1.gety()})")

t2.geserhz(15, "kanan")
print(f"Titik t2 digeser ke kanan sebanyak 15 sekarang x nya {t2.getx()}")

t2.geservc(9, "atas")
print(f"Titik t2 digeser ke atas sebanyak 9 sekarang y nya {t2.gety()}")

print(f"Titik t2 di koordinat ({t2.getx()}, {t2.gety()})")

print(f"Titik t1 ({t1.getx()}, {t1.gety()}) dan titik t2 ({t2.getx()}, {t2.gety()}) memiliki jarak {t1.hitungjarak(t2)}")


