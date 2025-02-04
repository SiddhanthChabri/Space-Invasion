import pygame
import random
import math


pygame.init() #This initializes the pygame

screen = pygame.display.set_mode((800, 600)) #creates a screen of 800px width and 600px height

#Background
background = pygame.image.load('background.jpg')

#Title and icon section
pygame.display.set_caption("Space Invation")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


#player configuration
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


#enemy configuration
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

#bullet configuration
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 1
bullet_state = "ready"

#Score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


#Game over text
overFont = pygame.font.Font('freesansbold.ttf', 62)

def showScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))

def gameOver():
    overText = font.render("Game Over: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(overText, (200, 250))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX- bulletX),2) + math.pow((enemyY - bulletY), 2))
    if distance < 27:
        return True
    else:
        return False
#running window
running = True
while running:

    screen.fill((1, 11, 25))
    screen.blit(background,(0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        # if keystorke is pressed check whether if its right or left
        if event.type == pygame.KEYDOWN:
            print("A key is pressed")
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change -= 0.3
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change += 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0

    #changing for boundries so it does not go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #enemy movement
    for i in range(num_of_enemies):

        #Gave over
        if enemyY[i] > 450:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            gameOver()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

    #collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            scoreValue += 1
            
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    

    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()