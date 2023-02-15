from loadimages import *

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = monsterImage
		# defines the rectangle of the monsters (hit-box)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.moveDirection = 2
		self.moveCounter = 0

	def update(self):
		# makes monster move by 2 pixels to the right
		self.rect.x += self.moveDirection
		self.moveCounter += 2
		if abs(self.moveCounter) > 55:
			# reverses direction monster moves in
			self.moveDirection *= -1
			self.moveCounter *= -1

# creates a new group of monsters
monsterGroup = pygame.sprite.Group()
