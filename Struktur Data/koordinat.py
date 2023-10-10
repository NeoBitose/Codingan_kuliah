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

# titik_a = Koordinat(3,1)
# print(f"Titik a memiliki x {titik_a.getx()} dan y {titik_a.gety()}")

# # 3.1
# titik_a.geserhz(15, "kanan")
# print(f"Titik a digeser ke kanan sebanyak 15 sekarang x nya {titik_a.getx()}")

# # 3.2
# titik_a.geservc(5, "atas")
# print(f"Titik a digeser ke atas sebanyak 5 sekarang y nya {titik_a.gety()}")

# # 3.3
# titik_b = Koordinat(8,6)
# print(f"Titik b memiliki x {titik_b.getx()} dan y {titik_b.gety()}")
# print(f"Titik a ({titik_a.getx()}, {titik_b.gety()}) dan titik b ({titik_b.getx()}, {titik_b.gety()}) memiliki jarak {titik_a.hitungjarak(titik_b)}")

# # 3.4
# print(f"Titik a memiliki x {titik_a.getx()}")

# # 3.5
# print(f"Titik a memiliki y {titik_a.gety()}")
