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
