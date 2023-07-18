import random


class Player:
    def __inti__(self, letter):
        self.letter = letter  # letters are x or o

    def get_move(self, game):
        pass


class Randomcomputerplayer(Player):
    def __inti__(self, letter):
        super().__inti__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class Humanplayer(Player):
    def __inti__(self, letter):
        super().__inti__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("invalid moves try again")
        return val
