import math
def onalti():
        # ----------------- HAZIR MATEMATİK KOMUTLARI-----------------------
        #abs komutu mutlak değer hesaplamak için kullanılır
        print(abs(-5))

        #ceil() komutu: Ondalık kısmı bulunan sayıların bir üstteki tamsayıya yuvarlamak için kullanılır
        #floor() komutu: Ondalık kısmı bulunan sayıların bir alttaki tamsayıya yuvarlamak için kullanılır
        #round() komutu: Ondalık kımsını bulunan sayıları; ondalık kısımlaro 0,5'ten büyükse üstteki tam sayıya,
        #küçükse alttaki tam sayıya yuvarlanmak için kullanılır
        print(math.ceil(1.3),math.floor(3.7),round(2.6),round(6,3))

        #pow() komutu: Üs alma işlemi için kullanılır; ilk parametre taban ve ikinci parametre üst değerini belirtir
        print(math.pow(3,5))

        #sqrt() komutu: karekök alma işlemi için kullanılır.
        print(math.sqrt(81))
        print(math.sqrt(100))

        #log() komutu: Matematikteki log alma işleminin karşılığıdır, bir sayı bir sayının kaçıncı kuvvetidir bunu hesaplar
        print(math.log(81,9))
        print(math.log(27,3))

        #sin() komutu: Sinus değerini hesaplamak için kullanılır.
        #cos() komutu: Cosinus değerini hesaplamak için kullanılır.
        #tan() komutu: Tanjant değerini hesaplamak için kullanılır.
        #radians() komutu: Yukarıdaki fonksiyonları kullanabilmek için açı derecelerini ilk olarak radyant cinsine çevirmemiz gerekir
        derece=math.radians(90)
        print(derece)
        print(math.sin(derece))
        print(math.cos(derece))
        print(math.tan(derece))

        #bin() komutu: Bir sayıyı ikili taban karşılığına dönüştürmek için kullanılır.
        print(bin(128))

        #divmod() komutu: Bir sayının başka bir sayıya bölümü ve kalanı verir
        print(divmod(8,3))# çıktısı(2,2) ilk kısım bölüm diğer ksıım kalan
onalti()
