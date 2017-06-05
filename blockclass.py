#!/usr/bin/python
from __future__ import print_function
import random

class Block(): # class for all blocks
	
	def __init__(self):
		self._block = [['X']*4 for _ in range(4) ]
		self._posx = -1;
		self._posy = 15;
		self._curr = []

	def getpos(self): # return's protected variables
		return (self._posx,self._posy)

	def rotate(self,game): # for rotating the block
		preblock = self._block
		self._block = zip(*self._block[::-1])
		self.cords = self._getcoords()
		self._coori = self.cords[0]
		self._coorf = self.cords[1]
		try:	
			if game.checkPiecePos(self._posx,self._posy,self):
				game.fillPiecePos(self._posx,self._posy,self)
			else:
				self._block = preblock
				self.cords = self._getcoords()
				self._coori = self.cords[0]
				self._coorf = self.cords[1]
				game.fillPiecePos(self._posx,self._posy,self)
		except:
				self._block = preblock	
				self.cords = self._getcoords()
				self._coori = self.cords[0]
				self._coorf = self.cords[1]
				game.fillPiecePos(self._posx,self._posy,self)

	def fill(self,game): # for filling block at a position in board
		game.fillPiecePos(self._posx,self._posy,self)

	def moveLeft(self,game): # move block left by one unit
		try: 
			if game.checkPiecePos(self._posx,self._posy-1,self) and self._posy > 0 :
				game.fillPiecePos(self._posx,self._posy-1,self)
				self._posy -= 1
			else:
				game.fillPiecePos(self._posx,self._posy,self)
		except:
			game.fillPiecePos(self._posx,self._posy,self)
			pass
		
	def moveRight(self,game): # move block right by one unit
		try:
			if game.checkPiecePos(self._posx,self._posy+1,self) and self._posy < 29 :
				game.fillPiecePos(self._posx,self._posy+1,self)
				self._posy += 1
		except:
			game.fillPiecePos(self._posx,self._posy,self)
			pass

	def draw(self,game): # move block down by one unit
		try:
			if game.checkPiecePos(self._posx+1,self._posy,self):
				# print("Yes")
				game.fillPiecePos(self._posx+1,self._posy,self)
				self._posx += 1
				return 1
			else:
				game.fillPiecePos(self._posx,self._posy,self)
				return 0
		except:
			game.fillPiecePos(self._posx,self._posy,self)
			return 0
			pass

	def goEnd(self,game): # go to the end of board for drop
		try:
			while self.draw(game):
				pass
		except:
			pass

	def newblock(self,num): # to select a random block
		# randnum = random.randrange(1,8)
		blocks = { 1: BlockLine , 2 : BlockBlock , 3 : BlockZ , 4 : BlockS , 5 : BlockL , 6 : BlockJ , 7 : BlockT , 8: BlockSpecial}
		# return blocks[randnum]()
		selectedblock = blocks[num]()
		selectedblock.defineblock()
		return selectedblock

	def _getcoords(self): # protected functions which gets self._cords
		coor1 = [5,5]
		coor2 = [-1,-1]
		for i in range(4):
			for j in range(4):
				if self._block[i][j] != ' ':
					if coor1[0] > i :
						coor1[0] = i
					if coor1[1] > j :
						coor1[1] = j
					if coor2[0] < i:
						coor2[0] = i
					if coor2[1] < j:
						coor2[1] = j
		return [coor1,coor2]

	def getcoords(self): # overloaded method which sends coordinates which are protected
		return [self._coori,self._coorf]

	def defineblock(self): # define block here , for polymorphism 
		pass


class BlockLine(Block):
	
	def __init__(self):

		Block.__init__(self)

	def defineblock(self): # polymorphic method fo redefining block 
		self._block =[
		          [' ',' ',' ',' '],
			      ['X','X','X','X'],
			      [' ',' ',' ',' '],
			      [' ',' ',' ',' '],
			     ]
		self.cords = self._getcoords()
		self._coori = self.cords[0]
		self._coorf = self.cords[1]

class BlockBlock(Block):
	
	def __init__(self):

		Block.__init__(self)

	def defineblock(self): # polymorphic method fo redefining block 
		self._block =[
		              [' ',' ',' ',' '],
			      [' ','X','X',' '],
			      [' ','X','X',' '],
			      [' ',' ',' ',' '],
			     ]
		self.cords = self._getcoords()
		self._coori = self.cords[0]
		self._coorf = self.cords[1]

class BlockZ(Block):
	
	def __init__(self):

		Block.__init__(self)

	def defineblock(self): # polymorphic method fo redefining block 
		self._block =[ 
		       	  [' ',' ',' ',' '],
			      [' ','X','X',' '],
			      [' ',' ','X','X'],
			      [' ',' ',' ',' '],
			     ]
		self.cords = self._getcoords()
		self._coori = self.cords[0]
		self._coorf = self.cords[1]

class BlockS(Block):
	
	def __init__(self):

		Block.__init__(self)
 
	def defineblock(self): # polymorphic method fo redefining block 
		self._block =[
		          [' ',' ',' ',' '],
			      [' ',' ','X','X'],
			      [' ','X','X',' '],
			      [' ',' ',' ',' '],
			      ]
		self.cords = self._getcoords()
		self._coori = self.cords[0]
		self._coorf = self.cords[1]

class BlockL(Block):
	
	def __init__(self):

		Block.__init__(self)

	def defineblock(self): # polymorphic method fo redefining block 
		self._block =[
				  [' ',' ',' ',' '],
			      [' ','X',' ',' '],
			      [' ','X','X','X'],
			      [' ',' ',' ',' '],
			     ]
		self.cords = self._getcoords()
		self._coori = self.cords[0]
		self._coorf = self.cords[1]

class BlockJ(Block):
	
	def __init__(self):

		Block.__init__(self)

	def defineblock(self): # polymorphic method fo redefining block 
		self._block =[
				  [' ',' ',' ',' '],
			      [' ',' ',' ','X'],
			      [' ','X','X','X'],
			      [' ',' ',' ',' '],
			     ]
		self.cords = self._getcoords()
		self._coori = self.cords[0]
		self._coorf = self.cords[1]

class BlockT(Block):
	
	def __init__(self):

		Block.__init__(self)

	def defineblock(self): # polymorphic method fo redefining block 
		self._block=[
		          [' ',' ',' ',' '],
			      [' ','X','X','X'],
			      [' ',' ','X',' '],
			      [' ',' ',' ',' '],
			     ]
		self.cords = self._getcoords()
		self._coori = self.cords[0]
		self._coorf = self.cords[1]

class BlockSpecial(Block):
	
	def __init__(self):

		Block.__init__(self)

	def defineblock(self): # polymorphic method fo redefining block 
		self._block=[
		          [' ',' ',' ',' '],
			      [' ','@','@',' '],
			      [' ','@','@',' '],
			      [' ',' ',' ',' '],
			     ]
		self.cords = self._getcoords()
		self._coori = self.cords[0]
		self._coorf = self.cords[1]