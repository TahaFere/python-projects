def onuc():
        #----------------SÖZLÜKLER-----------------
        #elemanları anahtar- değer(key-value) yapısında saklamak için kullanılır.
        #sözcükler üzerinde ekleme, silme, güncelleme gibi işlemler yapılabilir.
        sozluk=dict()
        sozluk1={}
        print(type(sozluk),type(sozluk1))
        sayısozlugu={"1":"bir","2":"iki","3":"üç","4":"dört"}
        print(sayısozlugu["1"])
        print(sayısozlugu["2"])
        print(sayısozlugu["3"])
        for anahtar in sayısozlugu:
            print("{}:{}".format(anahtar,sayısozlugu[anahtar]))
        #in ve not in komutları
        if "4" in sayısozlugu:
            print(sayısozlugu["4"])
        else:
            print("böyle bir anahtar yok")
        #get komutu: içerisnine yazdığımız anahtara ait değeri getirilmesini sağlar.
        #eğer ki değeri yoksa hata üretmez ve NONE sonucu verir
        print(sayısozlugu.get("1"))
        print(sayısozlugu.get("2"))
        print(sayısozlugu.get("3"))
        print(sayısozlugu.get("4"))
        print(sayısozlugu.get("5"))
        sayısozlugu["5"]="beş"
        print(sayısozlugu)
        sayısozlugu["0"]="sıfır"
        print(sayısozlugu)
        sayısozlugu["2"]="İKİ"
        print(sayısozlugu)
        del sayısozlugu["0"]#iki ksımıda silecektir
        print(sayısozlugu)
        #items(), keys(), values() komutalrının kullanımı
        for anahtar,deger in sayısozlugu.items():
            print(anahtar,":",deger)
        for anahar1 in sayısozlugu.keys():
            print(anahar1)
        for deger1 in sayısozlugu.values():
            print(deger1)
        print("sayısoclugu {} eleman içermektedir.".format(len(sayısozlugu)))
        # update(), copy(), clear(), del(), komutlarını kullanma
        sayiguncel={"1":"BİR","2":"İKİ","3":"UC","4":"DÖRT","5":"BES"}
        print(sayısozlugu)
        print(sayiguncel)
        sayısozlugu.update(sayiguncel)
        print(sayısozlugu)
        # hafızada aynı yerde bulanan veri birinde olan değişiklik diğerinide etkiler
        sayısozlugu2=sayiguncel#= operator ile yapılırsa aynı yere işlenirler
        sayısozlugu2["6"]="ALTI"
        print(sayısozlugu)
        print(sayısozlugu2)
        print(id(sayısozlugu))
        print(id(sayısozlugu2))
        sayısozlugu3=sayısozlugu.copy()
        sayısozlugu3["8"]="SEKİZ"
        print(sayısozlugu)
        print(sayısozlugu3)
        print(id(sayısozlugu))
        print(id(sayısozlugu3))

        sayısozlugu.clear()#elemanları siler başlığı kalır
        print(sayısozlugu)
        print(sayısozlugu2)
        print(sayısozlugu3)

        del sayısozlugu #silme işlemi böyle kullanılır
onuc()