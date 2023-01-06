import pygame
import sys

# this initialises pygame so that it is ready to run
pygame.init()

# this sets the frame rate of my game to 30 so that the game can refresh at a smooth rate.
clock = pygame.time.Clock()
fps = 30

screenWidth = 1000
screenHeight = 700

# this sets the  size of the console to 1000 by 700 pixels
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('SanjusPlatformerGame')

# this sets the variable 'tileSize' to equal 50, which is the width and height of
# each block in my game in pixels
tileSize = 50
# this is the variable that controls whether the player is dead or alive
gameOver = 0
# this is the variable that controls whether the player is in the menu screen
gamePaused = True
menuState = 'start'

# define text font and colour
font = pygame.font.SysFont("arialblack", 20)
white = (255, 255, 255)


# function to draw text on screen
def drawText(text, font, white, x, y):
  image = font.render(text, True, white)
  screen.blit(image, (x, y))
