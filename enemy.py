from loadimages import *

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = monsterImage
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.moveDirection = 2
		self.moveCounter = 0

	def update(self):
		self.rect.x += self.moveDirection
		self.moveCounter += 2
		if abs(self.moveCounter) > 55:
			self.moveDirection *= -1
			self.moveCounter *= -1


monsterGroup = pygame.sprite.Group()
