class BoardFrame:

	def __init__(self, data, height, width):
		self.turn = data["turn"]
		self.height = height
		self.width = width
		self.snakes = data["snakes"]
		self.foods = data["food"]

		self.ourSnake = self.findOurSnake(self.snakes)
		self.ourLoc = self.ourSnake["coords"][0]
		self.grid = self.makeGrid()

	def findOurSnake(self, snakes):
		for snake in snakes:
			if snake["name"] == "crazySnake":
				return snake
	
	def makeGrid(self):
		grid = [ [ {"state": "empty", "snake": "empty", "cornerRank":0, "foodRank":0} for y in range(self.height)]  for x in range(self.width) ]

		for snake in self.snakes:
			snakeCoords = snake["coords"]

			grid[ snakeCoords[0][0] ][ snakeCoords[0][1] ]["state"] = "head"
			grid[ snakeCoords[0][0] ][ snakeCoords[0][1] ]["snake"] = snake["name"]

			for coordNumber in range (1, len(snakeCoords)):
				grid[ snakeCoords[coordNumber][0]][snakeCoords[coordNumber][1]]["state"] = "body"
				grid[ snakeCoords[coordNumber][0]][snakeCoords[coordNumber][1]]["snake"] = snake["name"]




