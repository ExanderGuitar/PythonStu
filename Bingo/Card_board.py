import random

class Card_board:
    def __init__(self) -> None:
        pass

    def create_card_board(self):
        self.numbers = list(range(0, 51))
        random.shuffle(self.numbers)
        self.numbers = self.numbers[0:20]

    def printCard(self):
        print("\t    Bingo Amigo Oro Feliz ")
        print("\t       Carton usuario ")
        print("\t----------------------------")

        for index, num in enumerate(self.numbers):
            if num == "X":
                print(f"\t  {num}", end=" ")
            elif num < 10:
                print(f"\t  {num}", end=" ")
            else:
                print(f"\t {num}", end=" ")

            if((index + 1) % 4 == 0):
                print()

    def mark_number(self, number) -> bool:
        try:
            position = self.numbers.index(int(number))
            self.numbers[position] = "X"
            return True
        except ValueError:
            return False
        