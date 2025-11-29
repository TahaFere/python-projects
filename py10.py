def on():
        sayi9=int(input("armstrong sayı kontrolü için sayı giriniz:"))
        kontrol=0
        for ac in str(sayi9):
            kontrol+=int(ac)**3
        if kontrol==sayi9:
            print(sayi9,"sayısı armstrong sayısıdır.")
        else:
            print(sayi9,"sayısı armstrong sayısı değildir.")
    
        print("\n------------------------")
        for ac in range(1,10000):
            kontrol=0
            for ad in str(ac):
             kontrol+=int(ad)**3
            if kontrol==ac:
                print(ac,"sayısı armstrong sayısıdır.")
                continue
            
        print("\n------------------------")
        print("MÜKEMMEL SAYI.....")
        say8=int(input("kontrol edilmesi istediğiniz mükemmel sayıyı giriniz:"))
        sayac1=1
        toplam=0
        while True:
            if(sayac1<say8):
                if(say8%sayac1==0):
                    toplam+=sayac1
                sayac1+=1
                continue
            
            if(say8==toplam):
                print(say8,"sayı mükemmel sayi değildir.")
                break
            
            else:
                print(say8,"sayısı mükemmel sayıdır.")
                break
        print("\n----------------------------")
on()