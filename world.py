from settings import *
from map import *
from enemy import *
from fire import *
from spike import *
from coin import *
from doorway import *


# this is the world class
class World:
    def __init__(self, data):
        self.tileList = []
        # this adds the data to every row in the game
        rowCounter = 0
        for row in data:
            # this adds the data to every column in the game
            collumnCounter = 0
            for tile in row:
                # if the tile is 1, then a dirt block is placed there.
                if tile == 1:
                    img = dirtImage
                    imgRectangle = img.get_rect()
                    imgRectangle.x = collumnCounter * tileSize
                    imgRectangle.y = rowCounter * tileSize
                    tile = (img, imgRectangle)
                    self.tileList.append(tile)
                # if the tile is 2, then a grass block is placed there.
                if tile == 2:
                    img = grassImage
                    imgRectangle = img.get_rect()
                    imgRectangle.x = collumnCounter * tileSize
                    imgRectangle.y = rowCounter * tileSize
                    tile = (img, imgRectangle)
                    self.tileList.append(tile)
                # if the tile is 3, then a brick block is placed there.
                if tile == 3:
                    img = brickImage
                    imgRectangle = img.get_rect()
                    imgRectangle.x = collumnCounter * tileSize
                    imgRectangle.y = rowCounter * tileSize
                    tile = (img, imgRectangle)
                    self.tileList.append(tile)
                # if the tile is 4, then a back brick block is placed there.
                if tile == 4:
                    img = blackBrickImage
                    imgRectangle = img.get_rect()
                    imgRectangle.x = collumnCounter * tileSize
                    imgRectangle.y = rowCounter * tileSize
                    tile = (img, imgRectangle)
                    self.tileList.append(tile)
                if tile == 5:
                    monster = Enemy(collumnCounter * tileSize, rowCounter * tileSize + 15)
                    monsterGroup.add(monster)
                if tile == 6:
                    fire = Fire(collumnCounter * tileSize, rowCounter * tileSize)
                    fireGroup.add(fire)
                if tile == 7:
                    spike = Spike(collumnCounter * tileSize, rowCounter * tileSize + 31)
                    spikeGroup.add(spike)
                if tile == 8:
                    doorway = Doorway(collumnCounter * tileSize, rowCounter * tileSize - 25)
                    doorwayGroup.add(doorway)
                if tile == 9:
                    coin = Coin(collumnCounter * tileSize + 13, rowCounter * tileSize + 10)
                    coinGroup.add(coin)
                collumnCounter += 1
            rowCounter += 1

    def draw(self):
        for tile in self.tileList:
            screen.blit(tile[0], tile[1])
            # this draws a white outline around every tile in my game
            # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


worldData = eval('level' + str(currentLevel))
# this creates an instance of the World class with worldData as an argument
world = World(worldData)
