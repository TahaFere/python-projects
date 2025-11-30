def bilgileri_yazdir(isim, soyisim, bolum):
    print("İsim:", isim)
    print("Soyisim:", soyisim)
    print("Bölüm:", bolum)

class Ogrenci:
    def __init__(self,isim,soyisim,bolum):
        self.isim=isim
        self.soyisim=soyisim
        self.bolum=bolum
        print("öğrenci oluşturuldu.")

    def bilgileri_yazdir(self):
        print("İsim:", self.isim)
        print("Soyisim:", self.soyisim)
        print("Bölüm:", self.bolum)