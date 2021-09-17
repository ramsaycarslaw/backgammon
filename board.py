board = """
+13-14-15-16-17-18------19-20-21-22-23-24-+
| X           O    |   | O              X |
| X           O    |   | O              X |
| X           O    |   | O                |
| X                |   | O                |
| X                |   | O                |
|                  |BAR|                  |
| O                |   | X                |
| O                |   | X                |
| O           X    |   | X                |
| O           X    |   | X              O |
| O           X    |   | X              O |
+12-11-10--9--8--7-------6--5--4--3--2--1-+
"""

class Game():

    def __init__(self):
        self.board = []
        self.bar = []
        self.white_turn = True
        # Populate array from 0 to 24 with empty arrays
        for i in range(0,24):
            self.board.append([])

    def new_game(self):
        """
        populate an array with the starting backgamon positions
        """
        self.board[0] = ["O","O"]
        self.board[5] = ["X", "X", "X", "X", "X"]
        self.board[7] = ["X", "X", "X"]
        self.board[11] = ["O", "O", "O", "O", "O" ]
        self.board[12] = ["X", "X", "X", "X", "X"]
        self.board[16] = ["O","O","O"]
        self.board[18] = ["O", "O", "O", "O", "O" ]
        self.board[23] = ["X","X"]

    # TODO fix this
    def print_board(self):
        print(" -- BOARD -- ")
        for i in range(len(self.board)):
            print(i, ": ".join(self.board[i]))
        print("")

    def print_bar(self):
        print(self.bar)

    def move(self, start, end):
        # Handle putting pieces back
        if start == 0:
            # Off the bar
            curr = self.bar[0]
        else:
            curr = self.board[start-1].pop()
        
        # Capture a piece
        if len(self.board[end-1]) == 1:
            if self.board[end-1][0] != curr:
                self.bar.append(self.board[end-1].pop())

        self.board[end-1].append(curr)

        # toggle turn
        self.white_turn = !self.white_turn


g = Game()
g.new_game()
g.print_board()
g.move(1,5)
g.print_board()
g.move(6,5)
g.print_board()
g.print_bar()

