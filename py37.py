def otuzyedi():
        # MODÜLLER
        #pythonda yazdığımız her bir farklı dosya bir modül olarak kabul edilir. modüller içerisinde yazdığımız fonksiyonlar, sınıflar
        # daha sonra başka programlarda veya aynı programın farklı yerinde çağırılabilir ve kullanabiliriz
        #Import ifadesi ile modüller program içerisine dahil edilir.
        import math # matematik modülünü py dosyasına dahil ettik
        import time # zaman modülünü py dosyasına dahil ettik
        import os # işletim sistemi modülünü py dosyasına dahil ettik
        import random # rastgele sayı modülünü py dosyasına dahil ettik
        import sys # sistem modülünü py dosyasına dahil ettik

        from os import name #os modülünden sadece name özelliğini dahil ettik
        name # çıktısı nt olur bu çıktı windows işletim sistemi olduğu için


        #from os import * #os modülündeki tüm özellikleri dahil ettik

        import math as matematik #math modülüne matematik ismini takma isim olarak verdik
        matematik.sqrt(16) #math modülündeki sqrt fonksiyonunu matematik takma ismi ile kullandık
        import os as isletimSistemi #os modülüne isletimSistemi ismini takma isim olarak verdik
        import sys as sistem #sys modülüne sistem ismini takma isim olarak verdik
        

        dir(matematik) #math modülündeki tüm fonksiyon ve özellikleri listeledik
        help(matematik.sqrt) #math modülündeki sqrt fonksiyonunun ne işe yaradığını gösterir
        dir(isletimSistemi) #os modülündeki tüm fonksiyon ve özellikleri listeledik
        dir(sistem) #sys modülündeki tüm fonksiyon ve özellikleri listeledik
        help(matematik)#math modülünün içindeki fonksiyon ve özelliklerin ne işe yaradığını gösterir
        help(isletimSistemi)#os modülünün içindeki fonksiyon ve özelliklerin ne işe yaradığını gösterir
        help(sistem)#sys modülünün içindeki fonksiyon ve özelliklerin ne işe yaradığını gösterir

otuzyedi()
