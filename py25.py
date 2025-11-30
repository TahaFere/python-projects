def yirmibeş():
        class araba:
            arabalistesi=[]
            def __init__(self,marka,hizartiş,hizazaliş):
                self.hiz=0
                self.marka=marka
                self.hizartiş=hizartiş
                self.hizazaliş=hizazaliş
                self.arabalistesi.append(marka)
            def bilgiYazdir(self):#nesne metodu
                print("araba markası:",self.marka)
                print("araba hızı:",self.hiz)
            def hizart(self):
                self.hiz+=self.hizartiş
            def hizazalt(self):
                self.hiz-=self.hizazaliş
            @classmethod
            def arablariYazdir(cls):
                for araba in cls.arabalistesi:
                    print("araba markası:",araba)

        araba1=araba("BMW",50,30)
        araba2=araba("AUDI",100,40)
        araba3=araba("TOYOTA",80,20)

        araba1.arablariYazdir()
        araba.arablariYazdir()

yirmibeş()

