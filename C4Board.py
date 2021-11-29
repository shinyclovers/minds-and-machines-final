
class C4Board():
	
	def __init__(self,players = 2, height = 6, width = 7):

		# this board is column major
		self.board = []
		self.height = height
		self.width = width
		self.maxPlayer = players
		self.currentPlayer = 1

		for i in range(width):
			self.board.append([0] * height)
		
		# "height" of the tokens at the i-th column
		self.height = [0] * width
	def updatePlayer(self):
		pastPlayer = self.currentPlayer
		self.currentPlayer+=1
		# if self.currentPlayer > 1
	def addPiece(self,column,player):
		
		if self.height[column] >= 6:
			print('Invalid insert')
		
		else:
			self.board[column][self.height[column]] = player
			self.height[column] += 1
	
	def detectLine(self):
		for width in range(self.width):
			for height in range(self.height):
				# [width][height]
				if not width < 3:
					count = 0
					for x in range(width):
						if self.board[width][height] == self.currentPlayerplayer:
							1
					
				
				

		
		