#+ toplama,- çıkarma, / bölme, * çarpma, // virgülsüz bölme, 
#% bölümden kalanı bulma, ** üs alma buna ondalıklı sayılar yazılırsa kök almak içinde kullanılır
#b değişkenini int(sayısal) değerden str(metin) türüne değiştirilmi\ş oldu
#mantıksal - boolean (true-false)
#sayılar (tam sayılar küsüratlı sayılar)-int
#karakter dizisi -str
#liste-list
#demetler - tuple
#kümeler set
#sözlükler dictionry
#
#----------IMPORT BÖLÜMÜ-------
import math #matematik kütüphanesini eklemiş olduk
import time # zaman modülünü py dosyasına dahil ettik
import os # işletim sistemi modülünü py dosyasına dahil ettik
import random # rastgele sayı modülünü py dosyasına dahil ettik
import sys # sistem modülünü py dosyasına dahil ettik
from os import name #os modülünden sadece name özelliğini dahil ettik
from bs4 import BeautifulSoup
import requests
import re
import urllib.parse
import urllib.request 
import time
import locale
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as nsn



#
#
#
a=int(input("sayı:"))

if(a==1):
    import py1
    py1.bir()#pythona giriş
elif(a==2):
    import py2 
    py2.iki()#print ile yazım çeşitliliği
elif(a==3):
    import py3 
    py3.uc()#aritmetik operatörler
elif(a==4):
    import py4 
    py4.dort()#kullanıcan veri almak
elif(a==5):
    import py5
    py5.bes()#delta hesaplama
elif (a==6):
       import py6
       py6.altı()#if elseif else yapısı 
if(a==7):
    import py7
    py7.yedi()#döngüler
if(a==8):
    import py8
    py8.sekiz()#faktöriyel hesaplama, basamak hesaplama, asal sayı kont, EBOB-EKOK hesaplama
if(a==9):
    import py9
    py9.dokuz()# üçgen kont, şifre kont, mükenmel sayı kont
if(a==10):
    import py10
    py10.on()#armstrong sayı kont
if(a==11):
    import py11
    py11.onbir()#listeler
if(a==12):
    import py12
    py12.oniki()#demetler
if(a==13):
    import py13
    py13.onuc()#sözlükler
if(a==14):
    import py14
    py14.ondort()#kümeler
if(a==15):
    import py15
    py15.onbes()# fonksiyonlar
if(a==16):
    import py16
    py16.onalti()#matematik modülü
if(a==17):
    import py17
    py17.onyedi()#string kokmutları
if(a==18):
    import py18 
    py18.onsekiz()

if(a==19):
    import py19
    py19.ondokuz()#try except 

if(a==20):
    import py20
    py20.yirmi()#dosya klasör işlemleri
if(a==21):
    #bir dosayadan okuduğumuz tüm harfleri ikinci bir dosayaya büyük harfe çevirerek aktarma yap
    def yirmibir():
        dosya=open("deneme1.txt",mode="r")
        dosya1=open("deneme2.txt",mode="w")
        icerik=dosya.read()
        dosya1.write(icerik.upper())
        #tumsatir=dosya.readlines()
        #for satir in tumsatir:
        #    dosya1.write(satir.upper())
        dosya.close()
        dosya1.close()


    #bir dosyada okuma yaparak dosyadaki kelime sayısını hesaplamasını yap
        dosya=open("deneme1.txt",mode="r")
        kelime=dosya.read()
        kelimelistesi=kelime.split(" ")
        #kelimesay=1
        #for bosluk in kelime:
        #    if bosluk==" ":
        #        kelimesay+=1
        print("deneme1.txt dosaysında {} kelime vardır.".format(len(kelimelistesi)))
        dosya.close()
        dosya1.close()



    #bir dosyada okuduğumuz tüm cümlelerin ilk harfini ikinci bir dosyaya büyük harfe çevirerek at 
        dosya=open("deneme1.txt","r")
        dosya1=open("deneme3.txt","w")
        sozcuk=dosya.read()
        sozcuk1=sozcuk.split(".")
        for cumle in sozcuk1:
            cumle+="."
            dosya1.write(cumle.capitalize())
        dosya1.close()
        dosya.close()


    #okuma yapacağınız dosya içerisinde her öğrencinin adı, soyadı, vize ve final notları bulunacak. Bu dosyadan okuduğumuz bilgilerle ikinci
    #bir dosyaya öğrenci adı, soyadı, harf notu ve dersten geçme-kalma bilgisi yazdıracaksınız. Harf notlarının aralığını kendiniz belirleyebilirsiniz.

        dosya=open("ogrenci.txt","r")
        dosya1=open("ogrenci1.txt","w")
        satir=dosya.readlines()
        geckal=str()
        puan=0
        for i in satir:
            satirici=i.split(" ")
            vize=int(satirici[2])
            final=int(satirici[3])
            puan=(vize*0.4)+(final*0.6)
            if puan<=100 and puan>75:
                harf="a"
            elif puan<75 and puan>55:
                harf="b"
            elif puan<55 and puan>45:
                harf="c"
            elif puan<45 and puan>35:
                harf="d"
            elif puan<35:
                harf="f"    
            if(puan>70):
                geckal="gecti"
            else:
                geckal="kaldi"
            dosya1.write(satirici[0])
            dosya1.write("\t")
            dosya1.write(satirici[1])
            dosya1.write("\t")
            dosya1.write(harf)
            dosya1.write("\t")
            dosya1.write(geckal)
            dosya1.write("\n")




    yirmibir()

if(a==22):
    def yirmiiki():
        #bir dosyada okuduğumuz tüm verileri tersine çevirerek ikinci  bir dosayaya aktarmamız gerekmektedir
        dosya=open("deneme01.txt",mode="r")
        dosya1=open("deneme3.txt",mode="w")
        metin=dosya.read()
        metin=metin[::-1]
        dosya1.write(metin)
        dosya.close()
        dosya1.close()

        #kullanıcın girdiği kelimenin dosya içerisinde olup olmadığını sorgulamız gerekmetedir
        giris=input("Aratmak istediğiniz kelimeyi giriniz:")
        dosyaa=open("deneme01.txt",mode="r")
        metinn=dosyaa.read()
        kelimee=metinn.split(" ")
        sayi=int()
        if giris in kelimee:
            print("Aradığınız kelime dosyada {} kelimesidir".format(int(kelimee.index(giris))+1))
        for sozcuk in kelimee:
            if sozcuk==giris:
                sayi+=1
        print("{} kelimeden metin içinde {} sayıda bulunmaktadır.".format(giris,sayi))
        dosyaa.close()


        #kullanıcıdan alacağınız bir filmin dosyada bulunup bulunmadığını sorgulayın.Eğer ki dosyada bulunuyorsa filmin ismini, çıkış tarihini ve puan 
        #konsola yazdırın aksi halde "aradığınız film listede yoktur!" yazdırın.
        giriss=input("Aramak istediğiniz filmin ismini yazınız:")
        DOSYA=open("filmlist.txt",mode="r")
        metin1=DOSYA.readlines()
        kont=False
        for sozcukk in metin1:
            filmadi,filmyili,filmpuani=sozcukk.split("-")
            if filmadi==giriss:
                print(sozcukk)
                kont=True
                break       
        if kont==False:
            print("Aradığınız film listede yoktur!!!")
        DOSYA.close()
    yirmiiki()

