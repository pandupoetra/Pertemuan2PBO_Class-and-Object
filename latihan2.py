class kucing:
    def __init__ (self,nama,ras,usia):
        self.nama = nama
        self.ras = ras
        self.usia = usia

namanya=input("masukan nama kucing = ")
rasya=input("masukan ras dari kucing = ")
umurnya=float(input("masukan umur kucing (dalam tahun) = "))

kucingA=kucing(namanya,rasya,umurnya)

print("Identitas Kucing")
print("Nama = ",kucingA.nama)
print("Ras  = ",kucingA.ras)
print("usia = ",kucingA.usia)