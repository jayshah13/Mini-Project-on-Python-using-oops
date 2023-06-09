import random

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = None
        self.players = ["Player 1", "Player 2"]
        self.symbols = ["X", "O"]

    def draw_board(self):
        print("-------------")
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print("|", end="")
            for cell in row:
                print(f" {cell} |", end="")
            print("\n-------------")

    def set_players(self, players):
        self.players = players

    def set_symbols(self, symbols):
        self.symbols = symbols

    def start_game(self):
        self.current_player = random.choice(self.players)
        print(f"{self.current_player} will play first.\n")
        self.draw_board()

        while True:
            move = self.get_move()
            self.make_move(move)

            if self.check_win():
                self.draw_board()
                print(f"\n{self.current_player} wins! Congratulations!")
                break

            if self.check_draw():
                self.draw_board()
                print("\nThe game is a draw.")
                break

            self.switch_player()
            self.draw_board()

    def get_move(self):
        if self.current_player == "Player 1":
            while True:
                move = input("Player 1, enter your move (1-9): ")
                if move.isdigit() and 1 <= int(move) <= 9 and self.board[int(move) - 1] == " ":
                    return int(move) - 1
                else:
                    print("Invalid move. Please try again.")

        else:  # Computer's move
            available_moves = [i for i, cell in enumerate(self.board) if cell == " "]
            return random.choice(available_moves)

    def make_move(self, move):
        self.board[move] = self.symbols[self.players.index(self.current_player)]

    def check_win(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True

        return False

    def check_draw(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]


# Playing against the computer
game1 = TicTacToe()
game1.set_players(["Player 1", "Computer"])
game1.set_symbols(["X", "O"])
game1.start_game()

# Playing between two players
game2 = TicTacToe()
game2.start_game()
