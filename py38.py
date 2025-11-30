def otuzsekiz():
        b=int(input("38 içinde hangi kodu çalıştırmak istersiniz? (1):"))
        if(b==1):
            import python.modül_dosya as md#kendi oluşturduğumuz modül dosyasını md takma ismi ile dahil ettik
            md.bilgileri_yazdir("Taha","Fere","bilgisayar mühendisliği")
            ogrenci1=md.Ogrenci("FATMANUR","TİLAVER","bilgisayar mühendisliği")
            ogrenci1.bilgileri_yazdir()
            ogrenci2=md.Ogrenci("TAHA","FERE","makine mühendisliği")
            ogrenci2.bilgileri_yazdir()
        
        if(b==2):
            import os 
            #name niteliği işletim sisteminin adını verir
            #işletim sistemi windows ise 'nt', MacOs ve linux ise 'posix' çıktısını verir
            print("işletim sistemi adı:",os.name)

            #sep niteliği dosya yollarında kullanılan ayırıcı karakteri verir
            #işletim sistemi windows ise '\' , MacOs ve linux ise '/' çıktısını verir
            print("dosya yolu ayırıcı karakter:",os.sep)

            #curdir niteliği geçerli dizini temsil eden karakteri dizisini verir
            #işletim sistemi windows ise '.' , MacOs ve linux ise '.' çıktısını verir
            print("geçerli dizin karakteri:",os.curdir)

            #pardir niteliği geçerli dizinin üst dizini temsil eden karakteri dizisini verir
            #işletim sistemi windows ise '..' , MacOs ve linux ise '..' çıktısını verir
            print("üst dizin karakteri:",os.pardir)

            #getcwd() fonksiyonu geçerli çalışma dizinini verir
            print("geçerli çalışma dizini:",os.getcwd())

            #chdir() fonksiyonu geçerli çalışma dizinini değiştirmeye yarar
            os.chdir("C:\\Users\\user\\Desktop")
            print("bulundumuz dizin:",os.getcwd())
            os.chdir("C:\\Users\\user\\Desktop\\code")

            #listdir() fonksiyonu bir dizi içindeki dosya ve klasörleri liste yapısı halinde sunar.
            print(os.listdir())
            for directory in os.listdir():
                print(directory)

            #startfile() fonksiyonu içerisine verdiğimiz dosya ismine göre dosyayı veya klasörü açmayı sağlar
            os.startfile('filmlist.txt')
            os.startfile('.')
            os.startfile('..')
        
            #mkdir() fonksiyonu içerisinine verdiğimiz dosya yolu ve dosya ismine göre yeni dizini oluşturmayı sağlar
            os.mkdir(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')

            #makedirs() fonksiyonu içerisine verdiğimiz dosya yolu ve dosya ismnine göre iç içe yeni dizini oluşturmayı sağlar
            os.makedirs(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu\\osmodülüoluştu2')

            #rename() fonksiyonu dizinlerin veya dosyaların adlarını değiştirmemizi sağlar
            os.rename("ornek.txt","ornekkk.txt")

            #remove() fonksiyonu dizinleri veya dosyaları silmemizi sağlar
            os.remove("boom.txt")

            #rdir() fonksiyonu içi boş olan bir dizini silmek için kullanılır, içinde dosya varsa hata verir
            os.rmdir(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu\\osmodülüoluştu2')
            os.rmdir(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')

            #removedirs fonksiyonu içi boş olan dizinleri silmek için kullanılır
            os.makedirs(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu\\osmodülüoluştu2')            
            os.removedirs(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')

            #path.abspath() fonksiyonu içerisine verdiğimiz dosyanın tam yolunu verir
            os.path.abspath("deneme1.txt")

            #path.dirname() fonksiyonu içerisine verdiğimiz bir dosya yolunun dizin kısmını verir
            os.path.dirname(os.path.abspath("deneme1.txt"))

            #path.exists fonksiyonu içerisine verdiğimiz dosya veya dizinin olup olmadığını inceler
            os.path.exists(os.path.abspath("deneme1.txt"))
            os.path.exists(os.path.abspath("deneme10.txt"))

            #path.isdir() fonksiyonu içerisine verdiğimiz parametrenin bir dizin olup olmadığını kontrol eder
            os.makedirs(r'C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')
            os.path.isdir('C:\\Users\\user\\Desktop\\code\\osmodülileoluştu')            

            #path.isfile() fonksiyonu içerisine verdiğimiz parametrenin bir dosya olup olmadığını kontrol eder
            os.path.isfile('C:\\Users\\user\\Desktop\\code\\deneme01.txt')

            #path.join() fonksiyonu verilen parametleler ile bir dosya yolu oluşturu
            os.path.join("taha","fatmanur")

            #path.split() fonksiyonu verilen dosya yolunun son kısmını ayırır
            os.path.split('C:\\Users\\user\\Desktop\\code\\deneme01.txt')

            #path.splitext() fonksiyonu verilen dosyanın uzantısı ve ismini birbirinden ayırı
            os.path.splitext('deneme01.txt')

otuzsekiz()
