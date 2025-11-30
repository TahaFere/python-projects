def kirkiki():
        #Random modülü
        #rastgele sayı üretmek için bazı nitelik ve fonksiyonları içerisinde bulunduran modül.
        import random

        #random() fonksiyonu 0 ile 1 arasında rastgele ondalıklı üretmimizi sağlar
        print(random.random())
        print("--")
        #uniform() fonksiyonu kendi belirledyeceğimiz aralıklar arasında rastgele ondalıklı sayı üretmemizi sağlar.
        print(random.uniform(0.5,2.5))
        print("--")
        #randint() fonksiyonu kendi belirleyeceğimz tam sayılar üretmemizi sağlar
        print(random.randint(1,100))
        print("--")
        #randrange() fonksiyonu kendi belirleceğimiz aralıkta sayılar üretmemizi sağlar
        print(random.randrange(50))
        print(random.randrange(25,75))
        print("--")
        #choice() fonksiyonu verdiğimiz bir listeden rastgele eleman seçimlerini sağlar.
        liste=["c","c++","phthon","ruby","java"]
        print(random.choice(liste))
        print(random.choice([i for i in range(35)]))
        print("--")
        #shuffle() fonksiyonu verdiğimiz bir listenin karıştırılmasını sağlar
        liste1=[i for i in range(20)]
        print(liste1)
        random.shuffle(liste1)
        print(liste1)
        print("--")
        #sample() fonksiyonu verdiğimiz bir liste ve eleman sayısına göre rastgele bir alt liste oluşturulmasını sağlar
        print(liste)
        print(liste1)
        print(random.sample(liste,3))
        print(random.sample(liste1,8))

kirkiki()
    