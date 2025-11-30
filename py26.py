def yirmialtı():
        class Mystring:
            stringlistesi=[]

            def __init__(self,string):
                print(string,"listeye ekleniyor...")
                self.string=string
                self.stringlistesi.append(string)
            
            @classmethod#sınıfın kendisine ait metotlar oluşturmak için kullanılır
            def listeyiyazdır(cls):
                for string in cls.stringlistesi:
                    print(string)
            @staticmethod#sınıfa ait olmayan ama sınıf ile ilgili olan metotlar için kullanılır
            def tersiniyazdır(string):
                print(string[::-1])
        
        string1=Mystring("hava savunma")
        string2=Mystring("astsubay")
        string3=Mystring("astçavuş")

        Mystring.listeyiyazdır()
        Mystring.tersiniyazdır(string2.string)

    
yirmialtı()
