def sekiz():
        faktoriyelsonucu=1
        sayi=int(input("lütfen faktöriyel bitiş sayısını giriniz:"))
        for i in range(2,sayi+1):
            faktoriyelsonucu*=i
        print("{}!={}".format(sayi,faktoriyelsonucu))
        print("\n---------------------")
        faktoriyelsonucu1=1
        sayaç1=1
        sayi1=int(input("faktörü hesaplanacak sayı giriniz:"))
        while(sayaç1<=sayi1):
            faktoriyelsonucu1*=sayaç1
            sayaç1+=1
        print("{}!={}".format(sayi1,faktoriyelsonucu1))
        print("\n---------------------")
        sayi3=int(input("lütfen hesaplanacak sayıyı giriniz:"))
        gecici=sayi3
        basmaksay=0
        while gecici!=0:
            gecici//=10
            basmaksay+=1
        print("{} sayisi {} basamaklıdır".format(sayi3,basmaksay))
        gecici1=sayi3
        basmaksay1=1
        for basmaksay1 in range(100):
            gecici1//=10
            basmaksay1+=1
            if(gecici1!=0):
                continue
            print("{} sayisi {} basamaklıdır".format(sayi3,basmaksay1))
            break
        print("\n----------------------------")
        sayi4=int(input("asal sayı değerniri giriniz:"))
        bolundumu=False
        for i in range(2,sayi4):#
            if(sayi4%i==0):
                bolundumu=True
                break
        if(bolundumu):
            print(sayi4,"asal değildir")
        else:
            print(sayi4,"asal sayi sayidir ")
        print("\n----------------------------")
        sayi5,sayi6=map(int,input("lüften EBOB-EKOK hesaplanacak iki sayı giriniz ',' koyarak :").split(","))
        buyuksayi=int()
        kucuksayi=int()
        EKOK=int()
        EBOB=int()
        if(sayi5>sayi6):
            buyuksayi=sayi5
            kucuksayi=sayi6
        else:
            buyuksayi=sayi6
            kucuksayi=sayi5
        #EKOK böümü
        sayac=buyuksayi
        while True:
            if(sayac%buyuksayi==0 and sayac%kucuksayi==0):
                EKOK=sayac
                break
            sayac+=1
        #EBOB bölümü
        sayac=kucuksayi
        while True:
            if(buyuksayi%sayac==0 and kucuksayi%sayac==0):
                EBOB=sayac
                break
            sayac-=1
        print("{} ve {} sayılarının EBOB değeri:{} EKOK değeri:{}".format(sayi5,sayi6,EBOB,EKOK))
        print("\n----------------------------")

        bosluk=0
        cumle=input("lütfen cümle giriniz:")
        for harf in cumle:
            if harf==" ":
                bosluk+=1
        print(cumle,"cümlesinde toplam",bosluk,"karakteri geççiyor")
        print("\n-------------------------")
        sayi7=int(input("lütfen sayıyı giriniz:"))
        gecicisay=sayi7
        sayiters=0
        while(gecicisay!=0):
            kalan=gecicisay%10
            sayiters=sayiters*10+kalan
            gecicisay//=10
        print("{} sayinin tersi :{}".format(sayi7,sayiters))
sekiz()