def oniki():
    #--------------DEMETLER------------------
    #çok sayıda değişkenleri bir arada saklayabilmek, daha kolay şekilde erişebilmek için kullanıyoruz.
    #Aynı yada farklı türde birden çok değeri bir arada saklamamıza imkan veren bir yapıdır.
    #.... ÖNEMLİ demetler oluştukdan sonra yeni eleman eklenemez, güncellenemez, silinemez.......
        demet=tuple()
        demet1=()
        print(type(demet),type(demet1))
        demet=(1,2,3,4,5,6)
        demet1=("kalkan","2","kısım","komutanı")
        demet2=("merhaba",2,False,"bebeğim",3.5,[1,2,3,4])
        print(demet)
        print(demet1)
        print(demet2)
        for eleman in demet:
            print(eleman,eleman**2)
        print(len(demet))
        for i in range(len(demet)):
            print(i,"=",demet[i])
        demet3=demet[3:]
        demet4=demet[:3]
        demet5=demet[::2]
        demet6=demet[::-1]
        print(demet3)
        print(demet4)
        print(demet5)
        print(demet6)
        #demet içinde elemen kontrolü
        # in, not in, index komutu kullanımı
        print(2 in demet2)
        print(False in demet2)
        print(3 not in demet)
        print(89 in demet)
        print(demet.index(2))
        if 5 in demet:
            print(demet.index(5))
        #demet içinde elemen kontrolü
        # in, not in, index komutu kullanımı
        print(min(demet))
        print(min(demet1))
        print(max(demet))
        print(max(demet1))
        print(sum(demet))
oniki()