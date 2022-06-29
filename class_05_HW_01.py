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
    for items in doc:
        if user_type == items["type"] and user_number==items["number"] and user_name==items["name"]:
            print("This document is already here")
            break
        print("added")
        doc_new.append({"type":user_type, "number":user_number, "name":user_name})
        return doc_new

def add_dir(dir, num):
    shelf_num=input("which shelf do you want to use: ")
    if shelf_num in dir.keys():
        dir[str(shelf_num)].append(num)
        print("already there")
        return dir
    return "shelf doesn't exist"

def delete_doc(doc, num ,dir):
    for id, items in enumerate(doc):
        if items["number"] == num:
            del doc[id]
            delete_shelf(dir, num)
            return doc
    return("This documents doesn't exist")

def delete_shelf(dir,num):
    for key, val in dir.items():
        if num in val:
            val.remove(num)
            dir[key]=val
            print(dir)

def move(dir):
    user_num=input("Doc number: ")
    for key, val in dir.items():
        if user_num in val:
            user_shelf = input("which shelf do you want to use:")
            if user_shelf in dir.keys():
                val.remove(user_num)
                dir[key] = val
                dir[user_shelf].append(user_num)
                return dir
            else:
                print("The shelf can be from 1 to 3")
                break
        else:
            print("bad doc number!")
            break

def add_shelf(dir):
    new_shelf=input("add your new shelf: ")
    if new_shelf not in dir.keys():
        dir[new_shelf]=[]
        return dir
    else:
        return "this shelf already here!!"


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
        elif user_comand == "d":
            user_number = input("doc number: ")
            print(delete_doc(doc, user_number, dir))
            print("deleted")
        elif user_comand == "m":
            print(move(dir))
        elif user_comand=="as":
            print(add_shelf(dir))
        elif user_comand=="q":
            print("Thank you")
            break
main(documents,directories)