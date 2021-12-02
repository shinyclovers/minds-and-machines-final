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

		self.score_table = []
		for i in range(self.width):
			self.score_table.append([0] * self.height)

		dx = [-1, -1, -1, 0, 0, 1, 1, 1]
		dy = [-1, 0, 1, -1, 1, -1, 0, 1]
		for width in range(self.width):
			for height in range(self.height):
				for i in range(8):
					if width + dx[i] * (self.lineLength - 1) < 0 or width + dx[i] * (self.lineLength - 1) >= self.width or height + dy[i] * (self.lineLength - 1) < 0 or height + dy[i] * (self.lineLength - 1) >= self.height:
						continue
					for j in range(self.lineLength - 1):
						self.score_table[width + j * dx[i]][height + j * dy[i]] += 1 

		# "height" of the tokens at the i-th column
		self.heights = [0] * width

	def updatePlayer(self):

		self.currentPlayer+=1
		if self.currentPlayer > self.maxPlayer:
			self.currentPlayer = 1
		
	def addPiece(self,column,player):
		
		if self.heights[column] >= self.height:
			print('Invalid insert')
		
		else:
			self.board[column][self.heights[column]] = player
			self.heights[column] += 1
	
	def findWinner(self):
		dx = [-1, -1, -1, 0, 0, 1, 1, 1]
		dy = [-1, 0, 1, -1, 1, -1, 0, 1]
		for width in range(self.width):
			for height in range(self.height):
				# no player has placed a thing on this cell
				if self.board[width][height] == 0:
					continue
				for i in range(8):
					line_success = True
					if width + dx[i] * (self.lineLength - 1) < 0 or width + dx[i] * (self.lineLength - 1) >= self.width or height + dy[i] * (self.lineLength - 1) < 0 or height + dy[i] * (self.lineLength - 1) >= self.height:
						continue
					for j in range(self.lineLength - 1):
						if self.board[width + j * dx[i]][height + j * dy[i]] == self.board[width][height]:
							line_success = False
					if line_success:
						return self.board[width][height]
		return -1
	
	def score(self):
		init_score = sum([sum(l) for l in self.score_table])
		scores = [init_score] * self.maxPlayer
		for width in range(self.width):
			for height in range(self.height):
				for i in range(self.maxPlayer):
					if self.board[width][height] == (i + 1):
						scores[i] += self.score_table[width][height]
					else:
						scores[i] -= self.score_table[width][height]
		return scores
	
	def bestMove(self, player):
		# do implementation here
		print("NOT DONE YET")

if __name__ == "__main__":
	a = C4Board()
	bot_player = input("Is the computer player 1 or player 2?: ")
	while not (bot_player == "1" or bot_player == "2"):
		bot_player = input("Invalid input.\nIs the computer player 1 or player 2?: ")
	bot_player = int(bot_player)
