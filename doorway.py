from loadimages import *


class Doorway(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = doorwayImage
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


doorwayGroup = pygame.sprite.Group()
