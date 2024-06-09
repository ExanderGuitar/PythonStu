import random
import os
import Card_board as cb
import Menu as menu
import User as user

def startGame():
    # Generate the random stock number
    numbers_stock = list(range(0,51))
    random.shuffle(numbers_stock)

    # Generate user card
    player_card.create_card_board()

    while len(numbers_stock) > 0:
        print()
        print("¡Partida en curso!")
        print("------------------")
        ball = numbers_stock.pop()
        print(f"Bola número {ball}")

        if len(numbers_stock) == 0:
            print(f"¡Se acabaron los números, fin de la partida!")
        else:
            print(f"Quedan {len(numbers_stock)} bolas.")

        print()
        player_card.printCard()
        print()

        print("Que quieres hacer?")
        print("1. Marcar el número en el cartón.")
        print("2. Cantar línea.")
        print("3. Cantar bingo.")
        print("4. Pasar.")
        print("5. Abandonar la partida.")
        selection = input("Tu selección: ")

        if selection == "1":
            if player_card.mark_number(ball):
                print("¡Numero marcado!")
            else:
                print("Tu número no esta en tú cartón.")
        elif selection == "2":
            print("¡Línea!")
        elif selection == "3":
            print("¡Bingo, bingo!")
        elif selection == "4":
            print("No haces nada y esperas.")
        elif selection == "5":
            print("Saliendo de la sala.")
            break
        else:
            print("No te entiendo, pasas turno.")



main_loop_flag = True
first_time_playing = True
player = user.User()
player_card = cb.Card_board()

while main_loop_flag:
    
    if first_time_playing:
        menu.logo_program()
        player.changeName()
        first_time_playing = False

    menu.main_menu(player.name)
    user_main_input = input("Cual es tu opcion: ")

    if user_main_input == "1":
        startGame()
    elif user_main_input == "2":
        player.statistics()
    elif user_main_input == "3":
        player.changeName()
    elif user_main_input == "4":
        print("Adios y que te peten.")
        main_loop_flag = False
    else:
        print("Ni idea de lo que has puesto.")