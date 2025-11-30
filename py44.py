def kırkdort():
    #REQUEST MODÜLÜ
    #kurulum= pip install request
    #request modülüne neden ihtiyacımız var?
    #request modülünün kullanarak web üzerindeki HTTPS isteklerimizi(get,post,put,delete) yönetebileceğiz
        import requests

        b=int(input("bir sayı giriniz:"))
        print(b)
        if(b==1):
            def kirkdortbir():
                #GET modülü ile sayfa içeriğini alma ve parametre gönderme
                #GET modülü ie parametre göndereceğimiz zaman, gönderdiğimiz parametlerel URL yapısı içerisinde bulunuyor.
                sayfaURL="https://httpbin.org/get"
                sayfaCevabi=requests.get(sayfaURL)
                print(sayfaCevabi.status_code)
                print("----1")
                print(sayfaCevabi.content)
                print("----2")
                sayfaCevabi=requests.get(sayfaURL,params={"kullanici_adi":"Tf","sifre":"1234"})
                print(sayfaCevabi.status_code)
                print("----3")
                print(sayfaCevabi.url)
                print("----4")
                print(sayfaCevabi.content)
                print("----5")
                #POST modülü ile sayfa içeriğini alma ve sayfaya veri gönderme 
            kirkdortbir()
        if(b==2):

            sayfaURL="https://jsonplaceholder.typicode.com/posts"
            sayfaCevabi1=requests.post(sayfaURL)
            print(sayfaCevabi1.status_code)
            print(sayfaCevabi1.url)
            print(sayfaCevabi1.content)
            sayfaCevabi2=requests.post(sayfaURL,data={"kullanici_adi":"TF","sifre":"12345"})
            print(sayfaCevabi2)
            print(sayfaCevabi2.url)
            print(sayfaCevabi2.json)

        if(b==3):
            sayfaURL1="https://httpbin.org"
            sayfaCevabi3=requests.get(sayfaURL1)
            print(sayfaCevabi3.status_code)
            
            #text sitenin HTML içeriğini döndürü
            print(sayfaCevabi3.text)

            #headers sitenin hearder bilgisini döndürü
            print(sayfaCevabi3.headers)

            #request siteye yapmış oldupumuz isteğin ne olduğunu döndürü
            print(sayfaCevabi3.request)

            #elapsed toplam geçen süreyi döndürü
            print(sayfaCevabi3.elapsed)

kırkdort()
