def kirkyedi():
        # VERİ TABANI YÖNETİMİ (SQLİTE)
        #*neden ihtiyacımız var?
        #veritabanı, verileri kalıcı ve düzenli bir şekilde saklamaızı, verileri güncellememizi-silmemizi sağlayan veri yığınlarıdır.
        #veritabanında veriler satır ve sütün şeklinde saklanır. Her bir sütuna veriyle alakalı hangi verinin nasıl saklanacağı bilgisi yazılır,
        # her bir ayrı veri ise satırlara kaydedilir.
        #*nasıl yöneteceğiz?
        #birçok programlama dilinde veritabanı yönetmek için temel SQL sorguları mevcuttur.biz de python programlama dilinde hazır olarak sunulmuş
        #sqlite kütüphanesini kullanarak SQlL sorguları ile veritabanını yöneteceğiz
        #1.VERİ EKLEME(CREATE)
        #2.VERİ ALMA(READ)
        #3.VERİ GÜNCELLEME(UPDATE)
        #4.VERİ SİLME(DELETE)
        import sqlite3

        #veri tabanı oluşturma-bağlama ve connect() fonksiyonu
        #sqlite3.connect("veritabani_adi.uzanti")
        #buradaki uzantı .sqlite veya .db olabilir, eğerki verdiğiniz isim ile bir veri tabanı yoksa bulunduğunuz dizine bu veritabanı oluşturulur
        #eğer ki varsa bağlantı kurulur.
        veritabani=sqlite3.connect("ogrenci.db")

        #İmleç(cursor) tanımlama
        #oluşturduğumuz veya bağlantı kurduğumuz veri tabanı üzerinde işlme yapabilmemiz için bir cursor(imleç) oluşturmamız gerekiyor.
        #tüm işlemleri de bu imleci kullanarak yapacağız.
        imlec=veritabani.cursor()

        #TABLO OLUŞTURMA, VERİ TİPLERİ
        #tabloları oluştururken yazılacak verilerin veri tiplerin veri tiplerini önceden belirtmemiz gerekiyor, bu veri tipleri;
        #1.INTEGERR: tam sayılar için
        #2.REAL: ondalıklı sayılar için
        #3.TEXT: karakter dizileri için
        #4.BLOB: binay format için kullanılıyor.
        #bir tabloyu oluşturmal için sorgu içerisinde CRATE komutu kullanmamız gerekiyor, syntax yapısı şu şekilde;
        #CRATE TABLE tablo_adi(sutun1,sutun2,sutun3,...)
        #bu komutu çalıştımka için ise oluşturduğumuz imleç ile birlikte execute() fonksiyonunu kullanmamız gerekiyor
        #oluşturmaSorgu="CREATE TABLE ogrenci(ogrenciAdi TEXT,ogrenciSoyadı TEXT,ogrenciNo INTEGER)"
        #imlec.execute(oluşturmaSorgu)

        #aynı tablodan tekar oluşturmaya kalkarsak hata alırız bunu önüne geçmek için ise;
        #IF NOT EXISTS komutu ile engelleyebiliriz; eğerki tablo yok ise anlamına gelir
        sorgu="CREATE TABLE IF NOT EXISTS ogrenci(ogrenciAdi TEXT,ogrenciSoyadı TEXT,ogrenciNo INTEGER)"
        imlec.execute(sorgu)

        #tabloya kayıt ekleme
        #bir tabloya yeni kayıt eklemek aslında yeni bir satır eklemek anlamına geliyor, bunun için de INSERT INTO komutunu kullanıyoruz;
        #INSERT INTO tablo_adi(sutun1,sutun2,sutun3,...) VALUES(deger1,deger2,deger3,...)
        #imleç ile ekleme, güncelleme veya silme yaptıktan sonra bu işlemler geçici bir veri kümesi üzerinde yapılır. Kalıcı olmasını istiyorsanız
        #ve veritabanına yansımasını istiyorsanız commit() koutunu kullanmanız gerekiyor.
        sorgu2="INSERT INTO ogrenci(ogrenciAdi,ogrenciSoyadı,ogrenciNo) VALUES('taha','fere',1)"
        imlec.execute(sorgu2)#geciçi kayıt yazmış olduk (kayıt bir yerde yazılmayı bekliyor)
        veritabani.commit()

        #parametre ile ekleme
        #bazı durumlarda dışarıdan gelen verilere göre ekleme yapmamız gerekebilir. Bu durumlarda VALUES()kısmına ne yazacağız? 
        #bu durumlarda VALUES(?) şeklinde yazarak ardından parametreyi vereceğiz.
        sorgu3="INSERT INTO ogrenci(ogrenciAdi,ogrenciSoyadı,ogrenciNo) VALUES(?,?,?)"
        ogrenciBilgisi=("Fatmanur","Tilaver",2)
        ogrencibilgisi1=("ahmet","toprak",3)
        imlec.execute(sorgu3,ogrenciBilgisi)
        imlec.execute(sorgu3,ogrencibilgisi1)
        veritabani.commit()

        #kayıt listeleme
        #bir tablodaki verileri verilerin bir kısmını görüntülemek, listelemek, almak için SELECT komutu kullanıyoruz, şu şekilde;
        #SELECT sutun1,sutun2,sutun3,... FROM tablo_adi WHERE sorgu_kosulu
        sorgu4="SELECT ogrenciAdi,ogrenciSoyadı,ogrenciNo FROM ogrenci"
        imlec.execute(sorgu4)

        #verilerin görüntülenmesi
        #SELECT komutuyla verileri alabileceğimizi-listeleyebileceğimiz az önce görmüştük, peki bu verileri nasıl alacağız? nasıl görüntüleceğiz
        #1.FETCHALL: SELECT ile getirilen tüm verileri almak için kullanılır
        #2.FETCHONE: SELECT ile getirilen tek bir satır veriyi okumak için kullanılır, her çağrıldığında bir sonraki satır okunur
        #3.FETCHMANY: SELECT ile getirilen verilerden istediğimiz kadar satır okumak için kullanılır.
        imlec.execute(sorgu4)
        print(imlec.fetchall())
        print("********")

        imlec.execute(sorgu4)
        print(imlec.fetchone())
        print(imlec.fetchone())
        print(imlec.fetchone())
        print("********")

        imlec.execute(sorgu4)
        for ogrenci in imlec:
            print(ogrenci[0])
            print(ogrenci[1])
            print(ogrenci[2])
        print("********")

        imlec.execute(sorgu4)
        print(imlec.fetchmany(3))
        print("********")    

        #imleç üzerinden veri okuma 
        #fonlsiyon kullanmadan olarak SELECT  ile getirilen verileri imlec üzerinden okuyabiliriz
        sorgu4="SELECT ogrenciAdi,ogrenciSoyadı,ogrenciNo FROM ogrenci WHERE ogrenciAdi='taha'"
        imlec.execute(sorgu4)
        for ogrenci in imlec:
            print((ogrenci[0]),(ogrenci[1]),(ogrenci[2]))
        print("********")

        #kayıt güncelleme
        #bir tablodaki verileri güncellemk istiyorsak UPDATE komutunu kullanıyoruz, şu şekilde;
        #UPDATE tablo_adi SET sutun1=yeni_değer,sutun2=yeni_değer....
        sorgu5="UPDATE ogrenci SET ogrenciAdi='ahmet',ogrenciSoyadı='toprak',ogrenciNo=3"
        #imlec.execute(sorgu5)
        veritabani.commit()

        #dikkat
        #eğer ki spesifik bir sorguya göre güncelleme yapmazsanız tüm satırları etkiler
        #peki nasıl koşul ekleyeceğiz? WHERE komutu ile sorgulamalar yapabiliriz
        sorgu5="UPDATE ogrenci SET ogrenciAdi='taha',ogrenciSoyadı='toprak',ogrenciNo=3 "
        #imlec.execute(sorgu5)
        veritabani.commit()

        sorgu5="UPDATE ogrenci SET ogrenciAdi='taha',ogrenciSoyadı='toprak',ogrenciNo=3 Where ogrenciAdi='ahmet'"
        imlec.execute(sorgu5)
        veritabani.commit()
        imlec.execute(sorgu4)
        print(imlec.fetchmany(3))
        print("********")   

        #kayıt silme
        #bir tdan veri silmek istiyorsak DELETE FROM komutunu kullanıyoruz, şu şekilde;
        #DELETE FROM tablo_adi WHERE silme_koşulu
        sorgu6="DELETE FROM ogrenci WHERE ogrenciAdi='ahmet'"
        imlec.execute(sorgu6)
        veritabani.commit()



        #veri tabanı Bağlantı kesilmesi 
        #veri tabanı üerindeki işlemleri yaptıktan sonra veritabanı baplantısını close() fonksiyonu ile kesmemiz gerekiyor
        veritabani.close()

kirkyedi()
