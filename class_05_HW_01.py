documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
def name(doc, num):
    for item in doc:
        if item["number"] == num:
            return item["name"]
    return "there is no such number"

def shelf(dir, num):
    for item in range(1,len(dir)+1):
        if num in dir[str(item)]:
            return item
    return "there is no such number"

def list(doc):
    for items in doc:
        print(f"""{items["type"]} "{items["number"]}" "{items["name"]}" """)

def add_doc(doc):
    user_type=input("Doc type: ")
    user_number=input("doc number: ")
    user_name=input("user name")
    doc_new=doc
    i=0
    for items in doc:
        i+=1
        if user_type == items["type"] and user_number==items["number"] and user_name==items["name"]:
            print("This document is already here")
            break
        print("added")
        doc_new.append({"type":user_type, "number":user_number, "name":user_name})
        return doc_new

def add_dir(dir, num):
    shelf_num=input("which shelf do you want to use: ")
    if 0<int(shelf_num)<=3:
        dir[str(shelf_num)].append(num)
        print("already there")
        return dir
    return "shelf doesn't exist"


def main(doc, dir):
    while True:
        user_comand=input("Please give your comand: ")
        if user_comand=="p":
            user_data=input("Please give doc number: ")
            print(name(doc, user_data))
        elif user_comand=="s":
            user_data=input("Please give doc number: ")
            print(shelf(dir, user_data))
        elif user_comand=="l":
            list(doc)
        elif user_comand == "a":
            doc_new=add_doc(doc)
            print(doc_new)
            num=doc_new[len(doc_new)-1]["number"]
            print(add_dir(dir,num))
        elif user_comand=="q":
            print("Thank you")
            break
main(documents,directories)