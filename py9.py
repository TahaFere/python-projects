def dokuz():
        sayi7=int(input("üçgen limitini giriniz:"))
        baslangıc=1
        baslangıc1=1
        son=sayi7
        son1=sayi7*2
        ucgen='x'
        while baslangıc<=sayi7:
            print(ucgen*baslangıc,"\t",ucgen*son,"\t",ucgen*son1,"\t",ucgen*baslangıc1)
            baslangıc1+=2
            son1=son*2-1
            baslangıc+=1
            son-=1

        print("\n--------------------------------------")
        print("""
                ŞİFRESİNİZDE DİKKAT ETMENİZ GEREKENLER!!!!!
              1.ŞİFRENİZDE HEM BÜYÜK VE HEM KÜÇÜK HARF KULLANILMALIDIR
              2.ŞİFRENİZİN İÇİNDE BİR TANE SAYI İÇERMELİDİR.
              3.ŞİFRENİZ EN AZ 8 KARAKTERDEN OLUŞMALIDIR.
              4.ŞİFRENİZ EN UZUN 16 KARAKTERDEN OLUŞMALIDIR.            
    """)
        sifre=input("lütfen kontrol edilmesi gereken şifresinizi giriniz:")
        kontsayi=False
        buyukharf=False
        kucukharf=False
        sifresay=0
        for ch in sifre:
            if  buyukharf==False and ch>='A' and ch<='Z':
                buyukharf=True
            elif kucukharf==False and ch>='a' and ch<='z':
                kucukharf=True
            elif kontsayi==False and ch>='0' and ch<='9':
                kontsayi=True
            sifresay+=1
        if buyukharf==False:print("büyük harf kullanmanız gerekir...")
        elif kucukharf==False:print("küçük harf kullanılması gerekir...")
        elif kontsayi==False:print("sayi kullanılması gerekir....")
        elif sifresay<8:print("karakter sayısı azdır...")
        elif sifresay>16:print("karakter sayısı fazladır...")
        else:print("şifre uygundur....")
        #for kont in sifre:
        #    sifresay+=1
        #    for sayi in range(0,10):
        #        if kont==str(sayi):
        #            kontsayi=True
        #            break
        #        else:
        #            continue
        #if sifresay<8 or sifresay>16:
        #    if sifresay<8:
        #        print("ŞİFRENİZ KISA....")
        #    else:
        #        print("ŞİFRENİZ ÇOK UZUN....")
        #elif kontsayi==False:
        #    print("ŞİFRENİZDE SAYI İÇERMELİDİR....")
        #else:
        #    print("ŞİFRENİZ UYGUNDUR....")


        print("\n-----------------------------")
        sayi8=int(input("MÜKENMEL SAYI KONTROLÜ LÜTFEN SAYIYI GİRİNİZ:"))
        topla=0
        for i in range(1,sayi8):
            if(sayi8%i==0):
                topla+=i
        if topla==sayi8:
            print(sayi8,"sayı mükenmel sayıdır.")
        else:
            print(sayi8,"sayı mükenmel sayı değildir.")
        print("\n--------------------------")

        for ab in range(1,1000):
            topla=0
            for ii in range(1,ab):
                if(ab%ii==0):
                    topla+=ii
            if topla==ab:
                print(ab,"sayı mükenmel sayıdır.")
        print("\n--------------------------")
dokuz()