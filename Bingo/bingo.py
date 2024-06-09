import random
import Card_board as cb
import Menu as menu
import User as user

main_loop_flag = True
first_time_playing = True
player = user.User()

while main_loop_flag:
    
    if first_time_playing:
        menu.logo_program()
        player.changeName()
        first_time_playing = False

    menu.main_menu(player.name)
    user_main_input = input("Cual es tu opcion: ")

    if user_main_input == "1":
        user_card = cb.Card_board()
        user_card.printCard()
    elif user_main_input == "2":
        player.statistics()
    elif user_main_input == "3":
        player.changeName()
    elif user_main_input == "4":
        print("Adios y que te peten.")
        main_loop_flag = False
    else:
        print("Ni idea de lo que has puesto.")

numbers_stock = list(range(0,51))
random.shuffle(numbers_stock)

