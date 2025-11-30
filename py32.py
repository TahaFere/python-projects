def otuziki():
        class bankaSinif:
            def __init__(self,isim,soyisim,bakiye):
                if(self.isimSoyisimKontrol(isim) and self.isimSoyisimKontrol(soyisim)):
                    self.isim=isim
                    self.soyisim=soyisim
                    self.bakiye=bakiye
            
            @staticmethod
            def isimSoyisimKontrol(isimveyasoyisim):
                for karakter in isimveyasoyisim:
                    if not(karakter.isalpha() or karakter.isspace()):
                        return False
                return True

            def profilGörüntüle(self):
                print("isim:",self.isim)
                print("soyisim:",self.soyisim)
                print("bakiye:",self.bakiye)

            def paraYatir(self,miktar):
                if miktar>0:
                    self.bakiye+=miktar
                    print("{} TL para yatırıldı.".format(miktar))
                else:
                    print("Geçersiz miktar!")

            def paraCek(self,miktar):
                if miktar>0:
                    if miktar<=self.bakiye:
                        self.bakiye-=miktar
                        print("{} TL para çekildi.".format(miktar))
                    else:
                        print("Yetersiz bakiye!")
                else:
                    print("Geçersiz miktar!")

            def paraGönder(self,aliciHesap,miktar):
                if miktar>0:
                    if miktar<=self.bakiye:
                        self.bakiye-=miktar
                        aliciHesap.bakiye+=miktar
                        print("{} TL {} adlı hesaba gönderildi.".format(miktar,aliciHesap.isim))
                    else:
                        print("Yetersiz bakiye!")
                else:
                    print("Geçersiz miktar!")

        hesap1=bankaSinif("TAHA","FERE",1000)
        hesap2=bankaSinif("FATMANUR","TİLAVER",500)
        hesap1.profilGörüntüle()
        hesap2.profilGörüntüle()
        hesap1.paraYatir(300)
        hesap1.profilGörüntüle()
        hesap1.paraCek(200)
        hesap1.profilGörüntüle()
        hesap1.paraGönder(hesap2,400)
        hesap1.profilGörüntüle()
        hesap2.profilGörüntüle()

otuziki()
