def otuzdokuz():
        #SYS MODÜLÜ
        import sys
        #kullandığımız Python sürümü ile ilgili bilgi edinmemizi ve kullandığımız Python ile çeşitli işlemler yapabilmemizi sağlar
        
        #argv niteliği program çalışırken kullanılan parametreleri bir liste halinde tutar
        print(sys.argv)

        #executable niteliği pythonın çalıştırabilir dosyanın adını ve yolunu öğrenmek için kullanılır
        print(sys.executable)

        #platform niteliği kodlarımızın çalıştığı işletim sistemi hakkında bilgi almak için kullnılır.
        #GNU/linux :linux çıktısı    windows: win32 çıktısı       mac os: darvin çıktısı
        print(sys.platform)

        #version niteliği python sürümü öğrenmek için kullanılır
        print(sys.version)

        #exit() fonksiyonu program akışını sonlandırmak için kullanılır
        #sys.exit()

        #Standart Komutlar
        #çıktı vermek için ve kullanıcıdan değer almak için aşağıdaki standart komutlar kullanılır.
        #1-Standart çıktı konumu - stdout
        #2-Standart hata konumu - stderr
        #3-standart girdi konumu - stdin
        sys.stderr.write("HATA\n")
        sys.stdout.write("Normal\n")


otuzdokuz()
