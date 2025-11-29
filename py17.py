def onyedi():
        #--------------------- HAZIR STRİNG KOMUTLARI--------------------

        strging="       HAVA savunma ASTSUBAY astçavuş Taha Fere Kalkan 2 Kısım komutanı         \t\t"
        #replace() komutu: Bir string içerisindeki belirli bir karakter veya karakterleri değiştirmek için kullanılır
        strging2=strging.replace("a","*")
        strging3=strging.replace("savunma","*")
        strging4=strging.replace("a","*",6)
        print(strging.replace("a","*"))
        print(strging2)
        print(strging3)
        print(strging4)

        #upper() komutu: Tüm karakterleri büyük harfe çevirmek için kullanılır.
        #lower() komutu: Tüm karakterleri küçük harfe çevirmek için kullanılır.
        print(strging.upper())
        print(strging.lower())

        #capitalize() komutu: Stringin sadece ilk harfini büyük harfe çevirmek için kullanılır.
        #title() komutu: Her kelimenin ilk harfini büyük harfe çevirmek için kullanılır
        #swapcase() komutu: Stringteki tüm büyük harfleri küçük harfe, küçük harfleri de büyük harfe çevirmek için kullanılır.
        print(strging.capitalize())
        print(strging.title())
        print(strging.swapcase())

        #strip() komutu: Bir stringteki "\n"," ","\t","\v" karakterlerinden kurtulmak için kullanılır.
        #lstrip() komutu: Bir stringin solundaki "\n"," ","\t","\v" karakterlerinden kurtulmak için kullanılır.
        #rstrip() komutu: Bir stringin sağındaki "\n"," ","\t","\v" karakterlerinden kurtulmak için kullanılır.
        print(strging.strip(),len(strging.strip()))
        print(strging.lstrip(),len(strging.lstrip()))
        print(strging.rstrip(),len(strging.rstrip()))  

        #startswith() komutu: Bir string verilen karakter veya karakterler ile başlayıp başlamadığını sorgulamak için kullanılır.
        #endswith() komutu: Bir string verilen karakter veya karakterler ile bitip bitmediğini sorgulamak için kullanılır.
        print(strging.startswith("HAVA"))
        print(strging.startswith("   "))
        print(strging.endswith("\t"))
        print(strging.endswith("komutanı"))
onyedi()
