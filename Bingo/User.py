class User:

    def __init__(self) -> None:
        self.name = ""
        self.matches = 0
        self.win = 0
        self.lose = 0

    def statistics(self):
        print()
        print(f"Usuario: {self.name}")
        print(f"Partidas jugadas: {self.matches}.")
        print(f"Ganadas: {self.win}.")
        print(f"Perdidas: {self.lose}.")

    def changeName(self):
        self.name = input("Cual es tu nombre: ")