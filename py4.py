def dort ():
        gir=int(input("lütfen para tutarı giriniz: "))
        gir1=gir
        print("girilen para miktarı:",gir)
        ikiyuz=gir1//200
        gir1=gir1-(ikiyuz*200)
        print(gir,"tutarında 200 tl şu kadar=",ikiyuz,"kalan miktar=",gir1)
        yuz=gir1//100
        gir1=gir1-(yuz*100)
        print(gir,"tutarında 100 tl şu kadar=",yuz,"kalan miktar=",gir1)
        elli=gir1//50
        gir1=gir1-(elli*50)
        print(gir,"tutarında 50 tl şu kadar=",elli,"kalan miktar=",gir1)
        yirmi=gir1//20
        gir1=gir1-(yirmi*20)
        print(gir,"tutarında 20 tl şu kadar=",yirmi,"kalan miktar=",gir1)
        on=gir1//10
        gir1=gir1-(on*10)
        print(gir,"tutarında 10 tl şu kadar=",on,"kalan miktar=",gir1)
        bes=gir1//5
        gir1=gir1-(bes*5)
        print(gir,"tutarında 5 tl şu kadar=",bes,"kalan miktar=",gir1)
dort()