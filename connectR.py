def askUser():
    width = input("Board Width? >")
    height = input('Board Height? >')
    r = input("Connect? >")
    return int(width), int(height), int(r)

class game:

    def __init__(self):
        self.width, self.height, self.connect = askUser()
        self.board = [[' . ' for i in range(self.width)] for j in range(self.height)]
        self.printBoard()

    def printBoard(self): 
        row = len(self.board)
        col = len(self.board[0])
        for i in range(row):
            print()
            for j in range(col):
                print(self.board[i][j], end=' ')
            print()

    def askPlayer(self):
        move = int(input("Select a move between 0-{} >".format(self.width - 1)))
        if move <= self.width:
            return move
        else:
            move = int(input("Enter valid number between 0-{} >".format(self.width - 1)))
            return move 

    def move(self, turn, col):
        for i in range(self.height - 1, -1, -1):
            if self.board[i][col] == ' . ':
                self.board[i][col] = turn
                self.printBoard()
                return  
    
    def validMove(self, move):
        if move < 0 or move >= self.width:
            return False
        if self.board[move][0] != ' . ':
            return False
        return True

    def tie(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == ' . ':
                    return False    
        return True

    def winner(self, turn):
        for j in range(self.width - 1):
            for i in range((self.connect - 1)):
                if self.board[i][j] == turn and self.board[i+1][j] == turn and self.board[i+2][j] == turn and self.board[i+3][j] == turn:
                    return True 
        for i in range(self.height):
            for j in range((self.connect - 1)):
                if self.board[i][j] == turn and self.board[i][j+1] == turn and self.board[i][j+2] == turn and self.board[i][j+3] == turn:
                    return True                  
        for i in range(5,2,-1):
            for j in range((self.connect - 1)):
                if self.board[i][j] == turn and self.board[i-1][j+1] == turn and self.board[i-2][j+2] and self.board[i-3][j+3] == turn:
                    return True
        for i in range((self.connect - 1)):
            for j in range(self.width - (self.connect - 1)):
                if self.board[i][j] == turn and self.board[i+1][j+1] == turn and self.board[i+2][j+2] and self.board[i+3][j+3] == turn:
                    return True
        return False




game = game()
player1 = ' R '
player2 = ' B '
turn = player1
tie = False
winner = False
while not winner and not tie:
    move = game.askPlayer()
    game.move(turn, move)
    winner = game.winner(turn)
    if turn == player1:
        turn = player2
    else:
        turn =  player1
