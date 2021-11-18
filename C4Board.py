
class C4Board():
	
	def __init__(self, height = 6, width = 7):

		# this board is column major
		self.board = []

		for i in range(width):
			self.board.append([0] * height)
		
		# "height" of the tokens at the i-th column
		self.height = [0] * width

	def addPiece(self,column,player):
		
		if self.height[column] >= 6:
			print('Invalid insert')
		
		else:
			self.board[column][self.height[column]] = player
			self.height[column] += 1
	
	def winner(self):
		
		