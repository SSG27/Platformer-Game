from player import *
from button import *

def drawGrid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tileSize), (screenWidth, line * tileSize))
        pygame.draw.line(screen, (255, 255, 255), (line * tileSize, 0), (line * tileSize, screenHeight))


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
        if menuState == 'optionMain':
            screen.blit(menuBackgroundImage, (0, 0))
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
            drawText("select your desired frame rate below", font, (0, 0, 0), 300, 50)
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

        monsterGroup.draw(screen)
        fireGroup.draw(screen)
        spikeGroup.draw(screen)



        # if player has died
        if gameOver == -1:
            if restartButton.draw():
                player.reset(100, screenHeight - 130)
                gameOver = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # if gameOver == False:
                gamePaused = True
                menuState = 'main'

    pygame.display.update()

pygame.quit()
