from loadimages import *
from settings import *

class Button():
	def __init__(self, x, y, image):
		self.image = image
		# defines the rectangle of the button
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		# gets  the cursor's position
		mousePosition = pygame.mouse.get_pos()

		# check mouseover and clicked conditions
		if self.rect.collidepoint(mousePosition):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True
				
		# checks if the left mouse button is not being pressed
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		# draws buttons onto the screen
		screen.blit(self.image, self.rect)

		return action


# create buttons along with button coordinates on screen
restartButton = Button(screenWidth // 2 - 60, screenHeight // 2 - 21, restartImage)
startButton = Button(screenWidth // 2 - 130, screenHeight // 2 - 270, startImage)
optionButton = Button(screenWidth // 2 - 170, screenHeight // 2 - 55, optionsImage)
exitButton = Button(screenWidth // 2 - 110, screenHeight // 2 + 150, exitImage)
backButton = Button(screenWidth // 2 - 100, screenHeight // 2 + 70, backImage)
resumeButton = Button(screenWidth // 2 - 170, screenHeight // 2 - 270, resumeImage)
iButton = Button(30, 595, iImage)
tenButton = Button(100, 200, tenImage)
thirtyButton = Button(270, 200, thirtyImage)
sixtyButton = Button(440, 200, sixtyImage)
oneTwentyButton = Button(610, 200, oneTwentyImage)
twoFortyButton = Button(780, 200, twoFortyImage)
