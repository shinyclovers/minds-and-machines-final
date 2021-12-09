
class C4Board():
	
	def __init__(self, board = None, lineLength = 4, height = 6, width = 7, curPlayer = 1):

		# this board is column major
		if board is None:

			self.height = height
			self.width = width
			
			self.board = []
			for i in range(width):
				self.board.append([0] * height)
			
			# "height" of the tokens at the i-th column
			self.heights = [0] * width
		else:
			self.board = [col[:] for col in board]
			self.width = len(self.board)
			self.height = len(self.board[0])
			self.heights = [0] * self.width
			for i in range(self.width):
				for j in range(self.height):
					if self.board[i][j] != 0:
						self.heights[i] += 1

		# initialize member variables
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
			tmpBoard = C4Board(self.board)

			if not tmpBoard.addPiece(i):
				continue
			
			if tmpBoard.findWinner() == self.currentPlayer:
				# return a winning move
				return i
			
			else:
				# store down the current score we get
				bestMoveScore[i] = tmpBoard.score()[self.currentPlayer - 1]
		
		# find the best move of all of them and return it
		return bestMoveScore.index(max(bestMoveScore))

	def bestMoveBruteForce(self, player, depth = 5, best = -2147483648, worst = 2147483647, maximizing = True):
		
		# base cases
		if depth == 0:
			return (-1, self.score()[player - 1])
		
		if not self.findWinner() == -1:
			if self.findWinner() == player:
				return (-1, 1000)
			else:
				return (-1, -1000)
		
		if maximizing:
			val = -2147483647
			best_move = -1
			for i in range(self.width):
				tmp_board = C4Board(self.board)
				if tmp_board.addPiece(i):
					bf_score = tmp_board.bestMoveBruteForce(player, depth - 1, best, worst, False)[1]
					if bf_score > val:
						val = bf_score
						best_move = i
					if val >= worst:
						break
					best = max(best, val)
			return (best_move, val)
		else:
			val = 2147483648
			best_move = -1
			for i in range(self.width):
				tmp_board = C4Board(self.board)
				if tmp_board.addPiece(i):
					bf_score = tmp_board.bestMoveBruteForce(player, depth - 1, best, worst, True)[1]
					if bf_score < val:
						val = bf_score
						best_move = i
					if val <= best:
						break
					best = min(best, val)
			return (best_move, val)


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
			res = a.bestMoveBruteForce(bot_player)[0]
			if res == -1:
				print('Bot surrenders')
				break
			print('Bot plays column {}'.format(res))
			a.addPiece(res)
		else:
			ok = False
			while not ok:
				col = int(input("Which column do you want to insert the tile in: "))
				if not a.addPiece(col):
					print("Invalid insert")
				else:
					ok = True
	# print(a)
	print(a,'\n\nPlayer {} won!'.format(a.findWinner()))