import os
def rename_files():

    #(1) Get names from a filename folder
    file_list = os.listdir(r"C:\Users\Lucas\Desktop\Python programs\prank")
    print(file_list)

    saved_path = os.getcwd()
    print("Current Working Directory is"+saved_path)

    os.chdir(r"C:\Users\Lucas\Desktop\Python programs\prank")
    
    #(2) If number, rename
    for file_name in file_list:

        os.rename(file_name, file_name.translate(None,"0123456789"))

    os.chdir(saved_path)

    
    

    
rename_files()  
