class manusia:
    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=umur
        
    def tampilkan(self):
        print(f"{namanya} berumur {umurnya} tahun")
        
namanya=input("Masukan nama = ")
umurnya=int(input("Masukan umur = "))

manusia1=manusia(namanya,umurnya)
manusia1.tampilkan()