def ondort():
        #------------------KÜMELER--------------
        #Listeler ve demetler gibi birden çok elemanın bir arada saklanabilmesine olanak sağlar
        #ancak demetkerin aksine değiştirilebilir yapılardadır.
        kume=set()
        #kume2={} böyle kulanımda sözcük türünde oluşmuş oluyor
        kume2={1,2,3,54,6,7}
        kume3={"kalkan","2","kısım","komutanı","taha","fere"}
        kume4={1,2,3.5,"denem","boom"}
        print(kume)
        print(kume2)
        print(kume3)
        print(kume4)
        print(type(kume))
        print(type(kume2))
        print(type(kume3))
        print(type(kume4))
        print(len(kume4))
        print("----------------------------------------")
        #add() ekleme, remove() çıkarma, difference() bir kümede olup ikinci kümede olmayan elemanları bulur komutalarının kullanımı
        sayikumesi={1,2,3,4,5}
        print(sayikumesi)
        sayikumesi.add(6)
        sayikumesi.add(7)
        sayikumesi.add(8)
        print(sayikumesi)
        sayikumesi.remove(6)
        sayikumesi.remove(2)
        sayikumesi2={1, 2, 4, 5, 6, 9, 78}
        print(sayikumesi)
        print(sayikumesi2)
        print(sayikumesi.difference(sayikumesi2))
        print(sayikumesi-sayikumesi2)
        print(sayikumesi2.difference(sayikumesi))
        print(sayikumesi2-sayikumesi)
        #intersection() komutu[kesişim]: iki kümede ortak olan elemanları bulmak için kullanılır.
        #isdisjoint() komutu[ayrık küme]: iki kümenin ortak elemanı var mı yok mu bu sorgulanır
        # eğer ki hiç ortak eleman yoksa True sonuç verir aksı halde False sonuç verir.
        #issubset() komutu[alt küme içindeki küme]: bir kümedeki elemanların hepsinin başka bir küme içeriyor mu bunu sorgular
        # eğer içeriyorsa True aksi halde False sonuç verir
        #issuperset() komutu[alt kümenin dışında ki büyük küme]: bir küme, diğer kümedeki elemanları içeriyor mu bunu sorgular
        # eğer ki içeriyorsa True aksi halde False sonuç verir
        #union() komutu[birleşim]: iki kümenin birleşimini bulmak için kullanılır.
        küme1={1,2,3,4,5}
        küme2={1,2,3,4,5,6,7,8,9,10}
        print(küme1.intersection(küme2))
        print(küme2.intersection(küme1))

        print(küme1.isdisjoint(küme2))
        print(küme2.isdisjoint(küme1))

        print(küme1.issubset(küme2))
        print(küme2.issubset(küme1))

        print(küme1.issuperset(küme2))
        print(küme2.issuperset(küme1))

        print(küme1.union(küme2))
        print(küme2.union(küme1))
        print(küme1|küme2)
ondort()