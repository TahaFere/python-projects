def onbes():
        print("------------------------------------------------")
        #----------------FONKİSYONLAR-----------------
        #prohram içerisinde birden çok kez tekrar edicek durumları tek bir fonksiyon içerisinde yazıp kod tekrarını önlemek için
        def selamlar():
            print("Merhaba")
        selamlar()
        selamlar()
        def selamla1(isim):
            print("Merhaba",isim)
        selamla1("taha")
        selamla1(16)
        print("-------------------")
        def selamla2(isim="FatmaNur"):#istenilen değer kullanıcan gelmezse diye varsayılan değer tanımlanmalıdır
            print("merhaba",isim)
        selamla2("taha")
        selamla2()
        def selamla3(isim="Fatma Nur",isim1="taha"):#varsayılan değer tanımlandığınde istenilen bütün değerlere tanımlanmalıdır
            print("merhaba",isim,isim1)
        selamla3("Taha","Fatma Nur")
        selamla3(isim1="booom",isim="mademmor")
        def elemanyazdır(*sayilar):#belli olmayan sayıda parametre gelmesi durumunda kullanılır 
            for sayi in sayilar:
                print(sayilar,end="\n")
        elemanyazdır(12,42,5431,453,5,23,5523,12)
        print("-----------------------------")
        def topla(sayi1,sayi2):
            sonuc=sayi1+sayi2
            return sonuc
        sonuc=topla(5,13)
        print(sonuc)

        def listebüyükkücük(liste):
            liste.sort()
            enbuyuk=liste[-1]
            enkucuk=liste[0]
            return enkucuk,enbuyuk
        kucuk,buyuk=listebüyükkücük([1,31,234,124,547,23,35785,46,2,78,34,57,3,6,37])
        print(kucuk,buyuk)
        print("---------------------")
        def faktoriyelhesapla(sayi):#özyinelemi fonksiyon bunun amacı foksiyon içinde kendini yeniden çağırması
            if sayi==1:
                return 1
            return sayi*faktoriyelhesapla(sayi-1)
        print(faktoriyelhesapla(5))
        print("-------------------------------------")
        def sayidegistir(x):
            x=5#local değişken
            print(y)
        y=60#global değişken
        sayidegistir(y)
        print(y)
        print("-----------------------------------------------")

        def karakterdeğiştirme(metin,eskikarakter,yenikarakter):
            metin1=str()
            for i in metin:
                if i==eskikarakter:
                    i=yenikarakter
                    metin1+=i
                    continue
                else : 
                    metin1+=i
                    continue
            return metin1
        def harfdegistir(metin,eskikarakter,yenikarakter):
            cumle=list(metin)
            for indis in range(len(cumle)):
                if cumle[indis]==eskikarakter:
                    cumle[indis]=yenikarakter
            return cumle
        yenimetin=karakterdeğiştirme("hava savunma astsubay astçavuş Taha Fere Kalkan 2 Kısım komutanı"," ","-")
        print(yenimetin)
        yenimetin1=karakterdeğiştirme("hava savunma astsubay astçavuş Taha Fere Kalkan 2 Kısım komutanı","a","|")
        print(yenimetin1)
        girilenmetin=input("lütfen değişiklik yapılacak metnini girinz:")
        eskikarakter,yenikarakter=input("metinde değiştirilmesi istediğinizi eski ve yeni karakteri giriniz (karakterler arasına ',' koyunuz):").split(",")
        print(karakterdeğiştirme(girilenmetin,eskikarakter,yenikarakter))
        yenimetin2=str(harfdegistir(girilenmetin,eskikarakter,yenikarakter))
        print(yenimetin2)
        girilenmetin1=input("lütfen düzenlenmesini istediğiniz uzun metin giriniz:")
        def harfbuyutme(metin):
            cumle=list(metin)
            cumle[0]=cumle[0].upper()
            for indis in range(len(cumle)):
                if cumle[indis]==".":
                    cumle[indis+1]=cumle[indis+1].upper()
            return cumle     
        print(harfbuyutme(girilenmetin1))

        def anagramkont(sozcuk1,sozcuk2):
            soz1=set(sozcuk1)
            soz2=set(sozcuk2)
            if len(sozcuk1)!=len(sozcuk2):
                return False
            elif soz1.issuperset(soz2):
                return True
            elif soz2.issuperset(soz1):
                return True
            else: return False              
        sozcuk1,sozcuk2=input("lütfen anagram kontrolü yapılması için 2 sözcük giriniz araya ',' koyunuz:").split(",")
        print("anagram kontrolü sonucu:",anagramkont(sozcuk1,sozcuk2))


        def palindromkont(sozcuk1):
            terssoz=sozcuk1[::-1]
            if sozcuk1==terssoz:
                return True
            return False
        #    soz1=list(sozcuk1)
        #    soz2=list(sozcuk2)
        #    x=0
        #    for i in range(len(soz1)):
        #        x-=1
        #        if soz1[i]==soz2[x]:
        #            continue
        #        else: return False
        #    if abs(x)==len(soz1):
        #        return True
        kelime1=input("palindrom kontrolü yapılması istediğiniz kelime giriniz :")
        print("palindrom kontrolü sonucu:",palindromkont(kelime1))

        def fibonacci(sayi):
            if sayi==0 or sayi==1:
                return sayi
            return fibonacci(sayi-1)+fibonacci(sayi-2)
        girsayi=int(input("fibonaci kaçıncı basamağa kadar açılsın:"))
        print(fibonacci(girsayi))


        def unlubulma (metin):
            soz=list(metin)
            sayma=0
            for i in range(len(soz)):
                if soz[i]=="a" or soz[i]=="e" or soz[i]=="i" or soz[i]=="u" or soz[i]=="o":
                    sayma+=1
            return sayma
        giris=input("ünlü harfleri saydırmak metin giriniz:")
        print(unlubulma(giris))

        def unluharfHesaplama(string):
            unluharfler=['a','e','i','u','o']
            unluharfsayilar=[0 for i in range(5)]
            for indeks in range(len(unluharfler)):
                if unluharfler[indeks] in string:
                    sayi=string.count(unluharfler[indeks])
                    unluharfsayilar[indeks]=sayi
            for indeks in range(len(unlubulma)):
                print("{} harfi {} kere geçmektedir.".format(unluharfler[indeks],unluharfsayilar[indeks]))
        giris=input("ünlü harfleri saydırmak metin giriniz:")
        print(unluharfHesaplama(giris))

        def ortkarakersay(metin):
            cumle=list(metin)
            kelime=1
            for i in range(len(metin)):
                if cumle[i]==" ":
                    kelime+=1
            return len(metin)/kelime
        giris=input("lütfen karakter ortalaması hesaplanması için metin giriniz:")
        print(ortkarakersay(giris))

        def essizkarakter(metin):
            soz=set(metin)
            soz.remove(" ")
            return len(soz)
        giris=input("lütfen eşsiz karakter hesaplanması için sözcük giriniz:")
        print(essizkarakter(giris))


        def enbuyukenkucuk (giris,say):
            liste=set(giris)
            liste.remove(",")
            liste=list(liste)
            liste.sort()
            return liste[int(say)-1],liste[-int(sayi)]
        giris,sayi=input("lütfen liste giriniz ve listeden kaçıncı istediğinizi giriniz liste arasında ',' liste ile istediğiniz sayı arasında '-':").split("-")
        print(enbuyukenkucuk(giris,sayi))

        def OBEB (sayi1,sayi2):
            if sayi2==0:
                return sayi1
            return OBEB(sayi1,sayi2%sayi2)

        def OKEK (sayi1,sayi2):
            return sayi1*sayi2//OBEB(sayi1,sayi2)
        print("{} ve {} sayılarının OBEB={}, OKEK={}".format(3,5,OBEB(3,5),OKEK(3,5)))
onbes()