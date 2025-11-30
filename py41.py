def kirkbir():
        #Time Modülü
        #saat işlemleriyle ilgili faydalı nitelik ve fonksiyonların bulunduğu modüldür
        import time

        #gmtime() fonksiyonu başlangıç zamanın (EPOCH), struct yapısı şeklinde bize verir ve tm_year, tm_mont, tm_day, 
        #tm_sec, tm_wday, tm_yday nitelikleri vardır.
        epoch=time.gmtime(0)
        print(epoch)
        print(epoch.tm_year)

        #time() fonksiyonu başlangıçta(EPOCH) o ana kadar geçen toplam süreyi saniye cinsinden verir.
        print(time.time())

        #localtime() fonksiyonu yerel saat bilgisini, struct yapısı şeklinde bize verir ve m_year, tm_month, tm_day,
        #tm_sec, tm_wday, tm_yday nitelikleri vardır.
        print(time.localtime())

        #sleep() fonkisyonu yazdığıöız kodların belirli bir süre durmasını, uyumasını sağlar.  
        print("birazdan sleep çalışıcak ve program uyucak")
        time.sleep(5)
        print("az önce sleep çalıştı ve uyudum")


kirkbir()
