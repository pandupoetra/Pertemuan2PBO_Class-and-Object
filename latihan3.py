class persegi:
    def __init__(self,sisi):
        self.sisi=sisi
        
    def luas(self):
        hasil=self.sisi*self.sisi
        return hasil
    def keliling(self):
        hasil=self.sisi*4
        return hasil 
        
sisi_persegi=float(input("Masukan panjang sisi persegi = "))
persegi1=persegi(sisi_persegi)

luas_persegi=persegi1.luas()
keliling_persegi=persegi1.keliling()

print("keliling persegi adalah = ",keliling_persegi," cm")
print("luas persegi adalah = ",luas_persegi," cm")      
   

