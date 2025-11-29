def ondokuz():
        try:
            a=int(input("1.sayıyı giriniz="))
            b=int(input("2.sayıyı giriniz="))
            print(a/b)
        except:
            print("hatalı değer girişi.....")
        print("---------------------------------------")

        try:
            a=int(input("1.sayıyı giriniz="))
            b=int(input("2.sayıyı giriniz="))
            print(a/b)
        except ValueError:#boş değerler hatalı girişlerde
            print("hatalı değer girişi.....")
        except ZeroDivisionError:#sıfır bölüm hatası
            print("ikinci sayı 0 olmaz!....")
        except TypeError:#giriş hatası
            print("sayı girişi yapınız....")
        except:#genel beklenmedik hata oluşmasına karşı aç.....
            print("bir hata meydana geldi....")  

        print("---------------------------------------------")
        try:
            a=int(input("1.sayıyı giriniz="))
            b=int(input("2.sayıyı giriniz="))
            print(a/b)
        except TypeError:#giriş hatası
            print("sayı girişi yapınız....")
        except ValueError:#boş değerler hatalı girişlerde
            print("hatalı değer girişi.....")
        except ZeroDivisionError:#sıfır bölüm hatası
            print("ikinci sayı 0 olmaz!....")
        except:#genel beklenmedik hata oluşmasına karşı aç.....
            print("bir hata meydana geldi....")        
        finally:
            print("program sonlanıyor...")

        print("------------------------------------------------")

        sayi1=int(input("lütfen pozitif sayı giriniz"))
        if sayi1<0:
           pass# raise Exception("girilen sayı negatif olamaz")
        try:
            sayi2=int(input("lütfen pozitif sayı giriniz"))
            if sayi2<0:
                raise ValueError("girilen sayı negatif olamaz")
        except ValueError:
            print("GİRİLEN SAYI NEGATİF OLAMAZ")
        
        print("-------------------------------------------")

        sayi1=int(input("lütfen pozitif sayı giriniz"))
        assert sayi1>0, "sayı negaatif olamaz"

        try:
            sayi1=int(input("lütfen pozitif sayı giriniz"))
            assert sayi1>0, "sayı negaatif olamaz"
        except:
            print("SAYI NEGATİF OLAMAZ")
        try:
            sayi1=int(input("lütfen pozitif sayı giriniz"))
            assert sayi1>0
        except AssertionError:
            print("SAYI NEGATİF OLAMAZ")
        except ValueError:
            print("SAYI GİRMELİSİNİZ")
ondokuz()
