from loadimages import *

class Spike(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = spikeImage
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


spikeGroup = pygame.sprite.Group()
