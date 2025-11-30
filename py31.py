def otuzbir():
        class Insan:
            def __init__(self, isim,soyisim):
                self.isim=isim
                self.soyisim=soyisim

            def bilgiYazdir(self):
                print("isim:",self.isim)
                print("soyisim:",self.soyisim)

        class Ogrenci(Insan):
            ogrenciListesi=[]
            def __init__(self,isim,soyisim,ogrenciNo,ogrenciPuan):
                super().__init__(isim,soyisim)
                self.ogrenciNo=ogrenciNo
                self.ogrenciPuan=ogrenciPuan
                self.ogrencigecme=bool()
                self.ogrenciListesi.append(self)


            def bilgiYazdir(self):
                super().bilgiYazdir()
                print("öğrenci no:",self.ogrenciNo)
                print("öğrenci puanı:",self.ogrenciPuan)


        class Ogretmen(Insan):
            def __init__(self,isim,soyisim,departman):
                super().__init__(isim,soyisim)
                self.departman=departman

            def bilgiYazdir(self):
                super().bilgiYazdir()
                print("öğretmen departmanı:",self.departman)

            def ogrencigecmeHesapla(self):
                topPuan=0
                for i in Ogrenci.ogrenciListesi:
                    topPuan+=i.ogrenciPuan
                ortalama=topPuan/len(Ogrenci.ogrenciListesi)
                print("sınıf ortalaması:",ortalama)
                for ogrenci in Ogrenci.ogrenciListesi:
                    if ogrenci.ogrenciPuan>=ortalama:
                        ogrenci.ogrencigecme=True
                    else:
                        ogrenci.ogrencigecme=False

            def ogrenciBilgiYazdir(self):
                Ogretmen.ogrencigecmeHesapla(self)
                for ogrenci in Ogrenci.ogrenciListesi:
                    ogrenci.bilgiYazdir()
                    if ogrenci.ogrencigecme==True:
                        print("durum: geçti")
                    else:
                        print("durum: kaldı")
                    



        ogrenci1=Ogrenci("TAHA","FERE","2021001",85)
        ogrenci2=Ogrenci("FATMANUR","TİLAVER","2021002",95)
        ogrenci3=Ogrenci("AHMET","YILMAZ","2021003",65)
        ogrenci4=Ogrenci("MEHMET","ÖZTÜRK","2021004",75)

        print("-----ÖĞRENCİ BİLGİLERİ-----")
        
        ogrenci1.bilgiYazdir()
        ogrenci2.bilgiYazdir()
        ogrenci3.bilgiYazdir()
        ogrenci4.bilgiYazdir()

        print("-----ÖĞRETMEN BİLGİLERİ-----")

        ogretmen1=Ogretmen("ALİ","VELİ","MATEMATİK")
        ogretmen1.bilgiYazdir()
        ogretmen1.ogrencigecmeHesapla()
        ogretmen1.ogrenciBilgiYazdir()
        

otuzbir()
