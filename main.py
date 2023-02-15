from button import *
from world import *
from coin import *
from pygame import mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()


class Player:
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, gameOver):
        dx = 0
        dy = 0
        walkCooldown = 5

        if gameOver == 0:
            # get key-presses
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and self.jumped is False and self.inAir is False:
                jump_sfx.play()
                self.verticalVelocity = -12
                self.jumped = True
            if key[pygame.K_UP] is False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] is False and key[pygame.K_RIGHT] is False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.imagesRight[self.index]
                if self.direction == -1:
                    self.image = self.imagesLeft[self.index]

            # handle animation
            if self.counter > walkCooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.imagesRight):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.imagesRight[self.index]
                if self.direction == -1:
                    self.image = self.imagesLeft[self.index]

            # this adds velocity to my game so that the player can move with realistic speed when jumping
            self.verticalVelocity += 1
            if self.verticalVelocity > 10:
                self.verticalVelocity = 10
            # this adds the value of velocity to the variable 'dy'
            dy += self.verticalVelocity

            # check for collision
            self.inAir = True
            for tile in world.tileList:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.verticalVelocity < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.verticalVelocity = 0
                    # check if above the ground i.e. falling
                    elif self.verticalVelocity >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.verticalVelocity = 0
                        self.inAir = False

            # check for collision with monsters
            if pygame.sprite.spritecollide(self, monsterGroup, False):
                gameOver = -1
                gameOver_sfx.play()

            # check for collision with fire
            if pygame.sprite.spritecollide(self, fireGroup, False):
                gameOver = -1
                gameOver_sfx.play()

            # check for collision with spikes
            if pygame.sprite.spritecollide(self, spikeGroup, False):
                gameOver = -1
                gameOver_sfx.play()

            # check for collision with doorway
            if pygame.sprite.spritecollide(self, doorwayGroup, False):
                gameOver = 1

            # this adds the values of 'dx and 'dy' to the player's coordinates
            self.rect.x += dx
            self.rect.y += dy

        elif gameOver == -1:
            self.image = self.deadImage
            drawText('GAME OVER!', gameOverFont, blue, 270, 250)
            if self.rect.y > 200:
                self.rect.y -= 5

        return gameOver

    def reset(self, x, y):
        self.imagesRight = []
        self.imagesLeft = []
        for num in range(1, 8):
            imgRight = pygame.image.load(f'images/main character/guy{num}.png')
            imgRight = pygame.transform.scale(imgRight, (40, 35))
            imgLeft = pygame.transform.flip(imgRight, True, False)
            self.imagesRight.append(imgRight)
            self.imagesLeft.append(imgLeft)
        self.index = 0
        self.counter = 0
        self.image = self.imagesRight[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.verticalVelocity = 0
        self.jumped = False
        self.direction = 0
        self.inAir = True
        self.deadImage = deadImage

    def walls(self):
        # this prevents the player from falling through the screen
        if self.rect.bottom > screenHeight:
            self.rect.bottom = screenHeight
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.x > 960:
            self.rect.x = 960
        if self.rect.x < 0:
            self.rect.x = 0

    def draw(self):
        # this draws the player onto the screen
        screen.blit(self.image, self.rect)
        # this draws a white outline around the hit-box of the player
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


def drawGrid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tileSize), (screenWidth, line * tileSize))
        pygame.draw.line(screen, (255, 255, 255), (line * tileSize, 0), (line * tileSize, screenHeight))


# function to reset level
def resetLevel(currentLevel):
    player.reset(100, screenHeight - 130)
    monsterGroup.empty()
    fireGroup.empty()
    spikeGroup.empty()
    doorwayGroup.empty()
    coinGroup.empty()

    worldData = eval('level' + str(currentLevel))
    world = World(worldData)

    return world


# this creates an instance of the player's sprite at the coordinates (100, 600)
player = Player(100, screenHeight - 100)

