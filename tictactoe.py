#GV


board = ["-","-","-",
				"-","-","-",
					"-","-","-",]
					
game_still_going = True


winner = None

current_player = "X"
					
					

def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn(current_player):
	print(current_player + "'s turn ")
	print()
	#get position
	position = input("Choose a position from 1 - 9: ")
	
	valid = False
	
	while not valid:
		while position not in ['1','2','3','4','5','6','7','8','9']:
			print()
			position = input("Invalid input only from 1 - 9 please.")
			print()
		
		position = int(position) - 1
		
		
		
		if board[position] == "-":
			valid = True
		else:
			print()
			print(current_player + " cheated but yeh...")
			print()
		
		board[position] = current_player
		display_board()

def check_if_tie():
	global game_still_going
	if "-" not in board:
		print("Tie")
		game_still_going == False
	return
	
	
	
def flip_player():
	global current_player
	if current_player == "X":
		current_player = "O"
	elif current_player == "O":
		current_player = "X"
	
	

def checkrow():
	global game_still_going
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"
	if row_1 or row_2 or row_3:
		game_still_going = False
	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]
def checkcol():
	global game_still_going
	col1 = board[0] == board[3] == board[6] != "-"
	col2= board[1] == board[4] == board[7] != "-"
	col3 = board[2] == board[5] == board[8] != "-"
	if col1 or col2 or col3:
		game_still_going = False
	if col1:
		return board[0]
	elif col2:
		return board[1]
	elif col3:
		return board[2]


def checkdiag():
	global game_still_going
	d1 = board[0] == board[4] == board[8] != "-"
	d2 = board[6] == board[4] == board[2] != "-"
	if d1 or d2:
		game_still_going = False
	if d1:
		return board[0]
	elif d2:
		return board[1]
	



def check_if_win():
	#ch row
	global winner
	
	Rowwin = checkrow()
	#ch col
	Colwin = checkcol()
	#ch diagonals
	Diagwin = checkdiag()
	
	if Rowwin:
		winner = Rowwin
		
	elif Diagwin:
		winner = Diagwin
	elif Colwin:
		winner = Colwin
	else:
		winner = None
		
	
	

	
	


def check_if_game():
	check_if_win()
	check_if_tie()
	
	




def play_game():
	#Display initial board
	display_board()
	
	#while game is on
	while game_still_going:
	
		handle_turn(current_player)
		
		
		#check game
		
		
		check_if_game()
		
		#flip
		
		flip_player()
		
		#ended
		if winner == "X" or winner == "O":
			print()
			print(winner + " won.")
			
		elif winner == None:
			check_if_tie()
			
	
	
	
	
	

	
	
play_game()
	


#board
#display
#play
#turn
# check win
	#check rows
		#check col
#checm tie
#flip
