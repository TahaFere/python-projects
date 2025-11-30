def kirkbes():
    
        #BEAUTİFULSOUP MODÜLÜ
        #kurulumu pip install beutifulsoup4
        from bs4 import BeautifulSoup
        import requests
        
        #Beatifulsoup modülüne neden ihtiyacımız var?
        #HTML içeriğini çektiğimiz web siteyi parçalamak için kullanıyoruz        

        #Beautifulsoup obje oluşturarak parçalama işlmei ve prettify fonsksiyonu
        #HTML içeriğini çektiğimiz web siteyi parçalamak için kullanıyoruz
        sayfaURL="https://www.sondakika.com/"
        sayfaCevabi=requests.get(sayfaURL)
        if sayfaCevabi.status_code==200:
            htmlIcerik=sayfaCevabi.content
            soup=BeautifulSoup(htmlIcerik,"html.parser")
            print(soup.prettify())
            

        #belirli bir etiket değerlerini alma ve find fonksiyonu
        #find fonksiyonu ile birlikte oluşturduğumuz beautifulSoup ile parçalayabiliyoruz ve prettify fonksiyonunu 
        #kullanarak düzgün görünmesini sağlayabiliyoruz
        if sayfaCevabi.status_code==200:
            htmlIcerik=sayfaCevabi.content
            soup=BeautifulSoup(htmlIcerik,"html.parser")
            print(soup.find("title").text)
            print(soup.find("li"))#eşleşen ilk html kodunu getiri
            print(soup.find("a"))


        #belirli bir etiket değerlerini alma ve find_all fonksiyonu
        #find_all fonskiyonu ile birlikte oluşturduğuuz beautifulSoup obje üzerinde etiket araması yapabiliriz, 
        #eşleşen etiketler liste halinde bize verilir
        if sayfaCevabi.status_code==200:
            htmlIcerik=sayfaCevabi.content
            soup=BeautifulSoup(htmlIcerik,"html.parser")
            for icerik in soup.find_all("a"):
                print(icerik)
                print(icerik.text)
            print("*************")
            for icerik1 in soup.find_all("span",{"class":"news-txt"}):#class gibi iç parametleri yazmadan önce etiketi kontrol et nasıl yazılmış diye!!!
                print(icerik1)
            print("*************")
            for icerik in soup.find_all("a",{"title"}):
                print(icerik)
            print("*************")
        #etiket içerisinden belirli değerleri alma ve get fonksiyonu
        #get fonksiyonu ile birlikte find_all fonksiyonu ile elde ettiğimiz liste üzerinden belirli kısımları elde edebiliriz
        if sayfaCevabi.status_code==200:
            htmlIcerik=sayfaCevabi.content
            soup=BeautifulSoup(htmlIcerik,"html.parser")
            for icerik in soup.find_all("a"):
                print(icerik.get("href"))
            print("*************")
            for icerik in soup.find_all("a"):
                print(icerik.get("id"))
            print("*************")
            for icerik in soup.find_all("a"):
                print(icerik.get("title"))
            print("*************")
            for icerik in soup.find_all("span"):
                print(icerik.get("class"))
            print("*************")

kirkbes()
