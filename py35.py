def otuzbes():
        b=int(input("35 içinde hangi kodu çalıştırmak istersiniz? (1-2-3):"))
        if(b==1):
            def otuzbesbir():
                #ıterator(yenileyici), sayılabilir sayıda değer içeren bir nesnedir.
                myList=["elma","armut","muz"]
                myIt=iter(myList)

                print(next(myIt))
                print(next(myIt))
                print(next(myIt))

                while True:
                    try:
                        print(next(myIt))
                    except StopIteration:
                        break


                myStr="Python"
                myIt2=iter(myStr)

                print(next(myIt2))
                print(next(myIt2))
                print(next(myIt2))
                print(next(myIt2))
                print(next(myIt2))
                print(next(myIt2))

                while True:
                    try:
                        print(next(myIt2))
                    except StopIteration:
                        break

        if(b==2):
            def otuzbesiki():
                class Sayi:
                    def __iter__(self):
                        self.sayi=0
                        return self
                    
                    def __next__(self):
                        gecici=self.sayi
                        self.sayi+=1
                        return gecici
            
                Sayi=Sayi()
                sayiIt=iter(Sayi)
                print(next(sayiIt))
                print(next(sayiIt))
                print(next(sayiIt))
                print(next(sayiIt))

            otuzbesiki()

        if(b==3):
            def otuzbesüç():
                class Sayi:
                    def __iter__(self):
                        self.sayi=0
                        return self
                    
                    def __next__(self):
                        if self.sayi<=5:
                            gecici=self.sayi
                            self.sayi+=1
                            return gecici
                        else:
                            raise StopIteration
                sayi=Sayi()
                sayiIt=iter(sayi)
                while True:
                    try:
                        print(next(sayiIt))
                    except StopIteration:
                        print("İterasyon tamamlandı.")
                        break 
            otuzbesüç()


otuzbes()
