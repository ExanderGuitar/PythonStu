import random

class Card_board:
    def __init__(self) -> None:
        pass

    def create_card_board(self):
        self.numbers = list(range(0, 51))
        random.shuffle(self.numbers)
        self.numbers = self.numbers[0:25]
        self.lines = [self.numbers[0:5], self.numbers[5:10], 
                      self.numbers[10:15], self.numbers[15:20],
                      self.numbers[20:25]]
        for n in range(5):
            self.lines[n][random.randrange(5)] = "X"

    def printCard(self):
        print("\t       Bingo Amigo Oro Feliz        ")
        print("\t           Carton usuario           ")
        print("\t------------------------------------")

        for line in self.lines:
            for index, num in enumerate(line):
                if num == "X":
                    print(f"\t  {num}", end=" ")
                elif num < 10:
                    print(f"\t  {num}", end=" ")
                else:
                    print(f"\t {num}", end=" ")
            print()

    def mark_number(self, number) -> bool:
        try:
            position = self.numbers.index(int(number))
            self.numbers[position] = "X"
            return True
        except ValueError:
            return False
        