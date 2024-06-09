import random
import Card_board as cb
import Menu as menu

main_loop_flag = True
first_time_playing = True
user_name = ""

while main_loop_flag:
    
    if first_time_playing:
        menu.logo_program()
        user_name = input("Dinos tu nombre: ")
        first_time_playing = False

    menu.main_menu(user_name)
    user_main_input = input("Cual es tu opcion: ")

    if user_main_input == "1":
        user_card = cb.Card_board()
        user_card.printCard()
    elif user_main_input == "2":
        print("Has ganado la ostia de partidas.")
    elif user_main_input == "3":
        user_name = input("Cual es tu nombre de usuario: ")
    elif user_main_input == "4":
        print("Adios y que te peten.")
        main_loop_flag = False
    else:
        print("Ni idea de lo que has puesto.")

numbers_stock = list(range(0,51))
random.shuffle(numbers_stock)

