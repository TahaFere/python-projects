def kırksekiz():
        import sqlite3
        b=int(input("1.öğrenci not verileri(basit) \n " \
        "2.öğenci not verileri (class filan katma)\n" \
        "3.otel rezervasyon sisttemi(bir yerde hata var çıktı alınmıyor daha sonra bakıcam\n" \
        "4.otel rezervasyonu sistemi ders cevabı\n" \
        "veritabanı ile ilgili uygulama çalışması çalıştırmak istediğiniz numarayı giriniz: "))
        if(b==1):
            def bir():
                #ÖĞRENCİ NOT SİSTEMİ
                #1.öğrenci ekleme
                #2.öğrenci silme
                #3.öğrenci listeleme
                #4.öğrenci notu güncelleme
                #5.öğrencileri notlarına gore filtreleme
                veritabani=sqlite3.connect("ogrenciNot.db")
                imlec=veritabani.cursor()
                print("VERİTABANI OLUŞTURULDU")
                print("------------------")

                sorgu="CREATE TABLE IF NOT EXISTS OgrenciNot(ogrenciAdi TEXT,ogrenciSoyadi TEXT,ogrenciNo INTEGER,ogrenciNot INTEGER)"
                imlec.execute(sorgu)
                print("VERİTABANIN TABLOSU OLUŞTURULDU")
                print("------------------")

                #1.soru cevap
                print("VERİ EKLEME BAŞLATILDI...")
                sorgu1="INSERT INTO OgrenciNot(ogrenciAdi,ogrenciSoyadi,ogrenciNo,ogrenciNot) VALUES(?,?,?,?)"
                ogreniciBilgi=("taha","fere",1,80)
                ogreniciBilgi1=("fatmanur","tilaver",2,100)
                ogreniciBilgi2=("ahmet","toprak",3,80)
                ogreniciBilgi3=("ekrem","sever",4,60)
                ogreniciBilgi4=("cevahir","sözüer",5,45)
                ogreniciBilgi5=("yasin","fere",6,95)
                ogreniciBilgi6=("esra","fere",7,85)
                imlec.execute(sorgu1,ogreniciBilgi)
                imlec.execute(sorgu1,ogreniciBilgi1)
                imlec.execute(sorgu1,ogreniciBilgi2)
                imlec.execute(sorgu1,ogreniciBilgi3)
                imlec.execute(sorgu1,ogreniciBilgi4)
                imlec.execute(sorgu1,ogreniciBilgi5)
                imlec.execute(sorgu1,ogreniciBilgi6)
                veritabani.commit()
                print("VERİ EKLEME BİTTİ.")
                print("------------------")

                #3.sorunun cevabı
                print("VERİLER LİSTELENİYOR...")
                sorgu3="SELECT * FROM OgrenciNot "
                imlec.execute(sorgu3)
                print(imlec.fetchall())
                print("VERİLER LİSTELENDİ.")
                print("------------------")

                #2.soru cevap
                print("VERİ SİLME BAŞLATILIYOR...")
                sorgu2="DELETE FROM OgrenciNot where ogrenciNot=3"
                imlec.execute(sorgu2)
                veritabani.commit()
                print("VERİ SATIRI SİLİNDİ.")
                print("------------------")
                print("VERİLER LİSTELENİYOR...")
                imlec.execute(sorgu3)
                print(imlec.fetchall())
                print("VERİLER LİSTELENDİ.")
                print("------------------")

                #4.sorunun cevabı
                print("VERİ GÜNCELLEME BAŞLATILIYOR...")
                sorgu4="UPDATE OgrenciNot SET ogrenciNot=60 WHERE ogrenciNo=5"
                imlec.execute(sorgu4)
                veritabani.commit()
                print("VERİLER GÜNCELLENDİ.")
                print("------------------")
                print("VERİLER LİSTELENİYOR...")
                imlec.execute(sorgu3)
                print(imlec.fetchall())
                print("VERİLER LİSTELENDİ.")
                print("------------------")

                #5.sorunun cevabı
                sorgu5="SELECT * FROM OgrenciNot WHERE ogrenciNot=80"
                imlec.execute(sorgu5)
                print("notu 80 olanların issimleri listelenmiştir")
                for ogrenci in imlec:
                    print(ogrenci[0])
                print("------------------")
                sorgu6="SELECT * FROM OgrenciNot ORDER BY ogrenciNot DESC"
                print("öğrenci puanına göre büyükten küçüğe doğru listelenmiştir")
                imlec.execute(sorgu6)
                print(imlec.fetchall())


                kill="DELETE FROM OgrenciNot"
                imlec.execute(kill)
                veritabani.commit()
            bir()

        if(b==2):
            def iki():
                class Ogrenci:
                    ogrencilistesi=[]
                    def __init__(self,isim,soyisim,no,puan):
                        self.isim=isim
                        self.soyisim=soyisim
                        self.ogrenciNo=no
                        self.puan=puan

                    @classmethod
                    def ogrenciEkle(cls,isim,soyisim,ogrenciNo,puan):
                        yeniogrenci=Ogrenci(isim,soyisim,ogrenciNo,puan)
                        cls.ogrencilistesi.append(yeniogrenci)

                    @classmethod
                    def ListeyiYazdir(cls):
                        for ogrenci in cls.ogrencilistesi:
                            print("Ogrenci Adi:{}, Ogrenci Soyadi:{}, Ogrenci No:{}, Ogrenci Puanı:{}".format(ogrenci.isim,ogrenci.soyisim,ogrenci.ogrenciNo,ogrenci.puan))

                class VeriTabanıBağlantısı:
                    def __init__(self,veriTabaniIsim,tabloIsim):
                        self.veritabani=sqlite3.connect(veriTabaniIsim)
                        self.imlec=self.veritabani.cursor()
                        self.tablo=tabloIsim
                        self.imlec.execute("CREATE TABLE IF NOT EXISTS {}(ogrenciAdi nvarchar(20),ogrenciSoyadi nvarchar(20),ogrenciNo INTEGER PRIMARY KEY AUTOINCREMENT ,ogrenciNot INTEGER )".format(self.tablo))

                    def ogrencileriGetir(self):
                        sorgu="SELECT * FROM {}".format(self.tablo)
                        self.imlec.execute(sorgu)
                        Ogrenci.ogrencilistesi.clear()
                        for ogrenci in self.imlec:
                            Ogrenci.ogrenciEkle(ogrenci[0],ogrenci[1],ogrenci[2],ogrenci[3])

                    def ogrenciEkle(self,isim,soyisim,puan):
                        sorgu="INSERT INTO {}(ogrenciAdi,ogrenciSoyadi,ogrenciNot) VALUES(?,?,?)".format(self.tablo)
                        self.imlec.execute(sorgu,(isim,soyisim,puan))
                        self.veritabani.commit()
                        self.ogrencileriGetir()

                    def ogrenciSil(self,ogrenciNo):
                        sorgu="DELETE FROM {} WHERE ogrenciNo={}".format(self.tablo,ogrenciNo)
                        self.imlec.execute(sorgu)
                        self.veritabani.commit()
                        self.ogrencileriGetir()

                    def ogrenciGüncelle(self,ogrenciNo,yeniNot):
                        sorgu="UPDATE {} SET OgrenciNot={} WHERE ogrenciNo={}".format(self.tablo,yeniNot,ogrenciNo)
                        self.imlec.execute(sorgu)
                        self.veritabani.commit()
                        self.ogrencileriGetir()

                    def ogrenciFiltrele(self,notAlt,notUst):
                        sorgu="SELECT * FROM {} WHERE ogrenciNot>={} and ogrenciNot<={}".format(self.tablo,notAlt,notUst)
                        self.imlec.execute(sorgu)
                        for ogrenci in self.imlec:
                            print("Ogrenci Adi:{}, Ogrenci Soyadi:{}, Ogrenci No:{}, Ogrenci Puanı:{}".format(ogrenci[0],ogrenci[1],ogrenci[2],ogrenci[3]))

                    def baglantiyiKes(self):
                        self.veritabani.close()

                veritabani=VeriTabanıBağlantısı("OgrenciNotSistemi.db","Ogrenci")
                #veritabani.ogrenciEkle("taha","fere",90)
                #veritabani.ogrenciEkle("fatmanur","tilaver",100)
                #veritabani.ogrenciEkle("yasin","fere",70)
                #veritabani.ogrenciEkle("ahmet","fere",45)

                veritabani.ogrencileriGetir()
                Ogrenci.ListeyiYazdir()
                veritabani.ogrenciSil(4)
                veritabani.ogrenciGüncelle(8,100)
                veritabani.ogrencileriGetir()
                Ogrenci.ListeyiYazdir()
                print("---------------")
                veritabani.ogrenciFiltrele(45,80)
            iki()

        if(b==3):
            def uc():
                #1.oda Bilgisi yazdırma
                #2.oda filtreleme
                #3.oda ekleme
                #4.oda  rezerve etme
                #5.oda çıkış işlemi
                class Odalar:
                    odalistesi=[]
                    def __init__(self,odaNo,kisiSay,musaitlik):
                        self.odaNo=odaNo
                        self.kisiSay=kisiSay
                        self.musaitlik=musaitlik
                        self.odalistesi.append(self)

                    @classmethod
                    def odaEkle(cls,odaNo,kisiSay,musaitlik):
                        yeniOda=Odalar(odaNo,kisiSay,musaitlik)

                    @classmethod
                    def listeyiYazdır(cls):
                        for oda in cls.odalistesi:
                            print("Oda No={}, Kişi Sayısı={}, Müsaitlik Durumu={}".format(oda.odaNo,oda.kisiSay,oda.musaitlik))

                class VeriTabanıBağlantısı:
                    def __init__(self,VeriTabanıIsim,TabloIsmi):
                        self.veritabani=sqlite3.connect(VeriTabanıIsim)
                        self.imlec=self.veritabani.cursor()
                        self.tablo=TabloIsmi
                        self.imlec.execute("CREATE TABLE IF NOT EXISTS {}(OdaNo INTEGER PRIMARY KEY AUTOINCREMENT, KisiSayısı INTEGER, Musaitlik nvarchar(20) )".format(self.tablo))
                        print("VERİTABANI VE TABLO OLUŞTURULDU")

                    def odalarıgetir(self):
                        sorgu="SELECT * FROM {}".format(self.tablo)
                        self.imlec.execute(sorgu)
                        Odalar.odalistesi.clear()
                        for oda in self.imlec:
                            Odalar.odaEkle(oda[0],oda[1],oda[2])

                    def odaEkle(self,kisiSay,musaitlik):
                        sorgu="INSERT INTO {}(KisiSayısı,Musaitlik) VALUES(?,?)".format(self.tablo)
                        self.imlec.execute(sorgu,(kisiSay,musaitlik))
                        self.veritabani.commit()


                    def odaSil(self,odaNo):
                        sorgu="UPDATE {} SET KisiSayısı=0, Musaitlik=FALSE WHERE OdaNo={}".format(self.tablo,odaNo)
                        self.imlec.execute(sorgu)
                        self.veritabani.commit()
                        self.odalarıgetir()

                    def odaGüncelle(self,odaNo,kisiSay,müsaitlik):
                        sorgu="UPDATE {} SET KisiSayısı={}, Musaitlik={} WHERE OdaNo={}".format(self.tablo,kisiSay,müsaitlik,odaNo)
                        self.imlec.execute(sorgu)
                        self.veritabani.commit()
                        self.odalarıgetir()

                    def odaFiltrele(self,müsaitlik):
                        sorgu="SELECT * FROM {} WHERE Musaitlik=FALSE".format(self.tablo)
                        self.imlec.execute(sorgu)
                        print("BOŞ ODALAR:")
                        for oda in self.imlec:
                            print("{} numaralı oda müsaitlik{}".format(oda[0],oda[2]))

                veritabani=VeriTabanıBağlantısı("OtelSistemi.db","Odalar")
                Odalar.listeyiYazdır()
                veritabani.odalarıgetir()
                print("**")
                #veritabani.odaEkle(2,"evet")
                #veritabani.odaEkle(2,"evet")
                #veritabani.odaEkle(2,"hayır")
                #veritabani.odaEkle(3,"evet")
                #veritabani.odaEkle(3,"hayır")
                #veritabani.odaEkle(4,"evet")
                #veritabani.odaEkle(4,"hayır")
                #veritabani.odaEkle(5,"evet")

                veritabani.odalarıgetir()
            uc()
        if(b==4):
            def dort():
                class Oda:
                    odaListesi=[]
                    def __init__(self,odaNo,kisiSayisi,musaitlik):
                        self.odaNo=odaNo
                        self.kisiSayisi=kisiSayisi
                        self.musaitlik=musaitlik
                        self.odaListesi.append(self)

                    @classmethod
                    def odalariYazdir(cls):
                        print(cls.odaListesi)
                        for oda in cls.odaListesi:
                            print("oda No:{}, Kisi Sayisi:{}, Müsaitlik durumu:{}".format(oda.odaNo,oda.kisiSayisi,oda.musaitlik))
                    
                class veitabanıBaglantisi:
                    def __init__(self,veriTAbanıIsim,tabloIsim):
                        self.veritabani=sqlite3.connect(veriTAbanıIsim)
                        self.tablo=tabloIsim
                        self.imlec=self.veritabani.cursor()
                        self.imlec.execute("CREATE TABLE IF NOT EXISTS {}(odaNO INTEGER PRIMARY KEY AUTOINCREMENT,kisiSayisi INTEGER NOT NULL,odaMusaitlik INTEGER)".format(self.tablo))

                    def odalariGetir(self):
                        sorgu="SELECT * FROM {}".format(self.tablo)
                        self.imlec.execute(sorgu)
                        Oda.odaListesi.clear()
                        for oda in self.imlec:
                            print(oda)
                            yenioda=Oda(oda[0],oda[1],oda[2])
                            

                    def odaEkle(self,kisiSayisi):
                        sorgu="INSERT INTO {}(kisiSayisi,odaMusaitlik) VALUES(?,?)".format(self.tablo)
                        self.imlec.execute(sorgu,(kisiSayisi,1))
                        self.veritabani.commit()
                        self.odalariGetir()
                    
                    def odayiDoldur(self,odaNo):
                        sorgu="SELECT odaMusaitlik FROM {} WHERE odaNO={}".format(self.tablo,odaNo)
                        self.imlec.execute(sorgu)
                        musaitlik=self.imlec.fetchone()[0]
                        if musaitlik==1:
                            sorgu2="UPDATE {} SET odaMusaitlik=0 WHERE odaNo={}".format(self.tablo,odaNo)
                            self.imlec.execute(sorgu2)
                            self.veritabani.commit()
                            self.odalariGetir()
                            print("oda rezerve edildi!")
                        else:
                            print("oda müsait değil")

                    def odayiBosalt(self,odaNo):
                        sorgu="SELECT odaMusaitlik FROM {} WHERE odaNO={}".format(self.tablo,odaNo)
                        self.imlec.execute(sorgu)
                        musaitlik=self.imlec.fetchone()[0]
                        if musaitlik==1:
                            sorgu2="UPDATE {} SET odaMusaitlik=1 WHERE odaNo={}".format(self.tablo,odaNo)
                            self.imlec.execute(sorgu2)
                            self.veritabani.commit()
                            self.odalariGetir()
                            print("oda boşaltıldı")
                        else:
                            print("oda zaten boş durumda")
                    
                    def odaSorgula(self,kisiSayisi):
                        sorgu="SELECT * FROM {} WHERE kisiSayisi={} and odaMusaitlik=1".format(self.tablo,kisiSayisi)
                        self.imlec.execute(sorgu)
                        for oda in self.imlec:
                            print("0da no={}, müsaitlik durumu: Müsait, Kisi sayisi={}".format(oda[0],oda[1]))

                    def bagalntiyiKes(self):
                        self.veritabani.close()

                        


                veritabani=veitabanıBaglantisi("OtelSistemi.db","YeniOdalar")
                
                #veritabani.odaEkle(1)
                #veritabani.odaEkle(2)
                #veritabani.odaEkle(3)
                #veritabani.odaEkle(2)
                #veritabani.odaEkle(3)
                #veritabani.odaEkle(4)
                #veritabani.odaEkle(2)
                #veritabani.odaEkle(1)
                Oda.odalariYazdir()

                veritabani.odayiDoldur(3)
                veritabani.odayiDoldur(5)
                veritabani.odayiDoldur(6)
                Oda.odalariYazdir()
                
                veritabani.odayiBosalt(1)
                veritabani.odayiBosalt(3)
                Oda.odalariYazdir()

                veritabani.odaSorgula(2)

                veritabani.bagalntiyiKes()
            dort()
kırksekiz()
