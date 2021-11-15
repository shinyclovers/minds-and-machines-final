
class C4Board():
    def __init__(self):
       self.board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
       self.activePlayer = 1
       # index [0][0] is the bottom row left most corner
    def addPiece(self,column):
      for x in self.board:
          if x[column] == 0:
              x[column] = self.activePlayer
              if self.activePlayer == 1:
                  self.activePlayer +=1
              else:
                  self.activePlayer -= 1
                

