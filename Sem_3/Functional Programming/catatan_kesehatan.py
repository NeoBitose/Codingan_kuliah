class Akun():

  def __init__(self, user="admin", password="123"):
    self.user = user
    self.password = password
    self.trial = 0

  def login(self, loginUsr, passUsr):
    if loginUsr == self.user and passUsr == self.password:
      return True
    elif loginUsr != self.user or passUsr != self.password:
      return False

# class CatatanKesehatan():
   
#   def create():
#   def read():
#   def update():
#   def delete():



new_akun = Akun()

while True:
  inp_user = input("Masukkan user anda : ")
  inp_password = input("masukkan password anda : ")

  hasil = new_akun.login(inp_user, inp_password)
  print(new_akun.login(inp_user, inp_password))

  if hasil == True:
    print(f"total trial anda : {new_akun.trial}")
    break
  else:
    new_akun.trial += 1
    print(f"trial : {new_akun.trial}")
