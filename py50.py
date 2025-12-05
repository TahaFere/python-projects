def elli():
    import json

    # with open("python/data.json","r",encoding="utf-8") as f:# karakter hatası almamak için utf-8 olması gerektiğini belirttik
    #     result=json.load(f)# bu methot ile dict verisine çevrildi -- python içinde json verisi varsa loads eğer dişardan dosyadan çekiyorsan load kulanılır7
    #     print(type(result))
    #     print(f"Name:{result["name"]}")
    #     print(f"Age:{result["age"]}")
    #     print(f"City:{result["city"]}")
    #     print(f"Hobbies:",end="")
    #     for item in result["hobbies"]:
    #         print(item,end=" ")
    
    # person={"name":"Taha","age":25,"city":"BURSA","hobbies":["kodlama","müzik","spor"]}# tek tırnaklar arasındaki vei json stringidi
    # result=json.dumps(person,ensure_ascii=False,indent=4,sort_keys=True,separators=(".","= "))#proje içindeki tek veri türünü jsona çevireceğimiz için dumps kullandık, 
    # #eensure_ascii= karakterleri ingilizce olmadığını belli ediyorum kendini utf-8 göre ayarlıyor
    # #indent= 4 boşluk olucak şekilde girinti ayarlandı
    # #sort_keys= keyleri alfavetik sıraya koyuyor
    # #separators= json verisini iki key value arasında ki vigül değilde nokta koyup ,key ile value arasında ikinokta ile atama değilde eşittirme atama yapılmış gibi göstermeye yarıyor
    # print(type(result))
    # print(result)

    # print(json.dump({"name":"Taha","age":25}))
    # print(json.dump(["php","c++","java","c"]))
    # print(json.dump(("strawberry","pineapple")))
    # print(json.dump("hello python"))
    # print(json.dump(7))         # her biri json veri türüne değiştirile biliyor
    # print(json.dump(19.23))
    # print(json.dump(True))
    # print(json.dump(False))
    # print(json.dump(None))

    # x={
    #     "name":"Taha",
    #     "age":25,
    #     "married":False,
    #     "divorced":True,
    #     "parents":("ann","john"),
    #     "pets":None,
    #     "cars":["skoda superb","nissan juke"]
    # }
    # json_result=json.dumps(x,ensure_ascii=False,indent=4)
    # print(json_result)

    
    person={"name":"Taha","age":25,"city":"BURSA","hobbies":["kodlama","müzik","spor"]}
    with open("python/people.json","w",encoding="utf-8") as f:
        json_result=json.dump(person,f,ensure_ascii=False,indent=4)
        #dosya yazılacağı zaman dump dosyadan çekileceği zaman dumps kullanıyoruz


elli()