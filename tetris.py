#!/usr/bin/python
import curses
import time
from gameplayclass import Gameplay
from boardclass import Board
from blockclass import *
import random
import sys
import time
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=60)) # resizing terminal for proper view

curses.initscr() #create win
win = curses.newwin(38,60,1,1)
wins = win.subwin(36,32,1,1)
wins1 = win.subwin(34,32,3,1)
wins2 = win.subwin(34,55,3,1)
win.keypad(1)
win.nodelay(1)
curses.noecho()
curses.curs_set(0)
level = 1 # global variable for menu window
levelarray = { 0:1 , 1:2 , 2:3 , 3:4 , 4:5 , 5:6 , 6:7 , 7:"MAX"} # ranges of global variable level

def game(input_level): # main game window
	win.clear()
	win.nodelay(1)
	win.border('|',' ',' ',' ',' ',' ',' ', ' ')
	wins.border('|','|',' ','^')
	wins1.border('|','|','_','^')
	win.addstr(1,9,'TETRIS - By Teja', curses.A_BOLD )
	newgame = Gameplay()
	nextblock = random.randrange(1,8)
	currblock = newgame.newblock(nextblock)
	speeds = { 1 : 500 , 2 : 400 , 3 : 300 , 4 : 250 , 5 : 200 , 6 : 150 , 7 : 100 , "MAX" : 50 }
	level = input_level
	speed = speeds[level]
	gameover = False
	addedwall = False
	superblock = False
	start = time.time()
	while not gameover : # main game loop

		speed = speeds[level]
		go_down = currblock.draw(newgame)
		# win.refresh()
		k = 1
		l = 1
		for i in newgame._board:
			k+=1
			l = 0
			for j in i:
				l+=1
				if j == '@':
					win.addstr(1+k,1+l-1,j,curses.A_BOLD)
				else:
					win.addstr(1+k,1+l-1,j) # (x,y,string,attributes*)

		if go_down == 0 :
			if currblock.getpos()[0] == -1 :
				gameover = True
				break
				
			# * Semi Filled Row
			# if newgame.getscore() % 100 is 0 and newgame.getscore()!= 0 :
			# 	newgame.addsemifilled()

			if superblock == True:
				newgame.clearcolumn(currblock.getpos())
				curses.flash()
			if superblock == False:
				currblock.fill(newgame)
			if superblock == True:
				superblock = False
			newgame.updateScore()

			if newgame.getscore() % 200 is 0 and newgame.getscore()!= 0 :
				if level is 7:
					level = "MAX"
				elif level is not "MAX" :
					level += 1
				if level in [6,7,"MAX"] :
					if addedwall == False:
						isadded = newgame.checkRowEmpty() #add wall
						if isadded:
							addedwall = True
							curses.flash()

			currblock = newgame.newblock(nextblock)
			if nextblock == 8:
				superblock = True
			nextblock = random.randrange(1,8)
			
			#  * Special Block
			# if level in [6,7,'MAX'] and newgame.getscore() % 100 is 0 and newgame.getscore()!= 0 :
			# 	nextblock = 8 

			currblock.draw(newgame)

		# win.refresh()
		action = win.getch()
		if action == curses.KEY_UP or action == 115 :
			currblock.rotate(newgame)
		elif action == curses.KEY_DOWN :
			pass
		elif action == curses.KEY_RIGHT or action == 100:
			currblock.moveRight(newgame)
		elif action == curses.KEY_LEFT or action == 97:
			currblock.moveLeft(newgame)
		elif action == 32:
			currblock.goEnd(newgame)
		elif action == 113 :
			break

		win.addstr(36,9,'  SCORE  : ' + str(newgame.getscore()) ,  curses.A_BOLD )

		win.addstr(5,39,'Next Block' ,  curses.A_BOLD | curses.A_UNDERLINE )
		k = 4
		l = 37
		nextup = newgame.newblock(nextblock)
		for i in nextup._block:
			k+=1
			l = 40
			for j in i:
				l+=1
				win.addstr(1+k,1+l-1,j)
		del nextup
		end = time.time()
		m, s = divmod(end - start, 60)
		h, m = divmod(m, 60)
		win.addstr(10,34,'Time Elapsed : ' + "%d:%02d:%02d" % (h, m, s) , curses.A_BOLD)
		win.addstr(12,38,'Level  : ' + str(level) ,  curses.A_BOLD)

		win.addstr(15,42,'Controls' ,  curses.A_BOLD | curses.A_UNDERLINE )
		win.addstr(17,37,'    A/<- : Left ')
		win.addstr(18,37,'    D/-> : Right ')
		win.addstr(19,37,'    S/Up : Rotate ')
		win.addstr(20,37,'    Down : Speed Up ')
		win.addstr(21,37,'   Space : Drop ')
		win.addstr(22,37,'     Q   : Quit ')
		win.refresh() #to see value
		# win.getch()#get command from keyboard
		win.timeout(speed)

	win.clear()
	wins2.border('|')
	win.nodelay(0)

	#defining game over screen
	message1 = 'Game Over!'
	message2 = 'Your Score was ' + str(newgame.getscore()) 
	message3 = 'Press Space to play again!'
	message4 = 'Press Enter to quit!'
	message5 = 'Press M for Main Menu'
	win.addstr(10,18,message1,curses.A_STANDOUT)
	win.addstr(12,16,message2,curses.A_BOLD | curses.A_UNDERLINE)
	win.addstr(14,13,message3)
	win.addstr(16,14,message5)
	win.addstr(18,14,message4)
	
	q = 0
	while q not in [32,10,109]:
		q = win.getch()
	if q == 32:
		win.clear()
		level = 1
		game(level)
	if q == 109:
		menu()

