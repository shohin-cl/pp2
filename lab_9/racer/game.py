import pygame, random, sys, os, time
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5
count = 3

# my code
COINSIZE = 10
COINSPEED = 8
ADDNEWCOINS = 7
# coin_count = 0
most_coin = 0

# sample_coin = []

# ends here

def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # escape quits
                    terminate()
                return


def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False


# my code

def playerHasHitCoin(playerRect, coins):
    for coin in coins:
        if playerRect.colliderect(coin['rect']):
            # coins.remove(coin)
            return True
    return False
# ends here

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('car race')
pygame.mouse.set_visible(False)

# fonts
font = pygame.font.Font(None, 30)

# sounds
gameOverSound = pygame.mixer.Sound('music/crash.wav')
pygame.mixer.music.load('music/car.wav')
laugh = pygame.mixer.Sound('music/laugh.wav')

# images
playerImage = pygame.image.load('image/car1.png')
car3 = pygame.image.load('image/car3.png')
car4 = pygame.image.load('image/car4.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('image/car2.png')
sample = [car3, car4, baddieImage]
wallLeft = pygame.image.load('image/left.png')
wallRight = pygame.image.load('image/right.png')

# My code
coinImage = pygame.image.load('image/653278_coin_bitcoin_cash_currency_dollar_icon.png')
coinImage2 = pygame.image.load('image/5310117_coin_dollar_money_icon.png')
coinImage3 = pygame.image.load('image/3319620_coin_dollar_money_shine_icon.png')

sample_coin_list = [coinImage2, coinImage, coinImage3]
# ends here


# "Start" screen
drawText('Press any key to start the game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
drawText('And Enjoy', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) + 30)
pygame.display.update()
waitForPlayerToPressKey()
zero = 0

# My Code
if not os.path.exists('data/coins_count.dat'):
    f = open('data/coins_count.dat', 'w')
    f.write((str(zero)))
    f.close()

    v = open('data/coins_count.dat')
    most_coin = int(v.readline())
    v.close()
# ends here

if not os.path.exists("data/save.dat"):
    f = open("data/save.dat", 'w')
    f.write(str(zero))
    f.close()
v = open("data/save.dat", 'r')
topScore = int(v.readline())
v.close()
while (count > 0):
    # start of the game
    baddies = []
    # My code
    coins = []
    coinAddCounter = 0
    coin_count = 0
    # ends here
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:  # the game loop
        score += 1  # increase score

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0

                if event.key == ord('x'):
                    slowCheat = False
                    score = 0

                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

        # Add new baddies at the top of the screen
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        # My code
            coinAddCounter += 1

        if coinAddCounter == ADDNEWCOINS + 10:
            coinAddCounter = 0
            coinSize = 10
            choice = random.choice(sample_coin_list)
            newCoin = {'rect': pygame.Rect(random.randint(140, 485), 0 - coinSize, 30, 30),
                       'speed': COINSPEED,
                       'surface': pygame.transform.scale(choice, (30, 30)),
                       'choice': choice
                       }

            coins.append(newCoin)

        # ends here


        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = 30
            newBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                         'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface': pygame.transform.scale(random.choice(sample), (23, 47)),
                         }
            baddies.append(newBaddie)
            sideLeft = {'rect': pygame.Rect(0, 0, 126, 600),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface': pygame.transform.scale(wallLeft, (126, 599)),
                        }
            baddies.append(sideLeft)
            sideRight = {'rect': pygame.Rect(497, 0, 303, 600),
                         'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface': pygame.transform.scale(wallRight, (303, 599)),
                         }
            baddies.append(sideRight)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # My coin

        for coin in coins:
            if not reverseCheat and not slowCheat:
                coin['rect'].move_ip(0, coin['speed'])
            elif reverseCheat:
                coin['rect'].move_ip(0, -5)
            elif slowCheat:
                coin['rect'].move_ip(0, 1)

        for coin in coins[:]:
            if coin['rect'].top > WINDOWHEIGHT:
                coins.remove(coin)

        # ends here

        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 128, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 20)
        drawText('Rest Life: %s' % (count), font, windowSurface, 128, 40)

        # My code
        drawText('Coins: %s' %(coin_count), font, windowSurface, 350, 20)
        drawText('Most Coins %s' % (most_coin), font, windowSurface, 350, 40)
        # ends here

        windowSurface.blit(playerImage, playerRect)

        # My code
        for coin in coins:
            windowSurface.blit(coin['surface'], coin['rect'])

        # ends here

        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()
        # my code
        if playerHasHitCoin(playerRect, coins):
            for coin in coins:
                if playerRect.colliderect(coin['rect']):
                    coin_count += sample_coin_list.index(coin['choice']) + 1
                    coins.remove(coin)

        # ends here


        # Check if any of the car have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            # My code
            if coin_count > most_coin:
                fi = open('data/coins_count.dat', 'w')
                fi.write(str(coin_count))
                fi.close()
                most_coin = coin_count
            # ends here
            if score > topScore:
                g = open("data/save.dat", 'w')
                g.write(str(score))
                g.close()
                topScore = score
            break

        # My code
        N = 1
        if coin_count >= N * 5:
            N += 1
            for coin in coins:
                coin['speed'] += 0.1

            for b in baddies:
                b['speed'] += 0.1
        # Ends here

        mainClock.tick(FPS)

    # "Game Over" screen.
    pygame.mixer.music.stop()
    count = count - 1
    gameOverSound.play()
    time.sleep(1)
    if (count == 0):
        laugh.play()
        drawText('Game over', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
        pygame.display.update()
        time.sleep(2)
        waitForPlayerToPressKey()
        count = 3
        gameOverSound.stop()