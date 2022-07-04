import os
import pprint

def get_path(file_name:str, file_dir:str) -> str:
    FILE_NAME=file_name
    FILE_DIR=file_dir
    BASE_PATH=os.getcwd()
    path_to_file=os.path.join(BASE_PATH, FILE_DIR, FILE_NAME)
    return path_to_file

def cook_book_form(path_to_file_rec:str) -> dict:
    with open(path_to_file_rec, "r", encoding="utf-8") as rec_file:
        cond = rec_file.readline().strip()
        cook_book = {}
        while cond:
            dish_name = cond
            cook_book[dish_name] = []
            num_ingridients = int(rec_file.readline())
            for i in range(num_ingridients):
                ing = rec_file.readline().strip()
                specing = ing.split(sep=" | ")
                cook_book[dish_name].append(
                    {'ingredient_name': specing[0], 'quantity': specing[1], 'measure': specing[2]})
            rec_file.readline()
            cond = rec_file.readline().strip()
    return cook_book

def get_shop_list_by_dishes(dishes:list, person_count:int, cook_book:dict) ->dict:
    shop_list={}
    for dish in dishes:
        for food in cook_book[dish]:
            if food["ingredient_name"] not in shop_list:
                shop_list[food["ingredient_name"]]={"measure":food["measure"], "quantity":int(food["quantity"])*person_count}
            else:
                shop_list[food["ingredient_name"]]["quantity"]+=int(food["quantity"])*person_count
    return shop_list

def writer(file_name:str, file_dir:str, text:dict) -> None:
    with open(get_path(file_name, file_dir), "w", encoding="utf-8") as file:
        for key, val in text.items():
            x=f"{key}: {val} \n"
            file.write(x)

cook_book=cook_book_form(get_path("recipes.txt", "hw_dir"))
shop_list=get_shop_list_by_dishes(["Омлет"], 2, cook_book)
writer("shop_list.txt", "hw_dir", shop_list)

