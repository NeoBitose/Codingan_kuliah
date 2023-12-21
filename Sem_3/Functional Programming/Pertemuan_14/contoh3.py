def membuat_domain_website(nama_domain, ekstensi_domain):
  return nama_domain + ekstensi_domain

def merubah_huruf(alamat_website):
  return alamat_website.lower()

def hasil(nama, eks_domain):
  return merubah_huruf(membuat_domain_website(nama, eks_domain))

nama = "UNEJ"
ekstensi_domain = ".ac.id"

print(f"nama domain : {nama} \nekstensi domain website : {ekstensi_domain}")
print(f"website jadi {hasil(nama, ekstensi_domain)}")