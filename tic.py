board=['-','-','-','-','-','-','-','-','-']
player='O'
gameIsStillGoingOn=True
winner=None

def winCheck():
	if((board[0]==board[1]==board[2]!='-') or (board[3]==board[4]==board[5]!='-') or (board[6]==board[7]==board[8]!='-') or (board[0]==board[3]==board[6]!='-') or (board[1]==board[4]==board[7]!='-') or (board[2]==board[5]==board[8]!='-') or (board[0]==board[4]==board[8]!='-') or (board[2]==board[4]==board[6]!='-')):
		global gameIsStillGoingOn
		winner=player
		gameIsStillGoingOn=False
		print("The winner is : ",winner)
		return 1
	else:
		return 0

def drawCheck():
	if(('-' not in board) and (winCheck()!=1) ):
		global gameIsStillGoingOn
		print("Draw!")
		gameIsStillGoingOn=False

def switch():
	global player
	if(player=='O'):
		player='X'
	elif(player=='X'):
		player='O'


def printbrd():
	for i in range(len(board)):
		if (i==2 or i==5 or i==8):
			print(board[i])
		else:
			print(board[i],"|",end='')

printbrd()

while gameIsStillGoingOn:
	print("\nIt's "+ player + " turn")
	position=(int(input("Enter a number(1--9):"))) - 1
	if(board[position]=='-'):
		board[position]=player
		winCheck()
		drawCheck()
		switch()
	else:
		print("Oops,Already taken!")
	printbrd()
	
	


