def yirmi():
    # "w": "Write" anlamına geliyor ve dosyayı yazma modunda açmamızı sağlıyor. Eğerki belirtilen dosya yok ise dosya oluşturulur,
    # var ise eski dosya içeriği silinri
    #"a":"append" anlamına geliyor ve dosyayı yazma modunda açmamızı sağlıyor. Eğer ki belirtilen dosya yok ise dosya oluşturulur,
    #var ise eski dosyanın sonuna ekleme yapılır.
    #"r":"read" anlmanına geliyor ve dosyayı okuma modunda açmamızı sağlıyor. Eğer ki belirtilen dosay var ise okuma yapabilir.
        try:
            dosya=open("ornek.txt","w")
            dosya1=open("ornek2.txt","a")
            #dosya2=open("ornek3.txt","r")
            dosya.close()
            dosya1.close()
        except FileNotFoundError:
            print("belirtilen dosya bulunmadı")
    
    #write() fonksiyonudur: Dosyayı açtıktan sonra, write fonksiyonunu kullanarak dosyaya yazma yapabiliriz. Yan yana yazma işlemi yapılacatır.
    #alt satıra geçmek için "\n" kullanılabilir
        dosya=open("ornek.txt",mode="w")
        dosya.write("hava savunma\nastsubay astcavus \tTaha Fere \nKalkan 2 Kisim komutani\n")
        dosya.write("FATMANUR COK SEVIYORUM\n")
        dosya.write("cok cok cok cok seviyorum\n")
        dosya.close()
        
        dosya=open("ornek.txt",mode="a")
        dosya.write("denememeee\n")
        dosya.write("booooom\n")
        dosya.close()

        dosya=open("ornek1.txt",mode="w")
        for i in range(1,21):
            dosya.write("{}.satir\n".format(i))
        dosya.close()

        print("-----------------------------------")

        #read() fonksiyonu: Dosya açtıktan sonra, read fonksiyonunu kullanarak dosyadan okuma işlemi yapabiliriz
        #readline() fonksiyonu: Dosyayı açtıktan sonra, Readline fonksiyonunu kullanarak dosyadan satır satır okuma işlemi yapabiliriz.
        #readlines() fonksiyonu: Dosyayı açtıktan sonra, readlines fonksiyonunu kullanarak tüm satırları okuyabilir ve döngü yardımıyla erişebiliriz
        try:
            dosya=open("ornek1.txt",mode="r")
            print(dosya.read())
        except:
            print("dosya bulunamadı")
        print("---------------------------------")
        try:
            dosya=open("ornek1.txt",mode="r")
            print(dosya.readline())
            print(dosya.readline())
            print(dosya.readline())

        except:
            print("dosya bulunamadı")

        print("---------------------------------")
        try:
            dosya=open("ornek1.txt",mode="r")
            tumsatir=dosya.readlines()
            for satir in tumsatir:
                print(satir)

        except:
            print("dosya bulunamadı")

        print("-----------------------------------")
        #append() modu: Dosyayı açtıktan sonra, write fonksiyonunu kullanarak dosyaya yazma işlemi yapabilirz.
        dosya=open("ornek1.txt",mode="a")
        dosya.write("\ndeneme\n")



yirmi()