if(a==23):
    def yirmiüc():
        #NESNE TABANLI PROGLAMLAMA
        #-----KAPSÜLLEME
        #bir nesnenin metotlarını ve bilgilerini diğer nesnelerden saklayarak ve bunlara erişimini 
        #sınırlandırarak yanlış kullanımlardan koruyan bir konsepttir.
        #-----MİRAS
        #bir sınıfta başka bir sınıf oluştururken aralarında alt-üst hiyerarşisi oluşturmak ve bu sınıflar arasında ortak yapılar oluşturmak için kullanılır
        #-----ÇOK BİÇİMLİLİK
        #bir metodun bir çok nesne tarafından kullanılması anlamına gelmektedir.
        #-----SOYUTLAMA
        #gereksiz karmaşıklığın gizlenerek oluşturulan nesnelerin sadece gerekli kısımlarını yazılımın diğer kısımlarına sunulması işlemidir.

        #class deneme(): class deneme: buda olabilir. İkiside sınıf tanımlaması

        class ogrenci0():#bunu sınıftan oluşturulacak bütün nesneler aynı bilgileri içericektir bu bir YANLIŞ tanım olur
            adi="TAHA"
            soyadi="FERE"
            dersleri=["matematik","türkçe","fizik"]
        print(ogrenci0.adi)
        print(ogrenci0.soyadi)
        print(ogrenci0.dersleri)

        class ogrenci1():
            adi=""
            soyadi=""
            dersleri=[]
        ogrenci001=ogrenci1()
        ogrenci002=ogrenci1()
        
        ogrenci001.adi="TAHA"
        ogrenci001.soyadi="FERE"
        ogrenci001.dersleri.append("fizik")#burda nesneye eklenen diğer nesneyide etkiledi

        ogrenci002.adi="FATMANUR"
        ogrenci002.soyadi="TİLAVER"

        print("---------------")
        print(ogrenci001.adi)
        print(ogrenci001.soyadi)
        print(ogrenci001.dersleri)
        print("---------------")
        print(ogrenci002.adi)
        print(ogrenci002.soyadi)
        print("---------------")
        print(ogrenci001.dersleri)
        print(ogrenci002.dersleri)


        print("----------------------")

        #--------NESNE NİTELİKLERİ
        #şimdi de her nesnenin kendine ait niteliklerin belirlenmesi

        #----Init(self) fonksiyonu ve Constructor(yapıcı) kavramı
        #Inıt fonksiyonu Pythpn içersinde tanımlanmmış özel bir fonksiyondur, bir sınıftan nesne tanımladığımız zaman gerekli nitelikleri
        #tanımlamak ve yapılacak işlemleri gerçekleştirmek için kullanılır.
        #---UYARI---
        #init metodundan önce bir de new mwtodu çalışır ve sınıfı inşa etmek için kullanılır ancak biz kodlarımızda buna çok fazla yer
        #vermeyeceğiz.
        #---DİKKAT---
        #fonksiyonun ilk parametresi her zaman self olmak zorundadır!!! buradaki self anahtar kelimesi, nesneyi temsil eder gibi düşünebilirsiniz!!

        class Ogrenci:
            #ogrenciAd="" bu sınıf niteliği
            def __init__(self):
                self.ogrenciAd="" #nesnenin niteliği
                print("öğrenci adı:",self.ogrenciAd)
        ogrenci=Ogrenci()
        ogrenci.ogrenciAd="TAHA"
        print(ogrenci.ogrenciAd)
        print("---------------------")
        class Ogrenci2:
            def __init__(self, isim, soyisim, dersler):
                self.ogrenciad = isim
                self.ogrencisoyadi = soyisim
                self.ogrencidersleri = dersler
                print("Öğrenci Adı:", self.ogrenciad)
                print("Öğrenci Soyadı:", self.ogrencisoyadi)
                print("Öğrenci Dersleri:", self.ogrencidersleri)    

        ogrenci1 = Ogrenci2("FATMANUR", "TİLAVER", ["matematik", "fizik"])
        ogrenci2 = Ogrenci2("TAHA", "FERE", ["türkçe", "kimya"])
    yirmiüc()

if(a==24):
    def yirmidort():
        class araba:
            def __init__(self,marka,hizartiş,hizazaliş):
                self.hiz=0
                self.marka=marka
                self.hizartiş=hizartiş
                self.hizazaliş=hizazaliş
            def bilgiYazdir(self):#nesne metodu
                print("araba markası:",self.marka)
                print("araba hızı:",self.hiz)
            def hizart(self):
                self.hiz+=self.hizartiş
            def hizazalt(self):
                self.hiz-=self.hizazaliş
        araba1=araba("BMW",50,30)
        araba2=araba("AUDI",100,40)

        araba1.bilgiYazdir()
        araba2.bilgiYazdir()

        araba1.hizart()
        araba2.hizart()

        araba1.bilgiYazdir()
        araba2.bilgiYazdir()

        araba1.hizazalt()
        araba2.hizazalt()

        araba1.bilgiYazdir()
        araba2.bilgiYazdir()


    yirmidort()


if(a==25):
    def yirmibeş():
        class araba:
            arabalistesi=[]
            def __init__(self,marka,hizartiş,hizazaliş):
                self.hiz=0
                self.marka=marka
                self.hizartiş=hizartiş
                self.hizazaliş=hizazaliş
                self.arabalistesi.append(marka)
            def bilgiYazdir(self):#nesne metodu
                print("araba markası:",self.marka)
                print("araba hızı:",self.hiz)
            def hizart(self):
                self.hiz+=self.hizartiş
            def hizazalt(self):
                self.hiz-=self.hizazaliş
            @classmethod
            def arablariYazdir(cls):
                for araba in cls.arabalistesi:
                    print("araba markası:",araba)

        araba1=araba("BMW",50,30)
        araba2=araba("AUDI",100,40)
        araba3=araba("TOYOTA",80,20)

        araba1.arablariYazdir()
        araba.arablariYazdir()

    yirmibeş()


if(a==26):
    def yirmialtı():
        class Mystring:
            stringlistesi=[]

            def __init__(self,string):
                print(string,"listeye ekleniyor...")
                self.string=string
                self.stringlistesi.append(string)
            
            @classmethod#sınıfın kendisine ait metotlar oluşturmak için kullanılır
            def listeyiyazdır(cls):
                for string in cls.stringlistesi:
                    print(string)
            @staticmethod#sınıfa ait olmayan ama sınıf ile ilgili olan metotlar için kullanılır
            def tersiniyazdır(string):
                print(string[::-1])
        
        string1=Mystring("hava savunma")
        string2=Mystring("astsubay")
        string3=Mystring("astçavuş")

        Mystring.listeyiyazdır()
        Mystring.tersiniyazdır(string2.string)

    
    yirmialtı()


if(a==27):
    #public üyüler: sınıf dışından direkt olarak erişilebildiğimiz nitelikli ve metotlar public üyeler olarak adlandırılır.
    #private üyler: sınıf dışındna direkt olarak erişemediğimiz nitelikli ve metotlar private üyeler olarak adlandırılır.
    #semi-private: sınıf dışından direkt olarak erişebildiğimiz ancak sınıf dışında bu öğeyi değiştirmememiz gereken nitelik ve metotlar 
    #semi-private üyeler olarak adlandırılır.
    def yirmiyedi():
        class orneksinif:
            publicuye="publicüye"
            __privateuye="privateüye"
            _semiprivateuye="semiprivateüye"

        print(orneksinif.publicuye)#public üyelere sınıf dışından erişilebilir
        #print(orneksinif.__privateuye)#private üyelere sınıf dışından erişilemez. bu hata verir
        print(orneksinif._semiprivateuye)#semi-private üyelere sınıf dışından erişilebilir ancak bu önerilmez

        uye=orneksinif()
        print(uye._orneksinif__privateuye)#dolaylı yoldan private üyelere erişilebilir         


    yirmiyedi()


if(a==28):
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

if(a==29):
    def yirmidokuz():
        class complexNumber:
            def __init__(self,gercekKisim=0,sanalKisim=0):
                self.gercekKisim=gercekKisim
                self.sanalKisim=sanalKisim

            def complexToplam(self,complexSayi):
                toplamComplex=complexNumber()
                toplamComplex.gercekKisim=self.gercekKisim+complexSayi.gercekKisim
                toplamComplex.sanalKisim=self.sanalKisim+complexSayi.sanalKisim
                return toplamComplex
        
            def complexCarpim(self,complexSayi):
                carpimComplex=complexNumber()
                carpimComplex.gercekKisim=(self.gercekKisim*complexSayi.gercekKisim)-(self.sanalKisim*complexSayi.sanalKisim)
                carpimComplex.sanalKisim=(self.gercekKisim*complexSayi.sanalKisim)+(self.sanalKisim*complexSayi.gercekKisim)
                return carpimComplex
            
            def sabitCarpim(self,sabit):
                sabitComplex=complexNumber()
                sabitComplex.gercekKisim=self.gercekKisim*sabit
                sabitComplex.sanalKisim=self.sanalKisim*sabit
                return sabitComplex
            
            def negatifeCevir(self):
                negatifComplex=complexNumber()
                negatifComplex.gercekKisim=-1
                negatifComplex.sanalKisim=-1
                return negatifComplex

            def complexCikarma(self,complexSayi):
                complexSayi.negatifeCevir()
                cikarmaComplex=self.complexToplam(complexSayi)
                return cikarmaComplex
            
            def complexYazdir(self):
                if self.sanalKisim>=0:
                    print("{}+{}i".format(self.gercekKisim,self.sanalKisim))
                else:
                    print("{}{}i".format(self.gercekKisim,self.sanalKisim))

        complex1=complexNumber(3,5)
        complex1.complexYazdir()
        complex2=complexNumber(2,-4)
        complex2.complexYazdir()
        complexToplam=complex1.complexToplam(complex2)
        complexToplam.complexYazdir()
        complexCikarma=complex1.complexCikarma(complex2)
        complexCikarma.complexYazdir()
        complexCarpim=complex1.complexCarpim(complex2)
        complexCarpim.complexYazdir()
        sabitCarpim=complex1.sabitCarpim(3)
        sabitCarpim.complexYazdir()
    yirmidokuz()


