import os
def get_dir(folder_name:str)-> str:
    BASE_PATH=os.getcwd()
    FOLDER_NAME=folder_name
    return os.path.join(BASE_PATH,FOLDER_NAME)

def get_files(item_list:list)->list:
    file_list=[]
    for item in item_list:
        if (os.path.isfile(os.path.join(get_dir("files_HW"),item))):
            file_list.append(os.path.join(get_dir("files_HW"),item))
    return file_list

def get_files_vol(file_list:list)->dict:
    file_vol={}
    for file in file_list:
        with open(file, "r", encoding="utf-8") as item:
            file_vol[len(item.readlines())]=os.path.basename(file)
    return file_vol

def get_lines(file_name:str)->list:
    file_path=os.path.join(get_dir("files_HW"), file_name)
    with open(file_path, "r", encoding="utf-8") as cf:
        lines=cf.readlines()
    return lines

def worker(files_path:dict, path:str) -> None:
    dict=sorted(files_path.keys())
    file_res=os.path.join(path, "result.txt")
    with open(file_res, "w", encoding="utf-8") as temp_writer:
        for items in dict:
            print(files_path[items])
            temp_writer.writelines(f"\n{files_path[items]}\n{items}\n")
            for i in get_lines(files_path[items]):
                temp_writer.writelines(f"{i}")


def main():
    file_list=get_files(os.listdir(get_dir("files_HW")))
    worker(get_files_vol(file_list), get_dir("files_HW"))

main()