run = True
while run:

    clock.tick(fps)

    if gamePaused == True:
        if menuState == 'start':
            screen.blit(menuBackgroundImage, (0, 0))
            if exitButton.draw():
                run = False
            if startButton.draw():
                gamePaused = False
            if optionButton.draw():
                menuState = 'optionStart'
            if iButton.draw():
                menuState = 'informationStart'
        if menuState == 'optionStart':
            screen.blit(menuBackgroundImage, (0, 0))
            # draws the settings buttons on the screen
            if backButton.draw():
                menuState = 'start'
            if tenButton.draw():
                fps = 10
            if thirtyButton.draw():
                fps = 30
            if sixtyButton.draw():
                fps = 60
            if oneTwentyButton.draw():
                fps = 120
            if twoFortyButton.draw():
                fps = 240
            drawText("select your desired frame rate below", font, (0, 0, 0), 300, 90)
            drawText(f"FPS: {fps} ", font, white, 900, 5)
        if menuState == 'optionMain':
            screen.blit(menuBackgroundImage, (0, 0))
            # draws the settings buttons on the screen
            if backButton.draw():
                menuState = 'main'
            if tenButton.draw():
                fps = 10
            if thirtyButton.draw():
                fps = 30
            if sixtyButton.draw():
                fps = 60
            if oneTwentyButton.draw():
                fps = 120
            if twoFortyButton.draw():
                fps = 240
            drawText("select your desired frame rate below", font, (0, 0, 0), 300, 90)
            drawText(f"FPS: {fps} ", font, white, 900, 5)
        if menuState == 'main':
            screen.blit(menuBackgroundImage, (0, 0))
            if resumeButton.draw():
                gamePaused = False
            if optionButton.draw():
                menuState = 'optionMain'
            if exitButton.draw():
                run = False
            if iButton.draw():
                menuState = 'informationMain'
        if menuState == 'informationStart':
            screen.blit(menuBackgroundImage, (0, 0))
            drawText("use the arrow keys to move and jump", font, white, 300, 50)
            drawText("try and reach the doorway to reach the next level", font, white, 230, 150)
            drawText("press space to pause the game", font, white, 320, 250)
            drawText("avoid the monsters, fire and spikes", font, white, 310, 350)
            if backButton.draw():
                menuState = 'start'
        if menuState == 'informationMain':
            screen.blit(menuBackgroundImage, (0, 0))
            drawText("use the arrow keys to move and jump", font, white, 300, 50)
            drawText("try and reach the doorway to reach the next level", font, white, 230, 150)
            drawText("press space to pause the game", font, white, 320, 250)
            drawText("avoid the monsters, fire and spikes", font, white, 310, 350)
            if backButton.draw():
                menuState = 'main'

    else:
        screen.blit(backgroundImage, (0, 0))

        world.draw()

        gameOver = player.update(gameOver)
        player.draw()
        player.walls()

        # drawGrid()

        if gameOver == 0:
            monsterGroup.update()
            loopCounter = 0
            # update score
            # checks if player has collected a coin
            if pygame.sprite.spritecollide(player, coinGroup, True):
                score += 1
                coinPickUp_sfx.play()

        monsterGroup.draw(screen)
        fireGroup.draw(screen)
        spikeGroup.draw(screen)
        doorwayGroup.draw(screen)
        coinGroup.draw(screen)

        # draws the death counter at (10, 5)
        drawText(f"Deaths: {deathCounter} ", font, white, 10, 5)
        # draws the current level on the screen at (435, 5)
        drawText(f"Level: {currentLevel} ", font, white, 435, 5)
        # draws the score on the game window at (900, 5)
        drawText(f"Score: {score} ", font, white, 900, 5)

        # if player has died
        if gameOver == -1:
            if restartButton.draw():
                player.reset(100, 600)
                gameOver = 0
            if loopCounter == 0:
                deathCounter += 1
                loopCounter += 1

        # if player has completed level
        if gameOver == 1:
            currentLevel += 1
            if currentLevel <= 5:
                worldData = []
                world = resetLevel(currentLevel)
                gameOver = 0

            else:
                drawText("YOU WIN!", gameOverFont, blue, 330, 200)
                if restartButton.draw():
                    currentLevel = 1
                    # reset level
                    worldData = []
                    world = resetLevel(currentLevel)
                    score = 0
                    deathCounter = 0
                    gameOver = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gamePaused = True
                menuState = 'main'

    pygame.display.update()

pygame.quit()