if(a==30):
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



if(a==31):
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

if(a==32):
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


if(a==33):
    def otuzüc():
        class ucgen:
            def __init__(self,kenar1,kenar2,kenar3):
                while not self.ucgenOlusurMu(kenar1,kenar2,kenar3):
                    kenar1,kenar2,kenar3=input("üçgen oluşturmak için geçerli kenar uzunlukları giriniz:").split(",")
                    self.kenar1=kenar1
                    self.kenar2=kenar2
                    self.kenar3=kenar3
            
            @staticmethod
            def ucgenOlusurMu(kenar1,kenar2,kenar3):
                if(abs(kenar2-kenar3)>=kenar1 or kenar1>=kenar2+kenar3)and(abs(kenar1-kenar3)>=kenar2 or kenar2>=kenar1+kenar3)and(abs(kenar1-kenar2)>=kenar3 or kenar3>=kenar1+kenar2):
                    print("üçgen oluşturulamaz")
                    return False
                else:
                    print("üçgen oluşturulabilir")
                    return True

            def eskenarUcgenMi(self):
                if self.kenar1==self.kenar2 and self.kenar2==self.kenar3:
                    print("eşkenar üçgendir")
                    return True
                else:
                    print("eşkenar üçgen değildir")
                    return False

            def ikizkenarUcgenMi(self):
                if self.kenar1==self.kenar2 or self.kenar2==self.kenar3 or self.kenar1==self.kenar3:
                    print("ikizkenar üçgendir")
                    return True
                else:
                    print("ikizkenar üçgen değildir")
                    return False

            def cesitkenarUcgenMi(self):
                if not self.eskenarUcgenMi() and not self.ikizkenarUcgenMi():
                    print("çeşitkenar üçgendir")
                    return True
                else:
                    print("çeşitkenar üçgen değildir")
                    return False
            #    if self.kenar1!=self.kenar2 and self.kenar2!=self.kenar3 and self.kenar1!=self.kenar3:
            #        print("çeşitkenar üçgendir")
            #        return True
            #    else:
            #        print("çeşitkenar üçgen değildir")
            #        return False
            
            def ucgenTipi(self):
                if self.cesitkenarUcgenMi()==True:
                    print("üçgen çeşitkenar üçgendir")
                elif self.ikizkenarUcgenMi()==True:
                    print("üçgen ikizkenar üçgendir")
                elif self.eskenarUcgenMi()==True:
                    print("üçgen eşkenar üçgendir")
                else:
                    print("üçgen tanımlanamıyor")

            def alanHesaplama(self):
                if self.ucgenOlusurMu()==True:
                    s=(self.kenar1+self.kenar2+self.kenar3)/2
                    alan=(s*(s-self.kenar1)*(s-self.kenar2)*(s-self.kenar3))**0.5
                    print("üçgenin alanı:",alan)
                else:
                    print("üçgen oluşturulamadığı için alan hesaplanamaz")
            
        ucgen1=ucgen(5,5,5)
        ucgen1.ucgenOlusurMu()
        ucgen1.eskenarUcgenMi()
        ucgen1.ikizkenarUcgenMi()
        ucgen1.cesitkenarUcgenMi()
        ucgen1.ucgenTipi()
        ucgen1.alanHesaplama()
        ucgen2=ucgen(5,5,8)
        ucgen2.ucgenOlusurMu()
        ucgen2.eskenarUcgenMi()
        ucgen2.ikizkenarUcgenMi()
        ucgen2.cesitkenarUcgenMi()
        ucgen2.ucgenTipi()
        ucgen2.alanHesaplama()

    otuzüc()

if(a==35):
    def otuzbes():
        b=int(input("35 içinde hangi kodu çalıştırmak istersiniz? (1-2-3):"))
        if(b==1):
            def otuzbesbir():
                #ıterator(yenileyici), sayılabilir sayıda değer içeren bir nesnedir.
                myList=["elma","armut","muz"]
                myIt=iter(myList)

                print(next(myIt))
                print(next(myIt))
                print(next(myIt))

                while True:
                    try:
                        print(next(myIt))
                    except StopIteration:
                        break


                myStr="Python"
                myIt2=iter(myStr)

                print(next(myIt2))
                print(next(myIt2))
                print(next(myIt2))
                print(next(myIt2))
                print(next(myIt2))
                print(next(myIt2))

                while True:
                    try:
                        print(next(myIt2))
                    except StopIteration:
                        break

        if(b==2):
            def otuzbesiki():
                class Sayi:
                    def __iter__(self):
                        self.sayi=0
                        return self
                    
                    def __next__(self):
                        gecici=self.sayi
                        self.sayi+=1
                        return gecici
            
                Sayi=Sayi()
                sayiIt=iter(Sayi)
                print(next(sayiIt))
                print(next(sayiIt))
                print(next(sayiIt))
                print(next(sayiIt))

            otuzbesiki()

        if(b==3):
            def otuzbesüç():
                class Sayi:
                    def __iter__(self):
                        self.sayi=0
                        return self
                    
                    def __next__(self):
                        if self.sayi<=5:
                            gecici=self.sayi
                            self.sayi+=1
                            return gecici
                        else:
                            raise StopIteration
                sayi=Sayi()
                sayiIt=iter(sayi)
                while True:
                    try:
                        print(next(sayiIt))
                    except StopIteration:
                        print("İterasyon tamamlandı.")
                        break 
            otuzbesüç()


    otuzbes()

if(a==36):
    def otuzalti():
        #normal fonksiyonlardan farklı olarka geriye bir iterator dönen fonksiyonlardır.
        #generator fonksiyonlar, return ifadesi yerine kullanılacak en az 1 yield ifadesi içermelidir.
        #iter, next() ve StopIteration yapısını otomatik olarak oluştururlar.
        def deger_arttir():
            sayi=0
            yield sayi#birinci eleman kazandırıldı

            sayi+=1
            yield sayi

            sayi+=1
            yield sayi

        deger_arttir_iter=deger_arttir()
        print(deger_arttir_iter)
        print(next(deger_arttir_iter))
        print(next(deger_arttir_iter))
        print(next(deger_arttir_iter))

        while True:
            try:
                print(next(deger_arttir_iter))
            except :
                print("Generator tamamlandı.")
                break

        def kup_yazdir():
            sayiListesi=[i**3 for i in range(50)]
            for i,j in enumerate(sayiListesi):
                yield "{}^3:{}".format(i,j)
        
        kup_yazdir_Iter=kup_yazdir()
        print(kup_yazdir_Iter)

        for i in kup_yazdir_Iter:
            print(i)


        sayiListesi=[i for i in range(20)]
        print(sayiListesi)

        generator=(i for i in range(20))
        print(generator)#generator objesinin nerde olduğunu gösterir    

        for i in generator:# generator objesinden tek tek elemanlarına ulaşmış olduk.
            print(i)


    otuzalti()

