import os

def rename_files():
    file_list = os.listdir(r"D:\python practice\images")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"D:\python practice\images")
    saved_path = os.getcwd()
    print(saved_path)
    for file_name in file_list:
        print("old name : "+file_name)
        print("new name : "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    file_list = os.listdir(r"D:\python practice\images")
    print(file_list)
rename_files()