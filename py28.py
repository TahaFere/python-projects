#MİRAS ALMA yani "inheritance" işlemi sayesinden sınıflar arasında belirli bir hiyerarşi kurabiliriz.
    #Taban Sınıf(parent-super class) birkaç farklı sınıfın ortak niteliklerini ve metotlarını barındıran sınıfa verilen isimdir. taban sınıftan 
    #miras alınarak daha alt sınıf oluşturulabilir.
    #Alt sınfı (subClass) bir taban sınıftan miras alınarak oluşturulmuş sınıfa verilen isimdir. Taban sınıftana türerildiği için, taban sınıfın 
    #niteliklerine ve metotlarına sahibtir.
def yirmisekiz():
        class insan:
            def __init__(self,isim,soyisim,okul,yas):
                self.isim=isim
                self.soyisim=soyisim
                self.okul=okul
                self.yas=yas
            def bilgileriYazdır(self):
                print("isim:",self.isim)
                print("soyisim:",self.soyisim)
                print("okul:",self.okul)
                print("yaş:",self.yas)

        class Ogretmen(insan):
            def __init__(self,isim,soyisim,okul,yas,bolum):
            #    self.isim=isim
            #    self.soyisim=soyisim
            #    self.okul=okul
            #    self.yas=yas
                super().__init__(isim,soyisim,okul,yas)
                self.bolum=bolum

            def bilgileriYazdır(self):
                print("Öğretmen Bilgileri:")
                #print("isim:",self.isim)
                #print("soyisim:",self.soyisim)
                #print("okul:",self.okul)
                #print("yaş:",self.yas)
                super().bilgileriYazdır()
                print("bölüm:",self.bolum)

        class Ogrenci(insan):
            def __init__(self,isim,soyisim,okul,yas,sinif):
                #self.isim=isim
                #self.soyisim=soyisim
                #self.okul=okul
                #self.yas=yas
                super().__init__(isim,soyisim,okul,yas)
                self.sinif=sinif

            def bilgileriYazdır(self):
                print("Öğrenci Bilgileri:")
                #print("isim:",self.isim)
                #print("soyisim:",self.soyisim)
                #print("okul:",self.okul)
                #print("yaş:",self.yas)
                super().bilgileriYazdır()
                print("sınıf:",self.sinif)



        Ogretmen1=Ogretmen("TAHA","FERE","MSÜ",22,"Bilgisayar Mühendisliği")
        Ogrenci2=Ogrenci("FATMANUR","TİLAVER","MSÜ",21,"2.sınıf")
        Ogretmen1.bilgileriYazdır()
        Ogrenci2.bilgileriYazdır()


        class A:
            def yazdır(self):
                print("A")
            def yazdır2(self):
                print("AA")
        class B:
            def yazdır(self):
                print("B")
            def yazdır3(self):
                print("BB")
        class C(A,B):#ilk önce hangi sınıf yazılırsa o sınıfın metotları öncelikli olur
            def yazdır(self):
                print("C")
        nesne=C()
        nesne.yazdır()
        nesne.yazdır2()
        nesne.yazdır3()


yirmisekiz()
