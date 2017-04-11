import copy
import random

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
                print(self.board[i][j], end="")
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
                return

    
    def validMove(self, move):
        if move < 0 or move > self.width:
            return False
        if self.board[0][move] != ' . ':
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
                if self.board[i][j] == turn and self.board[i-1][j+1] == turn and self.board[i-2][j+2] == turn and self.board[i-3][j+3] == turn:
                    return True
        for i in range((self.connect - 1)):
            for j in range(self.width - (self.connect - 1)):
                if self.board[i][j] == turn and self.board[i+1][j+1] == turn and self.board[i+2][j+2] == turn and self.board[i+3][j+3] == turn:
                    return True
        return False

    def AImove(self, turn):
        possibilities = self.getMoves(turn, 2)
        print(possibilities)
        bestScore = 0
        for i in range(len(possibilities)):
            if possibilities[i] >= bestScore:
                bestScore = possibilities[i]
        bestMoves = []
        for i in range(len(possibilities)):
            if possibilities[i] == bestScore:
                bestMoves.append(i)
        return random.choice(bestMoves)

    def getMoves(self, turn, depth):
        if depth == 0:
            possible = []
            for i in range(self.width):
                if self.validMove(i):
                    newBoard = copy.deepcopy(self)
                    newBoard.move(turn, i)
                    possible.append(newBoard.getScore(turn))
            return possible
        possible = []
        oppTurn = ' '
        if turn == ' R ':
            oppTurn == ' B '
        else:
            oppTurn == ' R '

        if self.tie():
            return [0] * self.width

        possible = [0]*self.width
        for move in range(self.width):
            newBoard = copy.deepcopy(self)
            if newBoard.validMove(move):
                newBoard.move(turn, move)
            if newBoard.winner(turn):
                possible[move] = 10
                return possible
                possible[move] = newBoard.getScore(turn)
            else:
                if newBoard.tie():
                    possible[move] = 0
                    return possible
                else:
                    for move in range(newBoard.width):
                        oppBoard = copy.deepcopy(newBoard)
                        if oppBoard.validMove(move):
                            oppBoard.move(oppTurn, move)
                        if oppBoard.winner(oppTurn):
                            possible[move] = -10
                            return possible
                        else:
                            values = oppBoard.getMoves(oppTurn, depth - 1)
                            possible[move] += (sum(values) / oppBoard.width) / oppBoard.width

        return possible

    def getScore(self, turn):
        count = 0
        maxCount = 0
        for j in range(self.width - 1):
            for i in range((self.connect - 1)):
                if self.board[i][j] == turn:
                    count += 1
                if self.board[i+1][j] == turn:
                    count += 1
                if self.board[i+2][j] == turn:
                    count += 1 
                if self.board[i+3][j] == turn:
                    count += 1
            if count > maxCount:
                maxCount = count
                count = 0    
        for i in range(self.height):
            for j in range((self.connect - 1)):
                if self.board[i][j] == turn:
                    count += 1
                if self.board[i][j+1] == turn:
                    count += 1
                if self.board[i][j+2] == turn: 
                    count += 1
                if self.board[i][j+3] == turn:
                    count += 1
            if count > maxCount:
                    maxCount = count
                    count = 0              
        for i in range(5,2,-1):
            for j in range((self.connect - 1)):
                if self.board[i][j] == turn:
                    count += 1
                if self.board[i-1][j+1] == turn:
                    count += 1
                if self.board[i-2][j+2] == turn:
                    count += 1
                if self.board[i-3][j+3] == turn:
                    count += 1
            if count > maxCount:
                    maxCount = count
                    count = 0      
        for i in range((self.connect - 1)):
            for j in range(self.width - (self.connect - 1)):
                if self.board[i][j] == turn:
                    count += 1
                if self.board[i+1][j+1] == turn:
                    count += 1
                if self.board[i+2][j+2] == turn:
                    count += 1
                if self.board[i+3][j+3] == turn:
                    count += 1
        if count > maxCount:
                    maxCount = count
                    count = 0            
        if count == 1:
            return 1
        if count == 2:
            return 3
        if count == 3:
            return 6
        if count == 4:
            return 10
        return count


game = game()
player1 = ' R '
player2 = ' B '
turn = player1
tie = False
winner = False
while not winner and not tie:
    if turn == player2:
        move = game.AImove(turn)
        game.move(turn, move)
        game.printBoard()
        winner = game.winner(turn)
    else:
        move = game.askPlayer()
        game.move(turn, move)
        winner = game.winner(turn)
        game.printBoard()
    if turn == player1:
        turn = player2
    else:
        turn =  player1
