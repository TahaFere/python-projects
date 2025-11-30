def yirmiüc():
        #NESNE TABANLI PROGLAMLAMA
        #-----KAPSÜLLEME
        #bir nesnenin metotlarını ve bilgilerini diğer nesnelerden saklayarak ve bunlara erişimini 
        #sınırlandırarak yanlış kullanımlardan koruyan bir konsepttir.
        #-----MİRAS
        #bir sınıfta başka bir sınıf oluştururken aralarında alt-üst hiyerarşisi oluşturmak ve bu sınıflar arasında ortak yapılar oluşturmak için kullanılır
        #-----ÇOK BİÇİMLİLİK
        #bir metodun bir çok nesne tarafından kullanılması anlamına gelmektedir.
        #-----SOYUTLAMA
        #gereksiz karmaşıklığın gizlenerek oluşturulan nesnelerin sadece gerekli kısımlarını yazılımın diğer kısımlarına sunulması işlemidir.

        #class deneme(): class deneme: buda olabilir. İkiside sınıf tanımlaması

        class ogrenci0():#bunu sınıftan oluşturulacak bütün nesneler aynı bilgileri içericektir bu bir YANLIŞ tanım olur
            adi="TAHA"
            soyadi="FERE"
            dersleri=["matematik","türkçe","fizik"]
        print(ogrenci0.adi)
        print(ogrenci0.soyadi)
        print(ogrenci0.dersleri)

        class ogrenci1():
            adi=""
            soyadi=""
            dersleri=[]
        ogrenci001=ogrenci1()
        ogrenci002=ogrenci1()
        
        ogrenci001.adi="TAHA"
        ogrenci001.soyadi="FERE"
        ogrenci001.dersleri.append("fizik")#burda nesneye eklenen diğer nesneyide etkiledi

        ogrenci002.adi="FATMANUR"
        ogrenci002.soyadi="TİLAVER"

        print("---------------")
        print(ogrenci001.adi)
        print(ogrenci001.soyadi)
        print(ogrenci001.dersleri)
        print("---------------")
        print(ogrenci002.adi)
        print(ogrenci002.soyadi)
        print("---------------")
        print(ogrenci001.dersleri)
        print(ogrenci002.dersleri)


        print("----------------------")

        #--------NESNE NİTELİKLERİ
        #şimdi de her nesnenin kendine ait niteliklerin belirlenmesi

        #----Init(self) fonksiyonu ve Constructor(yapıcı) kavramı
        #Inıt fonksiyonu Pythpn içersinde tanımlanmmış özel bir fonksiyondur, bir sınıftan nesne tanımladığımız zaman gerekli nitelikleri
        #tanımlamak ve yapılacak işlemleri gerçekleştirmek için kullanılır.
        #---UYARI---
        #init metodundan önce bir de new mwtodu çalışır ve sınıfı inşa etmek için kullanılır ancak biz kodlarımızda buna çok fazla yer
        #vermeyeceğiz.
        #---DİKKAT---
        #fonksiyonun ilk parametresi her zaman self olmak zorundadır!!! buradaki self anahtar kelimesi, nesneyi temsil eder gibi düşünebilirsiniz!!

        class Ogrenci:
            #ogrenciAd="" bu sınıf niteliği
            def __init__(self):
                self.ogrenciAd="" #nesnenin niteliği
                print("öğrenci adı:",self.ogrenciAd)
        ogrenci=Ogrenci()
        ogrenci.ogrenciAd="TAHA"
        print(ogrenci.ogrenciAd)
        print("---------------------")
        class Ogrenci2:
            def __init__(self, isim, soyisim, dersler):
                self.ogrenciad = isim
                self.ogrencisoyadi = soyisim
                self.ogrencidersleri = dersler
                print("Öğrenci Adı:", self.ogrenciad)
                print("Öğrenci Soyadı:", self.ogrencisoyadi)
                print("Öğrenci Dersleri:", self.ogrencidersleri)    

        ogrenci1 = Ogrenci2("FATMANUR", "TİLAVER", ["matematik", "fizik"])
        ogrenci2 = Ogrenci2("TAHA", "FERE", ["türkçe", "kimya"])
yirmiüc()
