def yedi():
        print("-----------DÖNGÜLER-----------")
        print("while döngüsü")
        i=0
        print("döngü başlıyor...")
        while(i<10):
            print(i,end=" ")
            i+=1
        print("\ndöngü sonlandı...")
        print("-----------------------")
        i=0
        j=5
        print("döngü başlıyor....")
        while(i<10 and j<10):
            print(i)
            i+=1
            j+=1
        print("\ndöngü sonlandı")
        print("-----------------------")

        print("for döngüsü")
        str1="kalkan2kısımkomutanı"
        for ch in str1:
            print(ch,end=" ")
        print("-----------------------")
        elemanlistesi=[1,2,3,4,5,6,7]
        for eleman in elemanlistesi:
            print(eleman,end=" ")
        print("-----------------------")
        print("range fonksiyonu")
        for sayi in range(100):
            print(sayi,end=" ")
        print("\n-----------------------")
        for sayi in range(50,100):
            print(sayi,end=" ")
        print("\n-----------------------")
        for sayi in range(10,50,5):
            print(sayi,end=" ")
        print("\n---------------------")
        print("BREAK, CANTİNUE VE PASS KOMUTLARI")
        i=0
        while(True):
            print(i,end=" ")
            if(i>=50):
                break
            i+=2
        print("\n---------------------")
        for i in range(100):
            if(i%5!=0):
                continue#çalıştığında alt satırlar çalışmıyor başa dönüyor.....
            print(i,end=" ")
        print("\n---------------------")
        for i in range(100):
            if(i%5!=0):
                pass#hata almamak veya boşluk bıraakılacak yerler yazılır.......
            print(i,end=" ")
        print("\n---------------------")
yedi()