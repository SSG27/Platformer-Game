from loadimages import *

class Fire(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = fireImage
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


fireGroup = pygame.sprite.Group()
