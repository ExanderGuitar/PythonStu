import os
import pandas as pd
import ChromaSupport as chsup

#Function definitions

#Declared variables
main_loop = True
system_msg = ""
loaded_file = False

#Program start point

while(main_loop):
    os.system("cls")
    
    chsup.menu(system_msg)
    
    user_menu_input = input("Your selection: ")

    if(user_menu_input == "1"):
        print("Loading an excel file.\n")
        system_msg = chsup.load_excel_file()
    elif (user_menu_input == "2"):
        print("Loading a csv or text file.\n")
        system_msg = chsup.load_text_file()
    elif (user_menu_input == "3"):
        print("Changing directory.\n")
        system_msg = chsup.change_directory()
    elif (user_menu_input == "4"):
        print("Closing the program.\n")
        main_loop = False
    else:
        system_msg = "Error. Input not recognized.\n"



"""
file_name = input("Name of the file: ")

df = pd.read_csv(file_name, sep="\t")
print(df)
"""
