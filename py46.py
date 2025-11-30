def kirkaltı():
        from bs4 import BeautifulSoup
        import requests

        b=int(input("1.Amazon sitesinde en çok satan kitapları listeleme\n"
        "2.İş bankasından döviz bilgisini gösterme\n"
        "çalıştırmak istediğinizin program sayısını giriniz:"
        ))
        if(b==1):
            sayfaURL="https://www.amazon.com.tr/gp/bestsellers/books/"
            sayfaCevabi=requests.get(sayfaURL)
            if sayfaCevabi.status_code==200:
                htmlicerik=sayfaCevabi.content
                soup=BeautifulSoup(htmlicerik,"html.parser")
                for icerik in soup.find_all("li",{"class":"zg-no-numbers"}):
                    kitapAdi=icerik.find("div",{"class":"_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"})
                    kitapYazari=icerik.find("span",{"class":"a-size-small a-color-base"})
                    kitapPuan=icerik.find("span",{"class":"a-icon-alt"})
                    kitapFiyati=icerik.find("span",{"class":"p13n-sc-price"})
                    if kitapAdi!=None:
                        print("***************")
                        print("Kitabın Adı:"+kitapAdi.text)
                        print("Kitabın Yazarı:"+kitapYazari.text)
                        print("Kitabın Puanı:"+kitapPuan.text)
                        print("Kitabın Fiyatı:"+kitapFiyati.text)
                        print("***************")
                    else: continue
        if(b==2):
            sayfaURL="https://www.albaraka.com.tr/tr/doviz-kurlari"
            sayfaCevabi=requests.get(sayfaURL)
            if(sayfaCevabi.status_code==200):
                htmlicerik=sayfaCevabi.content
                soup=BeautifulSoup(htmlicerik,"html.parser")
                #print(soup)
                for icerik in soup.find_all("tr"):
                    #print(icerik)
                    #print(icerik.find("td",{"class":"text-left"}))
                    #print(icerik.find("td",{"class":"text-center"}))
                    doviz=icerik.find("tr",{"class":"text-left"})
                    dovizalıs=icerik.find("td",{"class":"text-center"})
                    print("doviz adı:"+doviz)
                    print("doviz alış:"+dovizalıs)
                    print("*******")
            
kirkaltı()
