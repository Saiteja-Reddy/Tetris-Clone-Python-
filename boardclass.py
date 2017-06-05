#!/usr/bin/python

class Board(): #defining board class

	def __init__(self):
		self._board = [[' ']*30 for _ in range(32)]
		pass

	def checkPiecePos(self,row,col,piece): #method for checking piece position if valid or not
		for (x,y) in piece._curr:
			self._board[x][y] = ' '
		for i in range(piece._coori[0],piece._coorf[0]+1):
			for j in range(piece._coori[1],piece._coorf[1]+1):
				# print (str(i+row-piece._coori[0]) + " , " + str(j+col-piece._coori[1]))
				if   ((self._board[i+row-piece._coori[0]][j+col-piece._coori[1]] in ['X','W'] )and (piece._block[i][j] in ['X','@'])) :
				 	return 0;
		return 1;

	def fillPiecePos(self,row,col,piece): # method for copying piece contents to board
		for (x,y) in piece._curr:
			self._board[x][y] = ' '
		piece._curr = []
		for i in range(piece._coori[0],piece._coorf[0]+1):
			for j in range(piece._coori[1],piece._coorf[1]+1):
				if piece._block[i][j] is 'X' :
						self._board[row+i-piece._coori[0]][j+col-piece._coori[1]] = 'X'
						# print(str(i+col) + " : " + str(j+row))
						piece._curr.append((row+i-piece._coori[0],j+col-piece._coori[1]))
				if piece._block[i][j] is '@' :
						self._board[row+i-piece._coori[0]][j+col-piece._coori[1]] = '@'
						# print(str(i+col) + " : " + str(j+row))
						piece._curr.append((row+i-piece._coori[0],j+col-piece._coori[1]))

	def clearcolumn(self,no): # method to clear a cloumn by column number for special block
		for i in range(32):
			self._board[i][no[1]]=' '
			self._board[i][no[1]+1]=' '