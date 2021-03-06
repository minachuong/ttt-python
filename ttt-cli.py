# print(u'\u2550')
# print(u'\u2551')
# print(u'\u2554')
# print(u'\u2557')
# print(u'\u255A')
# print(u'\u255D')
# print(u'\u2560')
# print(u'\u2563')
# print(u'\u2566')
# print(u'\u2569')
# print(u'\u256C')

horizontal_line = u'\u2550'
vertical_line = u'\u2551'
top_left_corner = u'\u2554'
top_right_corner = u'\u2557'
bottom_left_corner = u'\u255A'
bottom_right_corner = u'\u255D'
left_intersect = u'\u2560'
right_intersect = u'\u2563'
top_intersect = u'\u2566'
bottom_intersect = u'\u2569'
middle_intersect =  u'\u256C'

p = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

players = { "First" : "X", "Second" : "O" }

winner = False

# Board
def print_board():
		print(top_left_corner + horizontal_line + top_intersect + horizontal_line + top_intersect + horizontal_line + top_right_corner)
		print(vertical_line + p[0] + vertical_line + p[1] + vertical_line + p[2] + vertical_line)
		print(left_intersect + horizontal_line + middle_intersect + horizontal_line + middle_intersect + horizontal_line + right_intersect)
		print(vertical_line + p[3] + vertical_line + p[4] + vertical_line + p[5] + vertical_line)
		print(left_intersect + horizontal_line + middle_intersect + horizontal_line + middle_intersect + horizontal_line + right_intersect)
		print(vertical_line + p[6] + vertical_line + p[7] + vertical_line + p[8] + vertical_line)
		print(bottom_left_corner + horizontal_line + bottom_intersect + horizontal_line + bottom_intersect + horizontal_line + bottom_right_corner)

print_board()

turn_counter = 1

def user_input(turn_counter):
		if (turn_counter % 2 != 0):
				player = "First"
		else:
				player = "Second"

		user = int(raw_input(player + " Player: Mark your position: "))

		if (p[user - 1] == "X" or p[user - 1] == "O"):
				print("Please choose an unmarked position.")
				user_input(turn_counter)
		else:
				if (turn_counter % 2 != 0):
						p[user - 1] = "X"
				else:
						p[user - 1] = "O"

				print_board()
				check_winner(p, player)

def check_winner(marked_array, player):
	if (all(x == players[player] for x in [p[0],p[1],p[2]]) or all(x == players[player] for x in [p[3],p[4],p[5]]) or all(x == players[player] for x in [p[6],p[7],p[8]]) or all(x == players[player] for x in [p[0],p[3],p[6]]) or all(x == players[player] for x in [p[1],p[4],p[7]]) or all(x == players[player] for x in [p[2],p[5],p[8]]) or all(x == players[player] for x in [p[0],p[4],p[8]]) or all(x == players[player] for x in [p[2],p[4],p[6]])):
		print(player.upper() + " PLAYER WINS!")
		# end game
		global winner
		winner = True

x = 0
while(x < 9 and winner == False):
		user_input(turn_counter)
		turn_counter = turn_counter + 1
		x += 1
