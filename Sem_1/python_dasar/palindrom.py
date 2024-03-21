kata = input("masukkan kata : ")
if kata == kata[::-1]:
  print(f"kata {kata} adalah palindrom karena {kata} sama dengan {kata[::-1]}")
else:
  print(f"kata {kata} adalah bukan palindrom karena {kata} tidak sama dengan {kata[::-1]}")