import random
def altı ():
        print("İF-ELSE-ELİF yapıları")
        if (5>3):#true sonuç dondüğü için buraya döndü
            print("if bloğuna girdi")
        elif(8>7):#başta true bulduğu için buralara bakamdı
            print("elif bloğuna girdi")
        print("-----------------------------")
        if (2>3):#false olduğu için bu bloğu atladı
            print("if bloğuna girdi")
        elif(8>7):#true olduğu için bu bloğa girdi
            print("elif bloğuna girdi")
        print("-----------------------------")
        if (2>3):#false olduğu için bu bloğu atladı
            print("if bloğuna girdi")
        elif(8>7):#false olduğu için bu bloğu atladı
            print("elif bloğuna girdi")
        else:#true olduğu için bu bloğa girdi
            print("else bloğunaa girdi")
        print("-------------------------------------------")
        sayi=int(input("sorgunlacak sayıyı giriniz: "))
        if(sayi%2==0):
            print(sayi,"çift sayidir")
        else:
            print(sayi,"tek sayıdır")
        print("-------------------------------------------")
        sayi1=random.randint(1,5)
        sayi2=random.randint(1,5)
        print("sayı1={} ve sayı2={}".format(sayi1,sayi2))
        if(sayi1>sayi2):
            print("sayı1 büyüktür.")
        elif(sayi2>sayi1):
            print("sayı2 büyüktür")
        else:
            print("sayılar eşittir")
        print("-------------------------------------------")        
        print("HESAP MAKİNESİ")
        sayi1=int(input(("1.sayıyı giriniz:")))
        sayi2=int(input(("2.sayıyı giriniz:")))
        opertor=str(input("+,-,*,/,^,'%' operatörlerinden birini giriniz"))
        if(opertor=="+" or opertor=="-" or opertor=="*" or opertor=="/"or opertor=="^"or opertor=="%"):
            if(opertor=="+"):
                print(sayi1,opertor,sayi2,"=",(sayi1+sayi2))
            elif(opertor=="-"):
                print(sayi1,opertor,sayi2,"=",(sayi1-sayi2))
            elif(opertor=="*"):
                print(sayi1,opertor,sayi2,"=",(sayi1*sayi2))
            elif(opertor=="/"):
                print(sayi1,opertor,sayi2,"=",(sayi1/sayi2))
            elif(opertor=="^"):
                print(sayi1,opertor,sayi2,"=",(sayi1**sayi2))
            elif(opertor=="%"):
                print(sayi1,opertor,sayi2,"=",(sayi1%sayi2))
        else:
            print("lütfen geçerli operatör giriniz")
        print("-------------------------------------------")
        print("""
            ATM uygulamasına hoş geldiniz.
                 PARA ÇEKMEK İÇİN: 1
                PARA YATIRMAK İÇİN: 2
            BAKİYENİZİ ÖĞRENMEK İÇİN: 3  
            """)
        bakiye=67459
        gunlukcekim=5000
        secim=int(input("LÜTFEN YAPMAK İSTEDİĞİNİZ SEÇENİĞİN NUMARASINI GİRİNİZ:"))
        if(secim==1 or secim==2 or secim==3):
            if(secim==1):
                cekim=int(input("GÜNLÜK ÇEKİM TUTARI 5000TL, ÇEKMEK İSTEDİĞİNİZ TUTARI YAZINI:"))
                if(cekim<gunlukcekim):
                    if(cekim<bakiye):
                        print(cekim,"tutarında para çekimi başarılıdır. Kalan bakiye:",(bakiye-cekim))
                    else:
                        print("HESABINIZ DA O KADAR BAKİYE BULUNUMAMAKTADIR...")
                else:
                    print("LÜTFEN GÜNLÜK ÇEKİM TUTARINI GEÇMEYENİZ...")
            elif(secim==2):
                yatir=int(input("Hesabınıza yatırılacak tutarı giriniz:"))
                if(yatir<=0):
                    print("LÜTFEN GEÇERLİ BİR TUTAR GİRİNİZ....")
                else:
                    print(yatir,"tutarında para hesabınıza yatırılmıştır. Hesabınızdaki bakiye:",(bakiye+yatir))
            elif(secim==3):
                print("HESABINIZDA {} BAKİYE BULUNMAKTADIR.".format(bakiye))
        else:
            print("LÜFTEN GEÇERLİ İŞLEM NUMARASI GİRİNİZ.........")
        sayi=random.randint(1,99999)
        #***basamak=0
        #kont=sayi%10
        #if(sayi>kont):
        #    print("1",sayi%10)
        #    basamak+=1
        #kont=sayi%100
        #if(sayi>kont):
        #    print("2",sayi%100)
        #    basamak+=1
        #kont=sayi%1000
        #if(sayi>kont):
        #    print("3",sayi%1000)
        #    basamak+=1    
        #kont=sayi%10000
        #if(sayi>kont):
        #    print("4",sayi%10000)
        #    basamak+=1
        #kont=sayi%100000
        #if(sayi>=kont):
        #    print("5",sayi%100000)
        #    basamak+=1
        ##print(sayi,"sayı",basamak,"basamaklıdır.")
        if(sayi<10):
            print(sayi,"sayi 1 basamaklıdır")
        elif(sayi<100):
            print(sayi,"sayi 2 basamaklıdır")
        if(sayi<1000):
            print(sayi,"sayi 3 basamaklıdır")
        if(sayi<10000):
            print(sayi,"sayi 4 basamaklıdır")
        else:
            print(sayi,"sayi 5 basamaklıdır")
    
        print("---------------------------------------")
        print("ALIŞVERİŞ UYGULAMIMIZA HOŞ GELDİNİZ")
        tutar=int(input("LÜTFEN ALIŞVERİŞ TUTARINIZI GİRİNİZ:"))
        print("""
                 TAKSİT SEÇENEKLERİ:
             0=>    TAKSİT OLMASIN
             1=>    3 TAKSİT %3
             2=>    6 TAKSİT %6
             3=>    9 TAKSİT %9
                """)
        taksit=int(input("LÜTFEN İSTEĞİNİZ TAKSİT SEÇENEĞNİN NUMARSINI GİRİNİZ:"))
        if(taksit==1):
            tutar+=tutar*0.03
        elif(taksit==2):
            tutar+=tutar*0.06
        elif(taksit==3):
            tutar+=tutar*0.09
        elif(taksit==0):
            print(tutar)
        else:
            print("HATALI GİRİŞ YAPILDI.......")
        print("ALIŞVERİŞ KARTINIZ VAR MI ?\n VARSA 1 TUŞALYINIZ YOKSA 0 TUŞLAYINIZ")
        kart=int(input("ALIŞVERİŞ KARTI:"))
        if(kart==1):
            tutar=tutar-(tutar*0.1)
            print("ALIŞVERİŞ TUTARINIZ:",tutar)
        elif(kart==0):
            print("ALIŞVERİŞ TUTARINIZ:",tutar)
        else:
            print("HATALI GİRİŞ YAPTINIZ")
    
        print("---------------------------------------")
    
        print("ÜÇGEN KONTROL UYGULAMASI")
        x,y,z=map(int,input("lütfen üçgen kenarlarını aralara ',' koyarak giriniz:").split(","))
        if(abs(y-z)>=x or x>=y+z):
            print("x kenarı üçgen şartını sağlamıyor")
        elif(abs(x-z)>=y or y>=x+z):
            print("y kenarı üçgen şartını sağlamıyor")
        elif(abs(x-y)>=z or z>=x+y):
            print("x kenarı üçgen şartını sağlamıyor")
        else:
            print("üçgen oluşturula bilir")
altı()