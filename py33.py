def otuzüc():
        class ucgen:
            def __init__(self,kenar1,kenar2,kenar3):
                while not self.ucgenOlusurMu(kenar1,kenar2,kenar3):
                    kenar1,kenar2,kenar3=input("üçgen oluşturmak için geçerli kenar uzunlukları giriniz:").split(",")
                    self.kenar1=kenar1
                    self.kenar2=kenar2
                    self.kenar3=kenar3
            
            @staticmethod
            def ucgenOlusurMu(kenar1,kenar2,kenar3):
                if(abs(kenar2-kenar3)>=kenar1 or kenar1>=kenar2+kenar3)and(abs(kenar1-kenar3)>=kenar2 or kenar2>=kenar1+kenar3)and(abs(kenar1-kenar2)>=kenar3 or kenar3>=kenar1+kenar2):
                    print("üçgen oluşturulamaz")
                    return False
                else:
                    print("üçgen oluşturulabilir")
                    return True

            def eskenarUcgenMi(self):
                if self.kenar1==self.kenar2 and self.kenar2==self.kenar3:
                    print("eşkenar üçgendir")
                    return True
                else:
                    print("eşkenar üçgen değildir")
                    return False

            def ikizkenarUcgenMi(self):
                if self.kenar1==self.kenar2 or self.kenar2==self.kenar3 or self.kenar1==self.kenar3:
                    print("ikizkenar üçgendir")
                    return True
                else:
                    print("ikizkenar üçgen değildir")
                    return False

            def cesitkenarUcgenMi(self):
                if not self.eskenarUcgenMi() and not self.ikizkenarUcgenMi():
                    print("çeşitkenar üçgendir")
                    return True
                else:
                    print("çeşitkenar üçgen değildir")
                    return False
            #    if self.kenar1!=self.kenar2 and self.kenar2!=self.kenar3 and self.kenar1!=self.kenar3:
            #        print("çeşitkenar üçgendir")
            #        return True
            #    else:
            #        print("çeşitkenar üçgen değildir")
            #        return False
            
            def ucgenTipi(self):
                if self.cesitkenarUcgenMi()==True:
                    print("üçgen çeşitkenar üçgendir")
                elif self.ikizkenarUcgenMi()==True:
                    print("üçgen ikizkenar üçgendir")
                elif self.eskenarUcgenMi()==True:
                    print("üçgen eşkenar üçgendir")
                else:
                    print("üçgen tanımlanamıyor")

            def alanHesaplama(self):
                if self.ucgenOlusurMu()==True:
                    s=(self.kenar1+self.kenar2+self.kenar3)/2
                    alan=(s*(s-self.kenar1)*(s-self.kenar2)*(s-self.kenar3))**0.5
                    print("üçgenin alanı:",alan)
                else:
                    print("üçgen oluşturulamadığı için alan hesaplanamaz")
            
        ucgen1=ucgen(5,5,5)
        ucgen1.ucgenOlusurMu()
        ucgen1.eskenarUcgenMi()
        ucgen1.ikizkenarUcgenMi()
        ucgen1.cesitkenarUcgenMi()
        ucgen1.ucgenTipi()
        ucgen1.alanHesaplama()
        ucgen2=ucgen(5,5,8)
        ucgen2.ucgenOlusurMu()
        ucgen2.eskenarUcgenMi()
        ucgen2.ikizkenarUcgenMi()
        ucgen2.cesitkenarUcgenMi()
        ucgen2.ucgenTipi()
        ucgen2.alanHesaplama()

otuzüc()
