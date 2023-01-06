from world import *


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

            # check for collision with fire
            if pygame.sprite.spritecollide(self, fireGroup, False):
                gameOver = -1

            # check for collision with spikes
            if pygame.sprite.spritecollide(self, spikeGroup, False):
                gameOver = -1

            # this adds the values of 'dx and 'dy' to the player's coordinates
            self.rect.x += dx
            self.rect.y += dy

        elif gameOver == -1:
            self.image = self.deadImage
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

