import random
import Card_board as cb
import Menu as menu


menu.main_menu()

numbers_stock = list(range(0,51))
random.shuffle(numbers_stock)

user_card = cb.Card_board()
user_card.printCard()