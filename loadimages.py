import pygame

# load backgrounds
backgroundImage1 = pygame.image.load('images/background/dungeon.png')
backgroundImage = pygame.transform.scale(backgroundImage1, (1000, 700))
menuBackgroundImage1 = pygame.image.load('images/background/menu.jpg')
menuBackgroundImage = pygame.transform.scale(menuBackgroundImage1, (1000, 700))
optionBackgroundImage = menuBackgroundImage

# load blocks
dirtImage1 = pygame.image.load('images/blocks/dirt.png')
dirtImage = pygame.transform.scale(dirtImage1, (50, 50))
grassImage1 = pygame.image.load('images/blocks/grass.png')
grassImage = pygame.transform.scale(grassImage1, (50, 50))
brickImage1 = pygame.image.load('images/blocks/brick.png')
brickImage = pygame.transform.scale(brickImage1, (50, 50))
blackBrickImage1 = pygame.image.load('images/blocks/dark brick.png')
blackBrickImage = pygame.transform.scale(blackBrickImage1, (50, 50))

# load enemies
monsterImage1 = pygame.image.load('images/enemies/monster.png')
monsterImage = pygame.transform.scale(monsterImage1, (35, 35))
fireImage1 = pygame.image.load('images/enemies/fire.png')
fireImage = pygame.transform.scale(fireImage1, (50, 50))
spikeImage1 = pygame.image.load('images/enemies/spikes.png')
spikeImage = pygame.transform.scale(spikeImage1, (50, 19))

# load character
deadImage1 = pygame.image.load('images/main character/ghost.png')
deadImage = pygame.transform.scale(deadImage1, (40, 35))

# load buttons
restartImage = pygame.image.load('images/buttons/restart_btn.png')
startImage = pygame.image.load('images/buttons/start_btn.png')
exitImage = pygame.image.load('images/buttons/exit_btn.png')
optionsImage1 = pygame.image.load('images/buttons/options_btn.png')
optionsImage = pygame.transform.scale(optionsImage1, (350, 130))
backImage1 = pygame.image.load('images/buttons/back_btn.png')
backImage = pygame.transform.scale(backImage1, (200, 100))
resumeImage1 = pygame.image.load('images/buttons/resume_btn.png')
resumeImage = pygame.transform.scale(resumeImage1, (350, 125))
iImage1 = pygame.image.load('images/buttons/i_btn.png')
iImage = pygame.transform.scale(iImage1, (75, 75))

# load fps buttons
tenImage = pygame.image.load('images/buttons/10.png')
thirtyImage = pygame.image.load('images/buttons/30.png')
sixtyImage = pygame.image.load('images/buttons/60.png')
oneTwentyImage = pygame.image.load('images/buttons/120.png')
twoFortyImage = pygame.image.load('images/buttons/240.png')
