    #public üyüler: sınıf dışından direkt olarak erişilebildiğimiz nitelikli ve metotlar public üyeler olarak adlandırılır.
    #private üyler: sınıf dışındna direkt olarak erişemediğimiz nitelikli ve metotlar private üyeler olarak adlandırılır.
    #semi-private: sınıf dışından direkt olarak erişebildiğimiz ancak sınıf dışında bu öğeyi değiştirmememiz gereken nitelik ve metotlar 
    #semi-private üyeler olarak adlandırılır.
def yirmiyedi():
        class orneksinif:
            publicuye="publicüye"
            __privateuye="privateüye"
            _semiprivateuye="semiprivateüye"

        print(orneksinif.publicuye)#public üyelere sınıf dışından erişilebilir
        #print(orneksinif.__privateuye)#private üyelere sınıf dışından erişilemez. bu hata verir
        print(orneksinif._semiprivateuye)#semi-private üyelere sınıf dışından erişilebilir ancak bu önerilmez

        uye=orneksinif()
        print(uye._orneksinif__privateuye)#dolaylı yoldan private üyelere erişilebilir         


yirmiyedi()