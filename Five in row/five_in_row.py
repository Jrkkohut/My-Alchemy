class Tile:
	def __init__(self, pos):
		self.position = pos  # [0, 0]
		self.isEmpty = True  # is empty at the start
		self.player = None  # None player at the start

	def __str__(self):
		if self.isEmpty:
			return str(self.position)
		else:
			return "  " + str(self.player) + "   "

	def writeUpPlayer(self, player):
		if self.isEmpty:
			self.isEmpty = False
			self.player = player
			return True
		else:
			return False


class Board:
	def __init__(self):
		self.tiles = [Tile([x, y]) for x in range(3) for y in range(3)]

	def printBoard(self):
		for x in range(3):
			for y in range(3):
				print(self.tiles[x*3 + y], end="")
			print()

	def writeUpPlayer(self, player, pos):
		return self.tiles[pos].writeUpPlayer(player)

	def checkDraw(self):
		for tile in self.tiles:
			if tile.isEmpty:
				return False
		return True

	def getTile(self, pos):
		return self.tiles[pos]


class Player:
	def __init__(self, id, mark):
		self.id = id
		self.mark = mark
		self.tiles = []

	def __repr__(self):
		return self.mark

	def turn(self):
		pos = input(f"{self.mark}: Enter position to add your mark (x,y): ")
		x, y = pos.split(",")
		return int(x)*3 + int(y)

	def addTile(self, tile):
		self.tiles.append(tile.position)

	def checkWin(self):
		win_seq = [
			[[0, 0], [0, 1], [0, 2]],
			[[1, 0], [1, 1], [1, 2]],
			[[2, 0], [2, 1], [2, 2]],
			[[0, 0], [1, 1], [2, 2]],
			[[0, 2], [1, 1], [2, 0]]
		]
		if len(self.tiles) < 3:
			return False
		for seq in win_seq:
			if seq[0] in self.tiles and seq[1] in self.tiles and seq[2] in self.tiles:
				return True
		return False


class Game:
	def __init__(self):
		self.board = Board()
		self.players = [Player(1, "X"), Player(2, "O")]

	def play(self):
		cnt = 0
		while not self.board.checkDraw():
			self.board.printBoard()
			pl = self.players[cnt % 2]
			pos = pl.turn()
			if self.board.writeUpPlayer(pl, pos):
				cnt += 1
				pl.addTile(self.board.getTile(pos))
				if pl.checkWin():
					print(f"Player {pl} is winner after {cnt} rounds!!!")
					self.board.printBoard()
					return
			else:
				print("Tile is full!")
		else:
			print("It's a draw!")


game = Game()
game.play()