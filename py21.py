#bir dosyadan okuduğumuz tüm harfleri ikinci bir dosayaya büyük harfe çevirerek aktarma yap
def yirmibir():
        dosya=open("deneme1.txt",mode="r")
        dosya1=open("deneme2.txt",mode="w")
        icerik=dosya.read()
        dosya1.write(icerik.upper())
        #tumsatir=dosya.readlines()
        #for satir in tumsatir:
        #    dosya1.write(satir.upper())
        dosya.close()
        dosya1.close()


    #bir dosyada okuma yaparak dosyadaki kelime sayısını hesaplamasını yap
        dosya=open("deneme1.txt",mode="r")
        kelime=dosya.read()
        kelimelistesi=kelime.split(" ")
        #kelimesay=1
        #for bosluk in kelime:
        #    if bosluk==" ":
        #        kelimesay+=1
        print("deneme1.txt dosaysında {} kelime vardır.".format(len(kelimelistesi)))
        dosya.close()
        dosya1.close()



    #bir dosyada okuduğumuz tüm cümlelerin ilk harfini ikinci bir dosyaya büyük harfe çevirerek at 
        dosya=open("deneme1.txt","r")
        dosya1=open("deneme3.txt","w")
        sozcuk=dosya.read()
        sozcuk1=sozcuk.split(".")
        for cumle in sozcuk1:
            cumle+="."
            dosya1.write(cumle.capitalize())
        dosya1.close()
        dosya.close()


    #okuma yapacağınız dosya içerisinde her öğrencinin adı, soyadı, vize ve final notları bulunacak. Bu dosyadan okuduğumuz bilgilerle ikinci
    #bir dosyaya öğrenci adı, soyadı, harf notu ve dersten geçme-kalma bilgisi yazdıracaksınız. Harf notlarının aralığını kendiniz belirleyebilirsiniz.

        dosya=open("ogrenci.txt","r")
        dosya1=open("ogrenci1.txt","w")
        satir=dosya.readlines()
        geckal=str()
        puan=0
        for i in satir:
            satirici=i.split(" ")
            vize=int(satirici[2])
            final=int(satirici[3])
            puan=(vize*0.4)+(final*0.6)
            if puan<=100 and puan>75:
                harf="a"
            elif puan<75 and puan>55:
                harf="b"
            elif puan<55 and puan>45:
                harf="c"
            elif puan<45 and puan>35:
                harf="d"
            elif puan<35:
                harf="f"    
            if(puan>70):
                geckal="gecti"
            else:
                geckal="kaldi"
            dosya1.write(satirici[0])
            dosya1.write("\t")
            dosya1.write(satirici[1])
            dosya1.write("\t")
            dosya1.write(harf)
            dosya1.write("\t")
            dosya1.write(geckal)
            dosya1.write("\n")
yirmibir()
