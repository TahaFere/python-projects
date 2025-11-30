def yirmidokuz():
        class complexNumber:
            def __init__(self,gercekKisim=0,sanalKisim=0):
                self.gercekKisim=gercekKisim
                self.sanalKisim=sanalKisim

            def complexToplam(self,complexSayi):
                toplamComplex=complexNumber()
                toplamComplex.gercekKisim=self.gercekKisim+complexSayi.gercekKisim
                toplamComplex.sanalKisim=self.sanalKisim+complexSayi.sanalKisim
                return toplamComplex
        
            def complexCarpim(self,complexSayi):
                carpimComplex=complexNumber()
                carpimComplex.gercekKisim=(self.gercekKisim*complexSayi.gercekKisim)-(self.sanalKisim*complexSayi.sanalKisim)
                carpimComplex.sanalKisim=(self.gercekKisim*complexSayi.sanalKisim)+(self.sanalKisim*complexSayi.gercekKisim)
                return carpimComplex
            
            def sabitCarpim(self,sabit):
                sabitComplex=complexNumber()
                sabitComplex.gercekKisim=self.gercekKisim*sabit
                sabitComplex.sanalKisim=self.sanalKisim*sabit
                return sabitComplex
            
            def negatifeCevir(self):
                negatifComplex=complexNumber()
                negatifComplex.gercekKisim=-1
                negatifComplex.sanalKisim=-1
                return negatifComplex

            def complexCikarma(self,complexSayi):
                complexSayi.negatifeCevir()
                cikarmaComplex=self.complexToplam(complexSayi)
                return cikarmaComplex
            
            def complexYazdir(self):
                if self.sanalKisim>=0:
                    print("{}+{}i".format(self.gercekKisim,self.sanalKisim))
                else:
                    print("{}{}i".format(self.gercekKisim,self.sanalKisim))

        complex1=complexNumber(3,5)
        complex1.complexYazdir()
        complex2=complexNumber(2,-4)
        complex2.complexYazdir()
        complexToplam=complex1.complexToplam(complex2)
        complexToplam.complexYazdir()
        complexCikarma=complex1.complexCikarma(complex2)
        complexCikarma.complexYazdir()
        complexCarpim=complex1.complexCarpim(complex2)
        complexCarpim.complexYazdir()
        sabitCarpim=complex1.sabitCarpim(3)
        sabitCarpim.complexYazdir()
yirmidokuz()

