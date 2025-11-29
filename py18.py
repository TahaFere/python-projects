def onsekiz():
        #zip fonksiyonu iki veya daha fazla listeyi, sözlüğü birleştirip tek bir zip objesi elde edebildiğimiz fonsiyondur
        liste1=[i for i in range(10)]
        liste2=[j for j in range(10,20)]
        liste3=zip(liste1,liste2)
        print(liste1)
        print(liste2)
        print(liste3)
        print(list(zip(liste1,liste2)))
        for i,j in liste3:
            print("ilk liste değerleri={}, ikinci liste değerleri={}".format(i,j))
        liste4=[k for k in range(20,30)]
        liste5=zip(liste1,liste2,liste4)
        for i,j,k in liste5:
            print("ilk liste değerleri={}, ikinci liste değerleri={}, üçüncü liste değerleri={}".format(i,j,k))

        listestr1=[i for i in range((5))]
        listestr2=['A','B','C','D','E']

        for i,j in zip(listestr1,listestr2):
            print(i,j)
        
        sozluk1={"A":1,"B":2,"C":3}
        sozluk2={"D":4,"E":5,"F":6}
        sozluk3=zip(sozluk1,sozluk2)
        list(zip(sozluk1.keys(),sozluk2.keys()))
        list(zip(sozluk1.values(),sozluk2.values()))
        list(zip(sozluk1.items(),sozluk2.items()))
        
        print("------------------------------------------------------")

        def kupal(x):
            return x**3
        map(kupal,liste1)
        list(map(kupal,liste1))

        for i in map(kupal,liste1):
            print(i)
        def kupal(x,y):
            return x**3,y**3
        for i,j in map(kupal,[i for i in range(10)],[j for j in range(10,20)]):
            print(i,j)
        
        print("-----------------------------------------------------")

        def ciftmi(x):
            if x%2==0:
                return True
            else:
                return False
        liste6=[i for i in range(20)]
        for i in liste6:
            print(ciftmi(i))
        
        filter(ciftmi,liste6)
        filtreliste=list(filter(ciftmi,liste6))
        print(filtreliste)

        print("-------------------------------------------------------")

        liste7=[i**2 for i in range(20)]
        enumerate(liste7)
        list(enumerate(liste7))

        for i,j in enumerate(liste7):
            print("indeks={}, değer={}".format(i,j))
                
onsekiz()
