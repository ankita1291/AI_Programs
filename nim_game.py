

import random as rand

class Board():
    def __init__(self):
        self.rows = []
        self.maxSticks = 5 # this is actually the max bits
        self.defaultBoard = [7, 5, 3]

    def getGameSettings(self):
        self.rows = self.defaultBoard

    def displayPosition(self):        
        for r in range(len(self.rows)):
            row = self.rows[r]
            s = ['|' for i in range(row)]
            s = ''.join(s)
            template = '{0:15}{1:40}{2:50}'
            s1 = '| row {} :'.format(r)
            s2 = '({} sticks)'.format(row)

            print(template.format(s1, s, s2))

    def checkGameWon(self):
        return sum(self.rows) == 0

    def take(self, s, r):
        if(self.rows[r] >= s):
            self.rows[r] -= s
            return True
        else:
            return False

    def reverseTake(self, s, r):
        self.rows[r] += s


def checkParity(board):
    # initialize to parity 0
    parity = [0 for i in range(board.maxSticks)]
    for row in board.rows:
        # binary representation of row
        form = '{' + '0:0{}b'.format(board.maxSticks) + '}'
        b = form.format(row)
        for i in range(board.maxSticks):
            parity[i] += int(b[i])

    s = []
    for p in parity:
        if p%2 == 0:
            s.append('0')
        else:
            s.append('1')

    return ''.join(s)

def parityEven(board):
    return int(checkParity(board), 2) == 0



def computerMove(board):
    for r in range(len(board.rows)):
        for i in range(board.rows[r]):
            s = i+1
            # try the move to take i sticks from r
            board.take(s, r)
            if parityEven(board):    
                print('Computer made move: {},{}'.format(s, r))

                if(board.checkGameWon()):
                    print('#                            You win!                                 #')
                    board.displayPosition()
                    return True
                else:
                    board.displayPosition()
                return False
            # if not, simply reverse the move, and try the next one.
            else:
                board.reverseTake(s, r)
    while True:
        # pick random row
        r = rand.randint(0, len(board.rows))
        # if it has more then one stick
        if board.rows[r] >= 1:
            # take a random amount of these sticks
            s = rand.randint(1, board.rows[r])
            board.take(s, r)
            print('Computer made move: {},{}'.format(1, r))
            board.displayPosition()

            return False

def playerMove(board):
    while True:
        try:
            playerMove = input('Enter next move: ') 
            m = playerMove.split(',')
            s = int(m[0])
            r = int(m[1])

            if r < len(board.rows) and s <= board.rows[r]:
                board.take(s, r)
                break
            else:
                print('Invalid move')

        except Exception:
            print('Invalid input, try again. Valid input:<sticks,row>')
   
    if(board.checkGameWon()):
        print('#                            You win!                                 #')
        board.displayPosition()
        return True
    else:
        board.displayPosition()
        return False

def main():
    board = Board()
    board.getGameSettings()
    # display the board position
    print('| Moves on form  : <sticks,row>  : will take #sticks from r:th row')
    print('| Example        : <3,0>         : 3 sticks will be taken from row 0.')
    print('|')

    board.displayPosition()
    playerWon = False
    computerWon = False

    # game main loop, loop until either player or computer has won
    while not playerWon and not computerWon:
        playerWon = playerMove(board)
        computerWon = computerMove(board)

if __name__ == "__main__":
    main()