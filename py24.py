def yirmidort():
        class araba:
            def __init__(self,marka,hizartiş,hizazaliş):
                self.hiz=0
                self.marka=marka
                self.hizartiş=hizartiş
                self.hizazaliş=hizazaliş
            def bilgiYazdir(self):#nesne metodu
                print("araba markası:",self.marka)
                print("araba hızı:",self.hiz)
            def hizart(self):
                self.hiz+=self.hizartiş
            def hizazalt(self):
                self.hiz-=self.hizazaliş
        araba1=araba("BMW",50,30)
        araba2=araba("AUDI",100,40)

        araba1.bilgiYazdir()
        araba2.bilgiYazdir()

        araba1.hizart()
        araba2.hizart()

        araba1.bilgiYazdir()
        araba2.bilgiYazdir()

        araba1.hizazalt()
        araba2.hizazalt()

        araba1.bilgiYazdir()
        araba2.bilgiYazdir()

yirmidort()