if(a==37):
    def otuzyedi():
        # MODÜLLER
        #pythonda yazdığımız her bir farklı dosya bir modül olarak kabul edilir. modüller içerisinde yazdığımız fonksiyonlar, sınıflar
        # daha sonra başka programlarda veya aynı programın farklı yerinde çağırılabilir ve kullanabiliriz
        #Import ifadesi ile modüller program içerisine dahil edilir.
        #import math # matematik modülünü py dosyasına dahil ettik
        #import time # zaman modülünü py dosyasına dahil ettik
        #import os # işletim sistemi modülünü py dosyasına dahil ettik
        #import random # rastgele sayı modülünü py dosyasına dahil ettik
        #import sys # sistem modülünü py dosyasına dahil ettik

        #from os import name #os modülünden sadece name özelliğini dahil ettik
        name # çıktısı nt olur bu çıktı windows işletim sistemi olduğu için


        #from os import * #os modülündeki tüm özellikleri dahil ettik

        import math as matematik #math modülüne matematik ismini takma isim olarak verdik
        matematik.sqrt(16) #math modülündeki sqrt fonksiyonunu matematik takma ismi ile kullandık
        import os as isletimSistemi #os modülüne isletimSistemi ismini takma isim olarak verdik
        import sys as sistem #sys modülüne sistem ismini takma isim olarak verdik
        

        dir(matematik) #math modülündeki tüm fonksiyon ve özellikleri listeledik
        help(matematik.sqrt) #math modülündeki sqrt fonksiyonunun ne işe yaradığını gösterir
        dir(isletimSistemi) #os modülündeki tüm fonksiyon ve özellikleri listeledik
        dir(sistem) #sys modülündeki tüm fonksiyon ve özellikleri listeledik
        help(matematik)#math modülünün içindeki fonksiyon ve özelliklerin ne işe yaradığını gösterir
        help(isletimSistemi)#os modülünün içindeki fonksiyon ve özelliklerin ne işe yaradığını gösterir
        help(sistem)#sys modülünün içindeki fonksiyon ve özelliklerin ne işe yaradığını gösterir

    otuzyedi()

