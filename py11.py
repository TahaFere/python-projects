import random
def onbir():
        print("----------LİSTELER--------------")
        liste=list()
        liste1=[]
        print(liste,type(liste),liste1,type(liste1))
        print("\n----------------------------")
        liste2=[1,2,3,4,5]
        print(liste2,type(liste2))
        print("\n----------------------------")
        liste3=["kalkan","2","kısım","kkomutanı"]
        print(liste3,type(liste3))
        print("\n----------------------------")
        liste4=["kalkan",2,"kısım",4,"komutanı",True,3.5]
        print(liste4,type(liste4))
        print("\n----------------------------")
        print(liste3[0],"\t",liste3[2],"\t",liste2[-1],"\t",liste2[-3])
        print("\n----------------------------")
        for eleman in liste4:
            print(eleman)
        print("\n----------------------------")
        for eleman in liste2:
            print(eleman**3)
        print("\n----------------------------")
        sayeleman=len(liste3)
        print(liste3,"eleman sayısı:",sayeleman)
        print(liste4,"eleman sayısı:",len(liste4))
        print("\n----------------------------")
        for i in range(len(liste4)):
            print(i)
        print("\n----------------------------")
        liste2[0]=6
        liste2[1]=11
        print(liste2)
        for i in range(len(liste2)):
            liste2[i]**=2
        print(liste2)
        print("\n----------------------------")
        liste5=liste2[3:]
        liste6=liste2[:3]
        liste7=liste2[::2]
        liste8=liste2[::-1]
        print(liste5)
        print(liste6)
        print(liste7)
        print(liste8)
        print("\n----------------------------")
        listebirles=liste2+liste4
        print(listebirles)
        print(liste2+liste4)
        print("\n----------------------------")
        liste4+=[89]
        liste4+=["güzellik"]
        print(liste4)
        print("\n----------------------------")
        liste3*=3
        print(liste3)
        print("\n----------------------------")
        #append komutu listenin sonun eleman ekler
        #insert komutu listenin istenilen indeksine ekler
        liste4.append(13)
        liste4.append("bal hatunum")
        liste4.append(False)
        liste4.insert(2,24)
        liste4.insert(0,"güzel fıstığım")
        print("\n----------------------------")
        #remove listeden belirli değeri çıkartır
        #dell listeden belirli indeksi siler yada listeyi komple silememizi sağlar
        #pop komutu listenin sonunda ki yada belirli indeksdeki elemanı silip değişkene atmamızı sağlar
        #listebirles=[36, 121, 9, 16, 25, 'kalkan', 2, 'kısım', 4, 'komutanı', True, 3.5]
        print(listebirles)
        listebirles.remove(2)#sadece 1 tane değeri siler aynı olan diğer değerler kalır
        print(listebirles)
        del(listebirles[1])
        print(listebirles)
        print(listebirles.pop())
        print(listebirles.pop(7))
        print(listebirles)
        print("\n----------------------------")
        #in komutu kullanıldığında listede True yada False döndürür
        #notin de komutuda liste içinde var ise False, yok ise True döndürü
        #index komutu aradığımız elemanın listede varsa kaçıncı indiste olduğunu verir yoksa Value Error verir
        liste=[13,24,62,335,64,345,]
        print(62 in liste)
        print(42 in liste)
        print(13 not in liste)
        print(34 not in liste)
        print(liste.index(64))
        if 46 in liste:
            print(liste.index(23))
        print("-------------------------------")
        #sort komutu: listenin elemanlarını küçükten büyüğe doğru sıralar
        #reverse komutu: Listenin elemanın tersine çevirir, baştaki sona ve sondaki başa gelir.
        liste=[2,44,345,12,34,4575,45,3,3,76,79,3532,57]
        liste.reverse()
        print(liste)
        liste.sort()
        print(liste)
        liste2=["balım","aşkım","hayatım","dünyam","nefesim","bir tanem","güzelliğim","bebeğim"]
        liste2.reverse()
        print(liste2)
        liste2.sort()
        print(liste2)
        print("------------------------------")
        #count komutu: listede bir elemanın kaç defa geçtiğinin sonucu verir (0 verirse eleman yoktur)
        liste=[2,324,35,6,23,3,5,575,3,423,33,54,57,79,5,3,3234,6,56,34,54,3,3,3,2,56445,6,]
        print(liste)
        print(liste.count(3))
        print(liste.count(2))
        print("-------------------------")
        #min komutu listenin en küçük elemanını verir
        #max komutu listenin en büyük elemanını verir
        #sum komutu listedki elemanların toplamını verir
        print(min(liste))
        print(max(liste))
        print(sum(liste))
        print("---------------------")
        liste=[i for i in range(5)]
        liste1=[i for i in range(random.randint(1,10))]
        liste2=[i for i in range(1,10) if i%2==0]
        print(liste)
        print(liste1)
        print(liste2)
onbir()