#!/usr/bin/python
from __future__ import print_function
from boardclass import Board
from blockclass import *


class Gameplay(Board,Block): #defining gameplay class

	def __init__(self):
		Board.__init__(self)
		Block.__init__(self)
		self._board = [[' ']*30 for _ in range(32)] #making board array all empty
		self.__score = 0 #initializing score to zero
	
	def getscore(self): # method to return private variable
		return self.__score

	def __checkRowFull(self): #for removing filled rows
		fullrows = []
		for l in range(32):
			count = 0 ;
			for k in self._board[l]:
				if k is not 'X':
					break
				else:
					count+=1
			if count is 30 :
				fullrows.append(l)
		rowsremoved = len(fullrows)
		for index in sorted(fullrows, reverse = True):
			del self._board[index]
		newrow = [' ' for _ in range(len(self._board[0]))]
		for i in range(rowsremoved):
			self._board.insert(0,newrow)
		return len(fullrows)

	def checkRowEmpty(self): #for wall
		try:
			emptyrows = []
			for l in range(32):
				count = 0 ;
				for k in self._board[l]:
					if k is not ' ':
						break
					else:
						count+=1
				if count is 30 :
					emptyrows.append(l)
			for index in sorted(emptyrows, reverse = True):
				selectedrow = emptyrows[15]
			walllength = random.randrange(16,20)
			newrow = []
			cases = random.randrange(1,3)
			for i in range(30):
				if cases is 1:
					if i > walllength:
						newrow.append(' ')
					else:
						newrow.append('W')
				else:
					if i > walllength:
						newrow.append('W')
					else:
						newrow.append(' ')

			del self._board[selectedrow]
			self._board.insert(selectedrow-1,newrow)
			return 1
		except:
			return 0
			pass

	def addsemifilled(self): # adds a semi filled row at bottom
		del self._board[0]
		newrow = []
		walllength = random.randrange(16,20)
		newrow = []
		cases = random.randrange(1,3)
		for i in range(30):
			if cases is 1:
				if i > walllength:
					newrow.append(' ')
				else:
					newrow.append('X')
			else:
				if i > walllength:
					newrow.append('X')
				else:
					newrow.append(' ')
		self._board.append(newrow)

	def updateScore(self): # score update
		self.__score += 10 + self.__checkRowFull() * 100 ;

	def printBoard(self): # printing board in test phase
		print('+',end="")
		for i in range(30):
			print('-',end="")
		print('+',end="\n")
		for i in range(32):
			print('|',end="")
			for j in self._board[i]:
				print(j,end="")
			print('|',end="\n")
		print('+',end="")
		for i in range(30):
			print('-',end="")
		print('+',end="\n")