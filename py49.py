def kırkdokuz():
        #numpy
        #python hazır olarak sunulmuş olan liste yapısından efektir olarak çalışır;hem daha hızlı hemde daha az belek gereksinimi vardrır.
        #veri analiz işlemlerindeki matematiksel hesaplamalar için kullanılır

        #numpy array ı nasıl kullanırız
        #1.direkt liste tanımlar gibi tanımlayabiliriz.
        #2.zeros() fonksiyonu ile tüm elemanları 0 olan dizi tanomlayabiliriz.
        #3.ones() fonksiyonu ile tüm elemanları 1 olan dizi tanımlayabiliriz.
        #4.full() fonksiyonu ile tüm elemanları aynı olan dizi tanımlayabiliriz.
        #5.arange() fonksiyonu ile belirli aralıkta, eleman sayısına göre sabit bir artış ile dizi tanımlayabiliriz.
        #6.linspace() fonkisyonu ile belirli aralıkta, eleman sayısına göre sabit bir artış ile dizi tanımlayabiliriz.
        #7.randint() fonksiyonu ile belirli aralıkta rastgele eleman üreterek dizi tanımlayabiliriz.
        import numpy as np

        npArrayList=np.array([1,2,3,4,5])
        print(type(npArrayList))
        print(npArrayList)

        npZerosList=np.zeros(5,dtype="int")
        print(type(npZerosList))
        print(npZerosList)

        npZerosList2D=np.zeros((5,5))#data type belirmeyince default olarak float oluyor
        print(type(npZerosList2D))
        print(npZerosList2D)

        npOnesArray=np.ones(5,dtype="int")
        print(type(npOnesArray))
        print(npOnesArray)

        npOnesArray2D=np.ones((5,5),dtype="int")
        print(type(npOnesArray2D))
        print(npOnesArray2D)

        npFullArray=np.full((5,5),5)
        print(type(npFullArray))
        print(npFullArray)

        npArangeArray=np.arange(0,50,5)#(başlangıç,bitiş,artış) değerleri sırasıyla girilir bitiş değer çıktıya dağil edilmez
        print(type(npArangeArray))
        print(npArangeArray)

        npLinspaceArray=np.linspace(0,50,10)#(başlangıç,bitiş,kaç_eleman_istiyorsak) veriler girilir
        print(type(npLinspaceArray))
        print(npLinspaceArray)
        
        npRandintArray=np.random.randint(0,50,(5,5))#(başlangıç,bitiş,kaç_eleman)
        print(type(npRandintArray))
        print(npRandintArray)
        print("*****")

        #numpy array bilgileri
        #1.dtype: arraydeki elemanların veri tipi
        #2.size:arraydeki toplam eleman sayısı
        #3.ndim: arrayin boyut sayısını
        #4.shape: arrayin satır-sütun bilgisi
        npArray=np.array([1,2,3,4,5])
        print(npArray)
        print(npArray.dtype)
        print(npArray.size)
        print(npArray.ndim)
        print(npArray.shape)#bunu çıktısı (5,) olucak bu da sadece tek satır olduğu için sütün bilgisi olmadığı için yazmadı

        npArray2D=np.random.randint(2,34,(6,8))
        print(npArray2D)
        print(npArray2D.dtype)
        print(npArray2D.size)
        print(npArray2D.ndim)
        print(npArray2D.shape)

        #array elemanlarına erişmek
        #1.index yardımıyla elemanlara erişmek
        #2.parçalama yardımıyla eleman alt kümelerine erişmek
        print(npArray)
        print(npArray[0])
        print(npArray[4])
        npArray[0]=0
        print(npArray)
        print("*****")
        print(npArray2D)
        print(npArray2D[0])#girilen satırı yazdırır
        print(npArray2D[1])#girilen satırı yazdırır
        print("*****")
        print(npArray2D[1][1])
        print(npArray2D[3][2])
        npArray2D[4][2]=45
        print(npArray2D)

        #parçalama yardımıyla eleman alt kümelerine erişmek array_isim(basalnagıc_indeks:indeks_artıs_miktarı)
        nparray=np.arange(0,50)
        print(nparray)
        print(nparray[::])
        print(nparray[0:-1:1])
        print(nparray[::5])
        print(nparray[:15:5])
        print(nparray[15::5])
        print("*****")
        print(npArray2D)
        print(npArray2D[::,::])#(satır kısmı,sütün kısmı)
        print(npArray2D[0::2,::])
        print(npArray2D[::,1::2])
        print(npArray2D[1::2,1::2])
        print("*****")
        #hazır Foksiyonlar
        #1.reshape(): numpy arrayı yeniden boyutlandırmak için kullanılır.
        #2.concatenate(): Numpy arraylari birleştirmek için kullanılır.
        #3.split(): numpy arrayı bölmek-ayırmak için kullanılır.
        #4.sort(): numpy arrayi sıralamak için kullanılır.
        nparray=np.arange(1,10)
        print(nparray)
        nparray2D=nparray.reshape((3,3))#yeniden boyutlandırıken elimizde ki veri sayısana dikkat edilmeli 
        print(nparray2D)
        nparray2D=nparray.reshape((9,1))
        print(nparray2D)
        a=np.arange(0,10)
        b=np.arange(10,20)
        c=np.concatenate([a,b])
        print(a)
        print(b)
        print(c)
        c=np.concatenate([b,a])
        print(c)
        a=np.array([[1,2,3,4,5],[1,2,3,4,5]])
        b=np.array([[6,7,8,9,10],[6,7,8,9,10]])
        print(a)
        print(b)
        c=np.concatenate([a,b])
        d=np.concatenate([a,b],axis=1)#a ilk satır b ilk satır,a ikinci satır ,b ikinci satır şeklinde birleştirildi
        print(c)
        print(d)
        print(nparray)
        a,b,c=np.split(nparray,3)
        print(a)
        print(b)
        print(c)
        print(npArray2D)
        a,b=np.vsplit(npArray2D,[2])
        print(a)
        print(b)
        c,d=np.hsplit(npArray2D,[2])
        print(c)
        print(d)
        randomarray=np.random.randint(0,50,(1,10))
        print(randomarray)
        sortedArray=np.sort(randomarray)
        print(sortedArray)
        randomarray=np.random.randint(0,50,(2,10))
        print(randomarray)
        sortedArray=np.sort(randomarray)
        print(sortedArray)
        randomarray=np.random.randint(0,50,(5,10))
        print(randomarray)
        sortedArray=np.sort(randomarray,axis=0)#sütuna göre sıralama yapıldı
        print(sortedArray)
        print("*********")

kırkdokuz()