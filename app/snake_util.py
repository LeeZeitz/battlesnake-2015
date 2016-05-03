# Returns a boolean stating whether or not our snake is closest to any given pieces of food
# foods is a list of coordinate pairs (also in list form) of the food on the board
# snakes is a list of all snake objects on the board

# TO-DO: Implement corner function. Use maze style recursion with a list storing checked (free?) coordinates.

import random


# Old functions, to be fixed and used at a later time.
# To-do: use "==" instead of "is" keyword to correctly test equality instead of identity.
'''
def closestToFood(foods, snakes):
	if len(foods) > len(snakes):
		for food in foods:
			for snake in snakes:
				coords = snake["coords"]
				distance = abs(food[0] - coords[0][0]) + abs(food[1] - coods[0][1])

				if snake["name"] is our_name:
					our_distance = distance

				if our_distance in locals() and distance < our_distance:
					return False
	else:
		for snake in snakes:
			coords = snake["coords"]

			if snake["name"] is our_name:
				our_distance = 100

			for food in foods:
				distance = abs(food[0] - coords[0][0]) + abs(food[1] - coods[0][1])

				if our_distance in locals() and distance < our_distance:
					return False
	return True


# returns boolean stating whether or not there is an obstruction between our head and a coordinate
def obstruction(foods, snakes, dest, ourLoc):

	for snake in snakes:
		coords = snake["coords"]
		
		for coord in coords:
			x = coord[0]
			y = coord[1]

			if ourLoc[0] is dest[0]:
				if y in range(ourLoc[1], dest[1]).sort():
					return coords
			elif ourLoc[1] is dest[1]:
				if x in range(ourLoc[0], dest[0]).sort():
					return coords
'''

def closestFood(board):
	maxDistance = 1000;
	coords = []
	
	for food in board.foods:
		distance = abs(board.ourLoc[0] - food[0]) + abs(board.ourLoc[1] - food[1])
		
		if distance < maxDistance:
			maxDistance = distance
			coords = food

	return coords


# Returns true if the move will not kill us
def safe(board, move):
	
	if isinstance(move, str):
		dest = getDest(board,move)		
	else:
		dest = move

	danger = []
	
	for snake in board.snakes:
		coords = snake["coords"]
		danger = danger + coords
		
	if (dest in danger):
		return False
	elif (dest[1] > board.height - 1) or (dest[0] > board.width - 1) or (dest[0] < 0) or (dest[1] < 0):
		return False
	else:
		return True

def idealMove(board, move):
	if isinstance(move, str):
		dest = getDest(board,move)		
	else:
		dest = move

	if not safe(board, dest):
		return False
	elif headOnCollision(board, dest):
		return False
	else:
		return True


def altMove(board, attemptedMove, dest):
	distX = dest[0] - board.ourLoc[0]
	distY = dest[1] - board.ourLoc[1]

	possibility = ["north", "south", "east", "west"]
	priority = []

	if distX < 0 and attemptedMove != "west":
			priority.append("west")
	elif distX > 0 and attemptedMove != "east":
			priority.append("east")
	elif distY < 0 and attemptedMove != "north":
			priority.append("north")
	elif distY > 0 and attemptedMove != "south":
			priority.append("south")

	random.shuffle(possibility)
	
	for direction in possibility:
		if direction not in priority and direction != attemptedMove:
			priority.append(direction)
	
	for direction in priority:
		if idealMove(board, direction):
			return direction

	priority.insert(0, attemptedMove)

	print "no_ideal"

	for direction in priority:
		if safe(board, direction):
			return direction

	return "no_safe"


def findMove(board, dest):
	lastMove = getlastMove(board, board.ourSnake)

	distX = dest[0] - board.ourLoc[0]
	distY = dest[1] - board.ourLoc[1]

	rand = bool(random.getrandbits(1))

	if rand or (distY == 0):
		if distX < 0 and lastMove != "east":
			nextMove = "west"
		elif distX > 0 and lastMove != "west": 
			nextMove = "east"
		elif distY < 0 and lastMove != "south":
			nextMove = "north"
		elif distY > 0 and lastMove != "north":
			nextMove = "south"

	if not rand or (distX == 0):
		if distY < 0 and lastMove != "south":
			nextMove = "north"
		elif distY > 0 and lastMove != "north":
			nextMove = "south"
		elif distX < 0 and lastMove != "east":
			nextMove = "west"
		elif distX > 0 and lastMove != "west": 
			nextMove = "east"
	
	elif distY == 0 and distX == 0:
		nextMove = "north"

	return nextMove

def headOnCollision(board, dest):

	for snake in board.snakes:
		if snake is board.ourSnake:
			continue

		head = snake["coords"][0]
		diffX = abs(head[0] - dest[0])
		diffY = abs(head[1] - dest[1])
		length = getLength(snake)

		if (diffX + diffY == 1 ) and (length >= getLength(board.ourSnake)):
			return True

	return False

def getLength(snake):
	length = 0
	for coord in snake["coords"]:
		length = length + 1
	return length

def getDest(board, move):
	if move == "north":
		dest = [board.ourLoc[0], board.ourLoc[1] - 1]
	elif move == "south":
		dest = [board.ourLoc[0], board.ourLoc[1] + 1]
	elif move == "east":
		dest = [board.ourLoc[0] + 1, board.ourLoc[1]]
	elif move == "west":
		dest = [board.ourLoc[0] - 1, board.ourLoc[1]]
	# should never get here
	else:
		dest = [0,0]

	return dest

def getlastMove(board, snake):
	diffX = snake["coords"][0][0] - snake["coords"][1][0]
	diffY = snake["coords"][0][1] - snake["coords"][1][1]

	if diffX < 0:
		lastMove = "west"
	elif diffX > 0:
		lastMove = "east"
	elif diffY < 0:
		lastMove = "north"
	elif diffY > 0:
		lastMove = "south"
	else:
		lastMove = "error"