if(a==38):
    def otuzsekiz():
        b=int(input("38 içinde hangi kodu çalıştırmak istersiniz? (1):"))
        if(b==1):
            import modül_dosya as md#kendi oluşturduğumuz modül dosyasını md takma ismi ile dahil ettik
            md.bilgileri_yazdir("Taha","Fere","bilgisayar mühendisliği")
            ogrenci1=md.Ogrenci("FATMANUR","TİLAVER","bilgisayar mühendisliği")
            ogrenci1.bilgileri_yazdir()
            ogrenci2=md.Ogrenci("TAHA","FERE","makine mühendisliği")
            ogrenci2.bilgileri_yazdir()
        
        if(b==2):
            import os 
            #name niteliği işletim sisteminin adını verir
            #işletim sistemi windows ise 'nt', MacOs ve linux ise 'posix' çıktısını verir
            print("işletim sistemi adı:",os.name)

            #sep niteliği dosya yollarında kullanılan ayırıcı karakteri verir
            #işletim sistemi windows ise '\' , MacOs ve linux ise '/' çıktısını verir
            print("dosya yolu ayırıcı karakter:",os.sep)

            #curdir niteliği geçerli dizini temsil eden karakteri dizisini verir
            #işletim sistemi windows ise '.' , MacOs ve linux ise '.' çıktısını verir
            print("geçerli dizin karakteri:",os.curdir)

            #pardir niteliği geçerli dizinin üst dizini temsil eden karakteri dizisini verir
            #işletim sistemi windows ise '..' , MacOs ve linux ise '..' çıktısını verir
            print("üst dizin karakteri:",os.pardir)

            #getcwd() fonksiyonu geçerli çalışma dizinini verir
            print("geçerli çalışma dizini:",os.getcwd())

            #chdir() fonksiyonu geçerli çalışma dizinini değiştirmeye yarar
            os.chdir("C:\\Users\\user\\Desktop")
            print("bulundumuz dizin:",os.getcwd())
            os.chdir("C:\\Users\\user\\Desktop\\code")

            #listdir() fonksiyonu bir dizi içindeki dosya ve klasörleri liste yapısı halinde sunar.
            print(os.listdir())
            for directory in os.listdir():
                print(directory)

            #startfile() fonksiyonu içerisine verdiğimiz dosya ismine göre dosyayı veya klasörü açmayı sağlar
            os.startfile('filmlist.txt')
            os.startfile('.')
            os.startfile('..')
        
            #mkdir() fonksiyonu içerisinine verdiğimiz dosya yolu ve dosya ismine göre yeni dizini oluşturmayı sağlar
            os.mkdir(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')

            #makedirs() fonksiyonu içerisine verdiğimiz dosya yolu ve dosya ismnine göre iç içe yeni dizini oluşturmayı sağlar
            os.makedirs(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu\\osmodülüoluştu2')

            #rename() fonksiyonu dizinlerin veya dosyaların adlarını değiştirmemizi sağlar
            os.rename("ornek.txt","ornekkk.txt")

            #remove() fonksiyonu dizinleri veya dosyaları silmemizi sağlar
            os.remove("boom.txt")

            #rdir() fonksiyonu içi boş olan bir dizini silmek için kullanılır, içinde dosya varsa hata verir
            os.rmdir(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu\\osmodülüoluştu2')
            os.rmdir(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')

            #removedirs fonksiyonu içi boş olan dizinleri silmek için kullanılır
            os.makedirs(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu\\osmodülüoluştu2')            
            os.removedirs(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')

            #path.abspath() fonksiyonu içerisine verdiğimiz dosyanın tam yolunu verir
            os.path.abspath("deneme1.txt")

            #path.dirname() fonksiyonu içerisine verdiğimiz bir dosya yolunun dizin kısmını verir
            os.path.dirname(os.path.abspath("deneme1.txt"))

            #path.exists fonksiyonu içerisine verdiğimiz dosya veya dizinin olup olmadığını inceler
            os.path.exists(os.path.abspath("deneme1.txt"))
            os.path.exists(os.path.abspath("deneme10.txt"))

            #path.isdir() fonksiyonu içerisine verdiğimiz parametrenin bir dizin olup olmadığını kontrol eder
            os.makedirs(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')
            os.path.isdir('C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')            

            #path.isfile() fonksiyonu içerisine verdiğimiz parametrenin bir dosya olup olmadığını kontrol eder
            os.path.isfile('C:\\Users\\user\\Desktop\\code\\deneme01.txt')

            #path.join() fonksiyonu verilen parametleler ile bir dosya yolu oluşturu
            os.path.join("taha","fatmanur")

            #path.split() fonksiyonu verilen dosya yolunun son kısmını ayırır
            os.path.split('C:\\Users\\user\\Desktop\\code\\deneme01.txt')

            #path.splitext() fonksiyonu verilen dosyanın uzantısı ve ismini birbirinden ayırı
            os.path.splitext('deneme01.txt')

    otuzsekiz()

if(a==39):
    def otuzdokuz():
        #SYS MODÜLÜ
        #import sys
        #kullandığımız Python sürümü ile ilgili bilgi edinmemizi ve kullandığımız Python ile çeşitli işlemler yapabilmemizi sağlar
        
        #argv niteliği program çalışırken kullanılan parametreleri bir liste halinde tutar
        print(sys.argv)

        #executable niteliği pythonın çalıştırabilir dosyanın adını ve yolunu öğrenmek için kullanılır
        print(sys.executable)

        #platform niteliği kodlarımızın çalıştığı işletim sistemi hakkında bilgi almak için kullnılır.
        #GNU/linux :linux çıktısı    windows: win32 çıktısı       mac os: darvin çıktısı
        print(sys.platform)

        #version niteliği python sürümü öğrenmek için kullanılır
        print(sys.version)

        #exit() fonksiyonu program akışını sonlandırmak için kullanılır
        #sys.exit()

        #Standart Komutlar
        #çıktı vermek için ve kullanıcıdan değer almak için aşağıdaki standart komutlar kullanılır.
        #1-Standart çıktı konumu - stdout
        #2-Standart hata konumu - stderr
        #3-standart girdi konumu - stdin
        sys.stderr.write("HATA\n")
        sys.stdout.write("Normal\n")


    otuzdokuz()

if(a==40):
    def kirk():
        #datetime modülü
        #zaman, saat vetarihlerle ilgili işlemler yapabilmemiz için fonksiyon ve nitelikler sunan bazı sınıflardan oluşur
        #dateTime modülü içersinde date, time, datetime sınıfları bulunur
        from datetime import datetime

        #now() Fonksiyonu o an ki tarih, saat ve zaman bilgilerini verir
        suan=datetime.now()
        print(suan)
        print(suan.year)
        print(suan.month)
        print(suan.day)
        print(suan.minute)
        print(suan.second)
        print(suan.microsecond)
        print("--------------------------")
        #today() fonksiyonu içerisinde bulunduğumuz gün ile ilgili bilgileri verir
        bugun=datetime.today()
        print(bugun)
        print(bugun.year)
        print(bugun.month)
        print(bugun.day)
        print(bugun.minute)
        print(bugun.second)
        print(bugun.microsecond)
        print("--------------------------")
        #ctime() fonksiyonu o an ki tarih ve zaman bilgilerinin okunaklı şekilde verir
        ctimesuan=datetime.ctime(suan)
        print(suan)
        print(ctimesuan)
        print("--------------------------")
        #strftime() fonksiyonu
        #tarih ve zaman bilgilendirmemizi sağlar
        #1.yıl bilgisini almak için: %Y
        #2.yıl bilgisinin son 2 hanesini almak için: %y
        #3.ay ismini almak için: %B
        #4.gün ismini almak için: %A
        #5.saat bilgisini almak için: %X
        #6.gün bilgisini almak için: %D
        #7.tarih, saat ve zaman için: %c
        print(datetime.strftime(suan,"%c"))
        print(datetime.strftime(suan,"%Y"))
        print(datetime.strftime(suan,"%y"))
        print(datetime.strftime(suan,"%B"))
        print(datetime.strftime(suan,"%X"))
        print(datetime.strftime(suan,"%D"))
        print("--------------------------")
        
        #locale ile türkçe yapalım
        import locale
        locale.setlocale(locale.LC_ALL,'')
        print(datetime.strftime(suan,"%B"))


        #strptime() fonksiyonu karakter dizisi şeklinde olan tarih bilgisini ayırmamızı sağlar
        suAn="8 kasım 2025 10:13:05"
        datetimesuAn=datetime.strptime(suAn,'%d %B %Y %H:%M:%S')
        print(datetimesuAn)

        #timestamp() fonksiyonu datetime objesini saniye cinsine çevirmek için kullanılır
        saniye=datetime.timestamp(suan)
        print(saniye)

        #fromtimestamp() Fonksiyonu saniye cinsinde olan datetime objeye çevirmek için kullanılıyor.
        suanFTS=datetime.fromtimestamp(saniye)
        print(suanFTS)
        
    kirk()

if(a==41):
    def kirkbir():
        #Time Modülü
        #saat işlemleriyle ilgili faydalı nitelik ve fonksiyonların bulunduğu modüldür
        import time

        #gmtime() fonksiyonu başlangıç zamanın (EPOCH), struct yapısı şeklinde bize verir ve tm_year, tm_mont, tm_day, 
        #tm_sec, tm_wday, tm_yday nitelikleri vardır.
        epoch=time.gmtime(0)
        print(epoch)
        print(epoch.tm_year)

        #time() fonksiyonu başlangıçta(EPOCH) o ana kadar geçen toplam süreyi saniye cinsinden verir.
        print(time.time())

        #localtime() fonksiyonu yerel saat bilgisini, struct yapısı şeklinde bize verir ve m_year, tm_month, tm_day,
        #tm_sec, tm_wday, tm_yday nitelikleri vardır.
        print(time.localtime())

        #sleep() fonkisyonu yazdığıöız kodların belirli bir süre durmasını, uyumasını sağlar.  
        print("birazdan sleep çalışıcak ve program uyucak")
        time.sleep(5)
        print("az önce sleep çalıştı ve uyudum")


    kirkbir()

if(a==42):
    def kirkiki():
        #Random modülü
        #rastgele sayı üretmek için bazı nitelik ve fonksiyonları içerisinde bulunduran modül.
        import random

        #random() fonksiyonu 0 ile 1 arasında rastgele ondalıklı üretmimizi sağlar
        print(random.random())
        print("--")
        #uniform() fonksiyonu kendi belirledyeceğimiz aralıklar arasında rastgele ondalıklı sayı üretmemizi sağlar.
        print(random.uniform(0.5,2.5))
        print("--")
        #randint() fonksiyonu kendi belirleyeceğimz tam sayılar üretmemizi sağlar
        print(random.randint(1,100))
        print("--")
        #randrange() fonksiyonu kendi belirleceğimiz aralıkta sayılar üretmemizi sağlar
        print(random.randrange(50))
        print(random.randrange(25,75))
        print("--")
        #choice() fonksiyonu verdiğimiz bir listeden rastgele eleman seçimlerini sağlar.
        liste=["c","c++","phthon","ruby","java"]
        print(random.choice(liste))
        print(random.choice([i for i in range(35)]))
        print("--")
        #shuffle() fonksiyonu verdiğimiz bir listenin karıştırılmasını sağlar
        liste1=[i for i in range(20)]
        print(liste1)
        random.shuffle(liste1)
        print(liste1)
        print("--")
        #sample() fonksiyonu verdiğimiz bir liste ve eleman sayısına göre rastgele bir alt liste oluşturulmasını sağlar
        print(liste)
        print(liste1)
        print(random.sample(liste,3))
        print(random.sample(liste1,8))

    kirkiki()
        
if(a==43):
    def kirkuc():
        #REQUEST MODÜLÜ HTTP İŞLEMLERİ
        #HTTP(hyper text transfer protocol), verilerin sunucudan kullanıca nasıl aktarılacağını kontrol eden protokoldür. 
        #istek ve yanıt şeklindeçalışır, sunucuya bir istek gönderilir ve o sunucudan olumlu veya olumsuz cevap döner.
        import urllib.request 
        
        #urlopen() fonksiyonu ile site bağlama
        siteUrl="https://httpbin.org"
        html=urllib.request.urlopen(siteUrl)
        print(html)

        #read() fonkisyonu ile sitenin HTML bilgisini alma
        print(html.read())
        print("-----1")
        #HEADER bilgisi gönderme
        #bazı sitelerde bu kadar kolay şekilde bağlanıp bilgi çekeiyoruz, iznimiz olmuyor. Bunun için de User Agent ieçrisnde
        #tanımlı olan işletim sistemi, tarayıcı ve cihaz bilgilerini header bilgisiyle birlikte siteye göndermemiz gerekebiliyor.
        siteURL1="https://eksisozluk.com"
        header_bilgisi={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0  Safari/537.36  OPR/123.0.0.0"}
        istek=urllib.request.Request(siteURL1,headers=header_bilgisi)
        html1=urllib.request.urlopen(istek)
        print(html1.read())
        print("-----2")

        #sitelere veri gönderme işlemleri
        veriler={
            "kullanıcı adi":"tahafr",
            "sifre":"12345",
            "email":"thfr@gmail.com",
            "telefon":"081241340",
            "bolum":"bilgisayar programciligi"
        }

        #urlencode() fonksiyonu ve şifrelenmiş URL oluşturma
        import urllib.parse

        sifreliveriler=urllib.parse.urlencode(veriler)
        print(sifreliveriler)
        #veriler arasına & koyulur, @ karakteri ise %40, boşluk karakteri ise + ile değiştirilir
        print("-----3")
        #Get methodu ile veri gönderme
        sonsiteurl=siteUrl+"/get"+"?"+sifreliveriler
        print(sonsiteurl)
        html2=urllib.request.urlopen(sonsiteurl)
        print(html2.read())
        print("-----4")
        #post metodu ile veri gonderme
        siteUrl=siteUrl+"/post"
        sifreliveriler=sifreliveriler.encode("utf-8")
        print(sifreliveriler)
        istek1=urllib.request.Request(siteUrl,data=sifreliveriler)#burdaki request bayt obje istemesinden dolayı utf-8 şeklinde şifreledik
        html3=urllib.request.urlopen(istek1)
        print(html3.read())
        print("-----5")

        #HTML etikete göre içerik okuma
        siteURL2="https://www.google.com/"
        html4=urllib.request.urlopen(siteURL2)
        icerik=html4.read()
        print(icerik)
        print("--------")
        import re

        etiketTanımı="<title>(.*?)</title>"#ortadaki kısım değişebilir kısımda sabit olan kısımlar title kısımları
        html4=urllib.request.urlopen(siteURL2)# bir yerde açtın diye açıldı diye düşünme urlopen kullan
        icerik1=str(html4.read())
        print(etiketTanımı)
        print(icerik1)
        aramaSonuc=re.search(etiketTanımı,icerik1)
        if aramaSonuc:
            etiket=aramaSonuc.group(0)
            icerik1=aramaSonuc.group(1)

            print("etiket:"+etiket)
            print("içeriğ:"+icerik1)

        print("-----6")
        #tarayıcıdan foto indirme
        gorselUrl="https://st2.depositphotos.com/2627021/7164/i/450/depositphotos_71640033-stock-photo-explosion-nuclear-bomb-in-ocean.jpg"
        urllib.request.urlretrieve(gorselUrl,".\\code.svg")
        print("-----7")
        #QR kod oluşturma
        try:
            boyut=input("lütfen oluşturulacak QR kod boyut bilgisini giriniz")
            veri=input("lütfen oluşturulacak QR kod verisini giriniz")
            veriler={
                "size":boyut+"x"+boyut,
                "data":veri
            }
            veriler=urllib.parse.urlencode(veriler)
            api_url="şuan bu şekilde çalışır web sitesi yoktur ondan çalışmaya devam"+veriler
            dosya_adi=".\\QR_"+veri+".png"
            urllib.request.urlretrieve(api_url,dosya_adi)
            print("indirme başarılı")
        
        except:
            print("hata meydana geldi")


        print("-----8")

    kirkuc()

if(a==44):
    def kırkdort():
    #REQUEST MODÜLÜ
    #kurulum= pip install request
    #request modülüne neden ihtiyacımız var?
    #request modülünün kullanarak web üzerindeki HTTPS isteklerimizi(get,post,put,delete) yönetebileceğiz
        import requests

        b=int(input("bir sayı giriniz:"))
        print(b)
        if(b==1):
            def kirkdortbir():
                #GET modülü ile sayfa içeriğini alma ve parametre gönderme
                #GET modülü ie parametre göndereceğimiz zaman, gönderdiğimiz parametlerel URL yapısı içerisinde bulunuyor.
                sayfaURL="https://httpbin.org/get"
                sayfaCevabi=requests.get(sayfaURL)
                print(sayfaCevabi.status_code)
                print("----1")
                print(sayfaCevabi.content)
                print("----2")
                sayfaCevabi=requests.get(sayfaURL,params={"kullanici_adi":"Tf","sifre":"1234"})
                print(sayfaCevabi.status_code)
                print("----3")
                print(sayfaCevabi.url)
                print("----4")
                print(sayfaCevabi.content)
                print("----5")
                #POST modülü ile sayfa içeriğini alma ve sayfaya veri gönderme 
            kirkdortbir()
        if(b==2):

            sayfaURL="https://jsonplaceholder.typicode.com/posts"
            sayfaCevabi1=requests.post(sayfaURL)
            print(sayfaCevabi1.status_code)
            print(sayfaCevabi1.url)
            print(sayfaCevabi1.content)
            sayfaCevabi2=requests.post(sayfaURL,data={"kullanici_adi":"TF","sifre":"12345"})
            print(sayfaCevabi2)
            print(sayfaCevabi2.url)
            print(sayfaCevabi2.json)

        if(b==3):
            sayfaURL1="https://httpbin.org"
            sayfaCevabi3=requests.get(sayfaURL1)
            print(sayfaCevabi3.status_code)
            
            #text sitenin HTML içeriğini döndürü
            print(sayfaCevabi3.text)

            #headers sitenin hearder bilgisini döndürü
            print(sayfaCevabi3.headers)

            #request siteye yapmış oldupumuz isteğin ne olduğunu döndürü
            print(sayfaCevabi3.request)

            #elapsed toplam geçen süreyi döndürü
            print(sayfaCevabi3.elapsed)

    kırkdort()

if(a==45):
    def kirkbes():
    
        #BEAUTİFULSOUP MODÜLÜ
        #kurulumu pip install beutifulsoup4
        from bs4 import BeautifulSoup
        
        #Beatifulsoup modülüne neden ihtiyacımız var?
        #HTML içeriğini çektiğimiz web siteyi parçalamak için kullanıyoruz        

        #Beautifulsoup obje oluşturarak parçalama işlmei ve prettify fonsksiyonu
        #HTML içeriğini çektiğimiz web siteyi parçalamak için kullanıyoruz
        sayfaURL="https://www.sondakika.com/"
        sayfaCevabi=requests.get(sayfaURL)
        if sayfaCevabi.status_code==200:
            htmlIcerik=sayfaCevabi.content
            soup=BeautifulSoup(htmlIcerik,"html.parser")
            print(soup.prettify())
            

        #belirli bir etiket değerlerini alma ve find fonksiyonu
        #find fonksiyonu ile birlikte oluşturduğumuz beautifulSoup ile parçalayabiliyoruz ve prettify fonksiyonunu 
        #kullanarak düzgün görünmesini sağlayabiliyoruz
        if sayfaCevabi.status_code==200:
            htmlIcerik=sayfaCevabi.content
            soup=BeautifulSoup(htmlIcerik,"html.parser")
            print(soup.find("title").text)
            print(soup.find("li"))#eşleşen ilk html kodunu getiri
            print(soup.find("a"))


        #belirli bir etiket değerlerini alma ve find_all fonksiyonu
        #find_all fonskiyonu ile birlikte oluşturduğuuz beautifulSoup obje üzerinde etiket araması yapabiliriz, 
        #eşleşen etiketler liste halinde bize verilir
        if sayfaCevabi.status_code==200:
            htmlIcerik=sayfaCevabi.content
            soup=BeautifulSoup(htmlIcerik,"html.parser")
            for icerik in soup.find_all("a"):
                print(icerik)
                print(icerik.text)
            print("*************")
            for icerik1 in soup.find_all("span",{"class":"news-txt"}):#class gibi iç parametleri yazmadan önce etiketi kontrol et nasıl yazılmış diye!!!
                print(icerik1)
            print("*************")
            for icerik in soup.find_all("a",{"title"}):
                print(icerik)
            print("*************")
        #etiket içerisinden belirli değerleri alma ve get fonksiyonu
        #get fonksiyonu ile birlikte find_all fonksiyonu ile elde ettiğimiz liste üzerinden belirli kısımları elde edebiliriz
        if sayfaCevabi.status_code==200:
            htmlIcerik=sayfaCevabi.content
            soup=BeautifulSoup(htmlIcerik,"html.parser")
            for icerik in soup.find_all("a"):
                print(icerik.get("href"))
            print("*************")
            for icerik in soup.find_all("a"):
                print(icerik.get("id"))
            print("*************")
            for icerik in soup.find_all("a"):
                print(icerik.get("title"))
            print("*************")
            for icerik in soup.find_all("span"):
                print(icerik.get("class"))
            print("*************")

    kirkbes()

if(a==46):
    def kirkaltı():
        from bs4 import BeautifulSoup

        b=int(input("1.Amazon sitesinde en çok satan kitapları listeleme\n"
        "2.İş bankasından döviz bilgisini gösterme\n"
        "çalıştırmak istediğinizin program sayısını giriniz:"
        ))
        if(b==1):
            sayfaURL="https://www.amazon.com.tr/gp/bestsellers/books/"
            sayfaCevabi=requests.get(sayfaURL)
            if sayfaCevabi.status_code==200:
                htmlicerik=sayfaCevabi.content
                soup=BeautifulSoup(htmlicerik,"html.parser")
                for icerik in soup.find_all("li",{"class":"zg-no-numbers"}):
                    kitapAdi=icerik.find("div",{"class":"_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"})
                    kitapYazari=icerik.find("span",{"class":"a-size-small a-color-base"})
                    kitapPuan=icerik.find("span",{"class":"a-icon-alt"})
                    kitapFiyati=icerik.find("span",{"class":"p13n-sc-price"})
                    if kitapAdi!=None:
                        print("***************")
                        print("Kitabın Adı:"+kitapAdi.text)
                        print("Kitabın Yazarı:"+kitapYazari.text)
                        print("Kitabın Puanı:"+kitapPuan.text)
                        print("Kitabın Fiyatı:"+kitapFiyati.text)
                        print("***************")
                    else: continue
        if(b==2):
            sayfaURL="https://www.albaraka.com.tr/tr/doviz-kurlari"
            sayfaCevabi=requests.get(sayfaURL)
            if(sayfaCevabi.status_code==200):
                htmlicerik=sayfaCevabi.content
                soup=BeautifulSoup(htmlicerik,"html.parser")
                #print(soup)
                for icerik in soup.find_all("tr"):
                    #print(icerik)
                    #print(icerik.find("td",{"class":"text-left"}))
                    #print(icerik.find("td",{"class":"text-center"}))
                    doviz=icerik.find("tr",{"class":"text-left"})
                    dovizalıs=icerik.find("td",{"class":"text-center"})
                    print("doviz adı:"+doviz)
                    print("doviz alış:"+dovizalıs)
                    print("*******")
            
    kirkaltı()

if(a==47):
    def kirkyedi():
        # VERİ TABANI YÖNETİMİ (SQLİTE)
        #*neden ihtiyacımız var?
        #veritabanı, verileri kalıcı ve düzenli bir şekilde saklamaızı, verileri güncellememizi-silmemizi sağlayan veri yığınlarıdır.
        #veritabanında veriler satır ve sütün şeklinde saklanır. Her bir sütuna veriyle alakalı hangi verinin nasıl saklanacağı bilgisi yazılır,
        # her bir ayrı veri ise satırlara kaydedilir.
        #*nasıl yöneteceğiz?
        #birçok programlama dilinde veritabanı yönetmek için temel SQL sorguları mevcuttur.biz de python programlama dilinde hazır olarak sunulmuş
        #sqlite kütüphanesini kullanarak SQlL sorguları ile veritabanını yöneteceğiz
        #1.VERİ EKLEME(CREATE)
        #2.VERİ ALMA(READ)
        #3.VERİ GÜNCELLEME(UPDATE)
        #4.VERİ SİLME(DELETE)
        import sqlite3

        #veri tabanı oluşturma-bağlama ve connect() fonksiyonu
        #sqlite3.connect("veritabani_adi.uzanti")
        #buradaki uzantı .sqlite veya .db olabilir, eğerki verdiğiniz isim ile bir veri tabanı yoksa bulunduğunuz dizine bu veritabanı oluşturulur
        #eğer ki varsa bağlantı kurulur.
        veritabani=sqlite3.connect("ogrenci.db")

        #İmleç(cursor) tanımlama
        #oluşturduğumuz veya bağlantı kurduğumuz veri tabanı üzerinde işlme yapabilmemiz için bir cursor(imleç) oluşturmamız gerekiyor.
        #tüm işlemleri de bu imleci kullanarak yapacağız.
        imlec=veritabani.cursor()

        #TABLO OLUŞTURMA, VERİ TİPLERİ
        #tabloları oluştururken yazılacak verilerin veri tiplerin veri tiplerini önceden belirtmemiz gerekiyor, bu veri tipleri;
        #1.INTEGERR: tam sayılar için
        #2.REAL: ondalıklı sayılar için
        #3.TEXT: karakter dizileri için
        #4.BLOB: binay format için kullanılıyor.
        #bir tabloyu oluşturmal için sorgu içerisinde CRATE komutu kullanmamız gerekiyor, syntax yapısı şu şekilde;
        #CRATE TABLE tablo_adi(sutun1,sutun2,sutun3,...)
        #bu komutu çalıştımka için ise oluşturduğumuz imleç ile birlikte execute() fonksiyonunu kullanmamız gerekiyor
        #oluşturmaSorgu="CREATE TABLE ogrenci(ogrenciAdi TEXT,ogrenciSoyadı TEXT,ogrenciNo INTEGER)"
        #imlec.execute(oluşturmaSorgu)

        #aynı tablodan tekar oluşturmaya kalkarsak hata alırız bunu önüne geçmek için ise;
        #IF NOT EXISTS komutu ile engelleyebiliriz; eğerki tablo yok ise anlamına gelir
        sorgu="CREATE TABLE IF NOT EXISTS ogrenci(ogrenciAdi TEXT,ogrenciSoyadı TEXT,ogrenciNo INTEGER)"
        imlec.execute(sorgu)

        #tabloya kayıt ekleme
        #bir tabloya yeni kayıt eklemek aslında yeni bir satır eklemek anlamına geliyor, bunun için de INSERT INTO komutunu kullanıyoruz;
        #INSERT INTO tablo_adi(sutun1,sutun2,sutun3,...) VALUES(deger1,deger2,deger3,...)
        #imleç ile ekleme, güncelleme veya silme yaptıktan sonra bu işlemler geçici bir veri kümesi üzerinde yapılır. Kalıcı olmasını istiyorsanız
        #ve veritabanına yansımasını istiyorsanız commit() koutunu kullanmanız gerekiyor.
        sorgu2="INSERT INTO ogrenci(ogrenciAdi,ogrenciSoyadı,ogrenciNo) VALUES('taha','fere',1)"
        imlec.execute(sorgu2)#geciçi kayıt yazmış olduk (kayıt bir yerde yazılmayı bekliyor)
        veritabani.commit()

        #parametre ile ekleme
        #bazı durumlarda dışarıdan gelen verilere göre ekleme yapmamız gerekebilir. Bu durumlarda VALUES()kısmına ne yazacağız? 
        #bu durumlarda VALUES(?) şeklinde yazarak ardından parametreyi vereceğiz.
        sorgu3="INSERT INTO ogrenci(ogrenciAdi,ogrenciSoyadı,ogrenciNo) VALUES(?,?,?)"
        ogrenciBilgisi=("Fatmanur","Tilaver",2)
        ogrencibilgisi1=("ahmet","toprak",3)
        imlec.execute(sorgu3,ogrenciBilgisi)
        imlec.execute(sorgu3,ogrencibilgisi1)
        veritabani.commit()

        #kayıt listeleme
        #bir tablodaki verileri verilerin bir kısmını görüntülemek, listelemek, almak için SELECT komutu kullanıyoruz, şu şekilde;
        #SELECT sutun1,sutun2,sutun3,... FROM tablo_adi WHERE sorgu_kosulu
        sorgu4="SELECT ogrenciAdi,ogrenciSoyadı,ogrenciNo FROM ogrenci"
        imlec.execute(sorgu4)

        #verilerin görüntülenmesi
        #SELECT komutuyla verileri alabileceğimizi-listeleyebileceğimiz az önce görmüştük, peki bu verileri nasıl alacağız? nasıl görüntüleceğiz
        #1.FETCHALL: SELECT ile getirilen tüm verileri almak için kullanılır
        #2.FETCHONE: SELECT ile getirilen tek bir satır veriyi okumak için kullanılır, her çağrıldığında bir sonraki satır okunur
        #3.FETCHMANY: SELECT ile getirilen verilerden istediğimiz kadar satır okumak için kullanılır.
        imlec.execute(sorgu4)
        print(imlec.fetchall())
        print("********")

        imlec.execute(sorgu4)
        print(imlec.fetchone())
        print(imlec.fetchone())
        print(imlec.fetchone())
        print("********")

        imlec.execute(sorgu4)
        for ogrenci in imlec:
            print(ogrenci[0])
            print(ogrenci[1])
            print(ogrenci[2])
        print("********")

        imlec.execute(sorgu4)
        print(imlec.fetchmany(3))
        print("********")    

        #imleç üzerinden veri okuma 
        #fonlsiyon kullanmadan olarak SELECT  ile getirilen verileri imlec üzerinden okuyabiliriz
        sorgu4="SELECT ogrenciAdi,ogrenciSoyadı,ogrenciNo FROM ogrenci WHERE ogrenciAdi='taha'"
        imlec.execute(sorgu4)
        for ogrenci in imlec:
            print((ogrenci[0]),(ogrenci[1]),(ogrenci[2]))
        print("********")

        #kayıt güncelleme
        #bir tablodaki verileri güncellemk istiyorsak UPDATE komutunu kullanıyoruz, şu şekilde;
        #UPDATE tablo_adi SET sutun1=yeni_değer,sutun2=yeni_değer....
        sorgu5="UPDATE ogrenci SET ogrenciAdi='ahmet',ogrenciSoyadı='toprak',ogrenciNo=3"
        #imlec.execute(sorgu5)
        veritabani.commit()

        #dikkat
        #eğer ki spesifik bir sorguya göre güncelleme yapmazsanız tüm satırları etkiler
        #peki nasıl koşul ekleyeceğiz? WHERE komutu ile sorgulamalar yapabiliriz
        sorgu5="UPDATE ogrenci SET ogrenciAdi='taha',ogrenciSoyadı='toprak',ogrenciNo=3 "
        #imlec.execute(sorgu5)
        veritabani.commit()

        sorgu5="UPDATE ogrenci SET ogrenciAdi='taha',ogrenciSoyadı='toprak',ogrenciNo=3 Where ogrenciAdi='ahmet'"
        imlec.execute(sorgu5)
        veritabani.commit()
        imlec.execute(sorgu4)
        print(imlec.fetchmany(3))
        print("********")   

        #kayıt silme
        #bir tdan veri silmek istiyorsak DELETE FROM komutunu kullanıyoruz, şu şekilde;
        #DELETE FROM tablo_adi WHERE silme_koşulu
        sorgu6="DELETE FROM ogrenci WHERE ogrenciAdi='ahmet'"
        imlec.execute(sorgu6)
        veritabani.commit()



        #veri tabanı Bağlantı kesilmesi 
        #veri tabanı üerindeki işlemleri yaptıktan sonra veritabanı baplantısını close() fonksiyonu ile kesmemiz gerekiyor
        veritabani.close()

    kirkyedi()

if(a==48):
    def kırksekiz():
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

if(a==49):
    def kırkdokuz():
        #numpy
        #python hazır olarak sunulmuş olan liste yapısından efektir olarak çalışır;hem daha hızlı hemde daha az belek gereksinimi vardrır.
        #veri analiz işlemlerindeki matematiksel hesaplamalar için kullanılır

        #numpy array ı nasıl kullanırız
        #1.direkt liste tanımlar gibi tanımlayabiliriz.
        #2.zeros() fonksiyonu ile tüm elemanları 0 olan dizi tanomlayabiliriz.
        #3.ones() fonksiyonu ile tüm elemanları 1 olan dizi tanımlayabiliriz.
        #4.full() fonksiyonu ile tüm elemanları aynı olan dizi tanımlayabiliriz.
        #5.arange() fonksiyonu ile belirli aralıkta, eleman sayısına göre sabit bir artış ile dizi tanımlayabiliriz.
        #6.linspace() fonkisyonu ile belirli aralıkta, eleman sayısına göre sabit bir artış ile dizi tanımlayabiliriz.
        #7.randint() fonksiyonu ile belirli aralıkta rastgele eleman üreterek dizi tanımlayabiliriz.
        import numpy as np

        npArrayList=np.array([1,2,3,4,5])
        print(type(npArrayList))
        print(npArrayList)

        npZerosList=np.zeros(5,dtype="int")
        print(type(npZerosList))
        print(npZerosList)

        npZerosList2D=np.zeros((5,5))#data type belirmeyince default olarak float oluyor
        print(type(npZerosList2D))
        print(npZerosList2D)

        npOnesArray=np.ones(5,dtype="int")
        print(type(npOnesArray))
        print(npOnesArray)

        npOnesArray2D=np.ones((5,5),dtype="int")
        print(type(npOnesArray2D))
        print(npOnesArray2D)

        npFullArray=np.full((5,5),5)
        print(type(npFullArray))
        print(npFullArray)

        npArangeArray=np.arange(0,50,5)#(başlangıç,bitiş,artış) değerleri sırasıyla girilir bitiş değer çıktıya dağil edilmez
        print(type(npArangeArray))
        print(npArangeArray)

        npLinspaceArray=np.linspace(0,50,10)#(başlangıç,bitiş,kaç_eleman_istiyorsak) veriler girilir
        print(type(npLinspaceArray))
        print(npLinspaceArray)
        
        npRandintArray=np.random.randint(0,50,(5,5))#(başlangıç,bitiş,kaç_eleman)
        print(type(npRandintArray))
        print(npRandintArray)
        print("*****")

        #numpy array bilgileri
        #1.dtype: arraydeki elemanların veri tipi
        #2.size:arraydeki toplam eleman sayısı
        #3.ndim: arrayin boyut sayısını
        #4.shape: arrayin satır-sütun bilgisi
        npArray=np.array([1,2,3,4,5])
        print(npArray)
        print(npArray.dtype)
        print(npArray.size)
        print(npArray.ndim)
        print(npArray.shape)#bunu çıktısı (5,) olucak bu da sadece tek satır olduğu için sütün bilgisi olmadığı için yazmadı

        npArray2D=np.random.randint(2,34,(6,8))
        print(npArray2D)
        print(npArray2D.dtype)
        print(npArray2D.size)
        print(npArray2D.ndim)
        print(npArray2D.shape)

        #array elemanlarına erişmek
        #1.index yardımıyla elemanlara erişmek
        #2.parçalama yardımıyla eleman alt kümelerine erişmek
        print(npArray)
        print(npArray[0])
        print(npArray[4])
        npArray[0]=0
        print(npArray)
        print("*****")
        print(npArray2D)
        print(npArray2D[0])#girilen satırı yazdırır
        print(npArray2D[1])#girilen satırı yazdırır
        print("*****")
        print(npArray2D[1][1])
        print(npArray2D[3][2])
        npArray2D[4][2]=45
        print(npArray2D)

        #parçalama yardımıyla eleman alt kümelerine erişmek array_isim(basalnagıc_indeks:indeks_artıs_miktarı)
        nparray=np.arange(0,50)
        print(nparray)
        print(nparray[::])
        print(nparray[0:-1:1])
        print(nparray[::5])
        print(nparray[:15:5])
        print(nparray[15::5])
        print("*****")
        print(npArray2D)
        print(npArray2D[::,::])#(satır kısmı,sütün kısmı)
        print(npArray2D[0::2,::])
        print(npArray2D[::,1::2])
        print(npArray2D[1::2,1::2])
        print("*****")
        #hazır Foksiyonlar
        #1.reshape(): numpy arrayı yeniden boyutlandırmak için kullanılır.
        #2.concatenate(): Numpy arraylari birleştirmek için kullanılır.
        #3.split(): numpy arrayı bölmek-ayırmak için kullanılır.
        #4.sort(): numpy arrayi sıralamak için kullanılır.
        nparray=np.arange(1,10)
        print(nparray)
        nparray2D=nparray.reshape((3,3))#yeniden boyutlandırıken elimizde ki veri sayısana dikkat edilmeli 
        print(nparray2D)
        nparray2D=nparray.reshape((9,1))
        print(nparray2D)
        a=np.arange(0,10)
        b=np.arange(10,20)
        c=np.concatenate([a,b])
        print(a)
        print(b)
        print(c)
        c=np.concatenate([b,a])
        print(c)
        a=np.array([[1,2,3,4,5],[1,2,3,4,5]])
        b=np.array([[6,7,8,9,10],[6,7,8,9,10]])
        print(a)
        print(b)
        c=np.concatenate([a,b])
        d=np.concatenate([a,b],axis=1)#a ilk satır b ilk satır,a ikinci satır ,b ikinci satır şeklinde birleştirildi
        print(c)
        print(d)
        print(nparray)
        a,b,c=np.split(nparray,3)
        print(a)
        print(b)
        print(c)
        print(npArray2D)
        a,b=np.vsplit(npArray2D,[2])
        print(a)
        print(b)
        c,d=np.hsplit(npArray2D,[2])
        print(c)
        print(d)
        randomarray=np.random.randint(0,50,(1,10))
        print(randomarray)
        sortedArray=np.sort(randomarray)
        print(sortedArray)
        randomarray=np.random.randint(0,50,(2,10))
        print(randomarray)
        sortedArray=np.sort(randomarray)
        print(sortedArray)
        randomarray=np.random.randint(0,50,(5,10))
        print(randomarray)
        sortedArray=np.sort(randomarray,axis=0)#sütuna göre sıralama yapıldı
        print(sortedArray)
        print("*********")

    kırkdokuz()