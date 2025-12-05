#json "javaScript object notation"

import json
import os

FILE_NAME="python/people1.json"

class Person:
    def __init__(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w", encoding="utf-8") as f:
                json.dump([],f,ensure_ascii=False,indent=4)

    def read_people(self):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
        
    def save_people(self,people):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(people,f,ensure_ascii=False,indent=4)
    
    def add_person(self):
        name=input("NAME:")
        age=int(input("AGE:"))
        city=input("CİTY:")
        
        new_person={"name":name,"age":age,"city":city}

        people=self.read_people()
        people.append(new_person)
        self.save_people(people)

        print(f"{name} has been added!")

    def delete_person(self):
        name=input("enter the name of the person to delete:")
        people=self.read_people()
        update_people=[item for item in people if item["name"]!=name]

        if len(people)==len(update_people):
            print(f"{name} not found!")
        else:
            self.save_people(update_people)
            print(f"{name} has been delete!")

    def show_people(self):
        people=self.read_people()

        if not people:
            print("no people found")
        else:
            for item in people:
                print(f"Name:{item["name"]}, Age:{item["age"]}, City:{item["city"]}")

class App:
    def __init__(self):
        self.manager=Person()

    def run(self):
        while True:
            print("\n1-Add Person")
            print("2-Delete Person")
            print("3-Show All Person")
            print("4-Exit")
            choice=int(input("choose an option"))
        
            if   choice==1: self.manager.add_person()
            elif choice==2: self.manager.delete_person()
            elif choice==3: self.manager.show_people()
            elif choice==4:
                print("Exiting...")
                break
            else:
                print("Invalid option! plase try again")

if __name__=="__main__":
    app=App()
    app.run()