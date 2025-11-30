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
