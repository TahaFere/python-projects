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
