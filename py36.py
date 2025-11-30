def otuzalti():
        #normal fonksiyonlardan farklı olarka geriye bir iterator dönen fonksiyonlardır.
        #generator fonksiyonlar, return ifadesi yerine kullanılacak en az 1 yield ifadesi içermelidir.
        #iter, next() ve StopIteration yapısını otomatik olarak oluştururlar.
        def deger_arttir():
            sayi=0
            yield sayi#birinci eleman kazandırıldı

            sayi+=1
            yield sayi

            sayi+=1
            yield sayi

        deger_arttir_iter=deger_arttir()
        print(deger_arttir_iter)
        print(next(deger_arttir_iter))
        print(next(deger_arttir_iter))
        print(next(deger_arttir_iter))

        while True:
            try:
                print(next(deger_arttir_iter))
            except :
                print("Generator tamamlandı.")
                break

        def kup_yazdir():
            sayiListesi=[i**3 for i in range(50)]
            for i,j in enumerate(sayiListesi):
                yield "{}^3:{}".format(i,j)
        
        kup_yazdir_Iter=kup_yazdir()
        print(kup_yazdir_Iter)

        for i in kup_yazdir_Iter:
            print(i)


        sayiListesi=[i for i in range(20)]
        print(sayiListesi)

        generator=(i for i in range(20))
        print(generator)#generator objesinin nerde olduğunu gösterir    

        for i in generator:# generator objesinden tek tek elemanlarına ulaşmış olduk.
            print(i)


otuzalti()
