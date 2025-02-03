import pygame
import random


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
enemyImg = pygame.image.load('Enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

#bullet configuration
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 1
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

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
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0

    #changing for boundries so it does not go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    #bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()