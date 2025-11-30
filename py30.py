def otuz():
        class Tarih:
            aylaraGoreGünler=[31,29,31,30,31,30,31,31,30,31,30,31]
            ayListesi=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
            def __init__(self,gün,ay,yil):
                self.gün=int(gün)
                self.ay=int(ay)
                self.yil=int(yil)
                if ay>=1 and ay<=12:
                    self.ay=ay
                else:
                    self.ay=1
                if gün>=1 and gün<=self.aylaraGoreGünler[self.ay-1]:
                    self.gün=gün
                else:
                    self.gün=1
                if yil>=1900 and yil<=2025:
                    self.yil=yil
                else:
                    self.yil=1900

            def günArttir(self):
                self.gün+=1
                if self.gün>Tarih.aylaraGoreGünler[self.ay-1]:
                    self.gün=1
                    self.ay+=1
                    if self.ay>12:
                        self.ay=1
                        self.yil+=1
            
            def tarihYazdir(self):
                print("{}/{}/{}".format(self.gün,self.ayListesi[self.ay-1],self.yil))

            def tarihKarsilastir(self,ikinciTarih):
                if self.yil>ikinciTarih.yil or (self.yil==ikinciTarih.yil and self.ay>ikinciTarih.ay) or (self.yil==ikinciTarih.yil and self.ay==ikinciTarih.ay and self.gün>ikinciTarih.gün):
                    print("ilk tarih daha büyüktür.")
                elif self.yil<ikinciTarih.yil or (self.yil==ikinciTarih.yil and self.ay<ikinciTarih.ay) or (self.yil==ikinciTarih.yil and self.ay==ikinciTarih.ay and self.gün<ikinciTarih.gün):
                    print("ikinci tarih daha büyüktür.")
                else:
                    print("tarihler eşittir.")

        tarih1=Tarih(28,2,2024)
        tarih2=Tarih(1,3,2024)

        tarih1.tarihYazdir()
        tarih2.tarihYazdir()
        tarih1.günArttir()
        tarih1.tarihYazdir()
        tarih1.tarihKarsilastir(tarih2)
otuz() 
