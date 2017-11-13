import os

def rename_files():
    path_name = r"/Users/alexander/Documents/developement/prank"
    file_list = os.listdir(path_name)
    os.chdir(path_name)
    
    print("Changing file names")

    for old_name in file_list:
        new_name = old_name.translate(None, "0123456789")
        print("Changing " + old_name + " to " + new_name)
        os.rename(old_name, new_name)

rename_files()
