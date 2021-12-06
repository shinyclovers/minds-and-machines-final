
class C4Board():
	
	def __init__(self, board = None, heights = None,lineLength = 4, height = 6, width = 7, curPlayer = 1):

		# this board is column major
		if board is None:
			self.board = []
			for i in range(width):
				self.board.append([0] * height)
			
			# "height" of the tokens at the i-th column
			self.heights = [0] * width
		else:
			self.board = [col[:] for col in board]
			self.heights = heights[:]

		# initialize member variables
		self.height = height
		self.width = width
		self.currentPlayer = curPlayer
		self.lineLength = lineLength

		# have a score table to see how good our move is
		self.scoreTable = []
		for i in range(self.width):
			self.scoreTable.append([0] * self.height)

		dx = [-1, -1, -1, 0, 0, 1, 1, 1]
		dy = [-1, 0, 1, -1, 1, -1, 0, 1]
		for width in range(self.width):
			for height in range(self.height):
				# loop through the 8 directions
				for i in range(8):
					if width + dx[i] * (self.lineLength - 1) < 0 or width + dx[i] * (self.lineLength - 1) >= self.width or height + dy[i] * (self.lineLength - 1) < 0 or height + dy[i] * (self.lineLength - 1) >= self.height:
						# at some point this direction will go out of bounds
						continue
					for j in range(self.lineLength - 1):
						self.scoreTable[width + j * dx[i]][height + j * dy[i]] += 1 


	def __repr__(self):
		return "Board State:\n" + '\n'.join([','.join([str(self.board[j][self.height - 1 - i]) for j in range(self.width)]) for i in range(self.height)])

	def updatePlayer(self):

		self.currentPlayer += 1
		if self.currentPlayer > 2:
			self.currentPlayer = 1
		
	def addPiece(self,column):

		if (not column in range(self.width)) or self.heights[column] >= self.height:
			print('Invalid insert')
			return False
		
		else:
			self.board[column][self.heights[column]] = self.currentPlayer
			self.heights[column] += 1
			self.updatePlayer()
			return True
	
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
					for j in range(self.lineLength):
						if not self.board[width + j * dx[i]][height + j * dy[i]] == self.board[width][height]:
							line_success = False
					if line_success:
						return self.board[width][height]
		return -1
	
	def score(self):
		init_score = sum([sum(l) for l in self.scoreTable])
		scores = [init_score] * 2
		for width in range(self.width):
			for height in range(self.height):
				for i in range(2):
					if self.board[width][height] == (i + 1):
						scores[i] += self.scoreTable[width][height]
					else:
						scores[i] -= self.scoreTable[width][height]
		return scores
	
	def bestMove(self):
		# do implementation here
		# initialize best scores
		bestMoveScore = [0] * self.width
		for i in range(self.width):
			# create a new board and test the moves
			tmpBoard = C4Board(self.board,self.heights)
			print(tmpBoard.addPiece(i))
			if not tmpBoard.addPiece(i):
				continue
			# tmpBoard.addPiece(i)
			if tmpBoard.findWinner == self.currentPlayer:
				# return a winning move
				return i
			else:
				# store down the current score we get
				bestMoveScore[i] = tmpBoard.score()[self.currentPlayer - 1]
		
		# find the best move of all of them and return it
		return bestMoveScore.index(max(bestMoveScore))


if __name__ == "__main__":
	a = C4Board()
	bot_player = input("Is the computer player 1 or player 2?: ")
	while not (bot_player == "1" or bot_player == "2"):
		bot_player = input("Invalid input.\nIs the computer player 1 or player 2?: ")
	bot_player = int(bot_player)

	while a.findWinner() == -1:
		print(a)
		print()
		if bot_player == a.currentPlayer:
			res = a.bestMove()
			print('Bot plays column {}'.format(res))
			a.addPiece(res)
		else:
			col = int(input("Which column do you want to insert the tile in: "))
			a.addPiece(col)
	# print(a)
	print(a,'\n\nPlayer {} won!'.format(a.findWinner()))