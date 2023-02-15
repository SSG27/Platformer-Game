from loadimages import *


class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = coinImage
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


coinGroup = pygame.sprite.Group()