def menu(): # home menu screen
	win.nodelay(0)
	win.clear()
	wins.border()
	selection = -1
	option = 0
	levoption = 0

	while  selection < 0:
		graphics = [0]*4
		graphics[option] = curses.A_REVERSE
		win.addstr(6,13,"XXX",curses.A_BOLD)
		win.addstr(7,13,"X",curses.A_BOLD)
		win.addstr(10,12,"Tetris",curses.A_BOLD | curses.A_UNDERLINE)
		win.addstr(14,13,"Play" , graphics[0])
		win.addstr(15,9,"Instructions",graphics[1])
		if levoption != 7:
			win.addstr(16,8,"  Level : " + str(levoption+1) + "  " ,graphics[2])
		else:
			win.addstr(16,8,"  Level : MAX" ,graphics[2])
		win.addstr(17,13,"Exit",graphics[3])
		win.addstr(34,20,"--By Teja")
		win.refresh()

		action = win.getch()
		if action == curses.KEY_UP :
			option = (option -1 )%4
		elif action == curses.KEY_DOWN:
			option = (option +1 )%4
		elif action == ord('\n'):
			selection = option
		elif graphics[2] == curses.A_REVERSE :
			if action == curses.KEY_RIGHT :
				levoption = (levoption + 1)%8
			elif action == curses.KEY_LEFT:
				levoption = (levoption - 1)%8

	if selection == 3:
		curses.endwin()
	elif selection == 1:
		instructions()
	elif selection == 0 or 2:
		win.clear()
		game(levelarray[levoption])

def instructions(): # instructions menu
	win.nodelay(0)
	win.clear()
	wins.border()
	win.addstr(9,10,'Instructions' ,  curses.A_BOLD | curses.A_UNDERLINE )
	win.addstr(11,6,'Use the following keys')
	win.addstr(13,6,'    A/<- : Left ')
	win.addstr(14,6,'    D/-> : Right ')
	win.addstr(15,6,'    S/Up : Rotate ')
	win.addstr(16,6,'    Down : Speed Up ')
	win.addstr(17,6,'   Space : Drop ')
	win.addstr(18,6,'     Q   : Quit ')
	win.addstr(20,4,'Press any key to continue',curses.A_BOLD)
	q = win.getch()
	if q:
		menu()


menu() # calling menu window

curses.endwin() #close window

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=100)) # resizing terminal to default size
