
class C4Board():
	
	def __init__(self,players = 2, lineLength = 4, height = 6, width = 7):

		# this board is column major
		self.board = []
		for i in range(width):
			self.board.append([0] * height)
		
		self.height = height
		self.width = width
		self.maxPlayer = players
		self.currentPlayer = 1
		self.lineLength = lineLength

		# "height" of the tokens at the i-th column
		self.heights = [0] * width

	def updatePlayer(self):

		self.currentPlayer+=1
		if self.currentPlayer > self.maxPlayer:
			self.currentPlayer = 1
		
	def addPiece(self,column,player):
		
		if self.height[column] >= 6:
			print('Invalid insert')
		
		else:
			self.board[column][self.height[column]] = player
			self.heights[column] += 1
	
	def detectLine(self):
		dx = [-1, -1, -1, 0, 0, 1, 1, 1]
		dy = [-1, 0, 1, -1, 1, -1, 0, 1]
		for width in range(self.width):
			for height in range(self.height):
				# no player has placed a thing on this cell
				if self.board[width][height] == 0:
					continue
				for i in range(8):
					line_success = True
					# check for line?
	
	def score(self):
		score_table = []
		for i in range(self.width):
			score_table.append([0] * self.height)

		dx = [-1, -1, -1, 0, 0, 1, 1, 1]
		dy = [-1, 0, 1, -1, 1, -1, 0, 1]
		for width in range(self.width):
			for height in range(self.height):
				for i in range(8):
					# idk, do something here?
					continue
		
		print(score_table)

a = C4Board()
a.score()