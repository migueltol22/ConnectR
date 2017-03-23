def board_size():
    x = input("Board Width? ")
    y = input("Board Height? ")
    r = input("Connect? ")
    return int(x), int(y), int(r)


class game:
    
    def __init__(self):
        width, height, connect = board_size()
        self.board = connectR(width, height, connect)
        self.player1 = player()
        self.player2 = player()


class player:
    turn = None

    def __init__(self):
        self.name = input("Player name? > ")

    def Askturn():
        x = input("Move? (0-6) > ")
        return int(x)



class connectR:
    board = [[]]
    connect = None

    def __init__(self, x = 7, y = 6, connect = 4):
        print("Creating Connect{} board with a width of {} and height of {}".format(connect, x, y))
        self.board = [[0 for row in range(x)] for col in range(y)]
        self.connect = connect

    def printBoard(self):
        row = len(self.board)
        col = len(self.board[0])
        for i in range(row):
            print()
            for j in range(col):
                print(self.board[i][j], end = " ")
        print()

game = game()



