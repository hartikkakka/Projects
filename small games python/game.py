from project_file.player import Humanplayer, Randomcomputerplayer


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("|" + "|".join(row) + "|")

    @staticmethod
    def print_board_num():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("|" + "|".join(row) + "|")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == " ":
        #       moves.append(i)
        # return moves

    def empty_square(self):
        return " " in self.board

    def num_empty_square(self):
        return self.board.count(" ")

    def make_moves(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all(spot == letter for spot in row):
            return True

        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all(spot == letter for spot in col):
            return True

        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal_1):
                return True
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal_2):
                return True

        return False


def play(game, x_player, o_player, print_games=True):
    if print_games:
        game.print_board_num()

    letter = "x"
    while game.empty_square():
        if letter == "o":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_moves(square, letter):
            if print_games:
                print(letter + f"makes a move to square {square}")
                game.print_board()
                print("")
            if game.current_winner:
                if print_games:
                    print(letter + " win ")
                return letter

            letter = "o" if letter == "x" else "x"


if __name__ == "__main__":
    x_player = Humanplayer("x")
    o_player = Randomcomputerplayer("o")
    t = TicTacToe()
    play(t, x_player, o_player, print_games=True)
