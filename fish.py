import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X=370
PLAYER_STARTER_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27
#INITIALIZE PYGAME
pygame.init()
#CREATE SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#BACKGROUND
background =pygame.image.load("spacceee.jpg")
#Caption and icon
pygame.display.set_caption("Space.invaders")
icon=pygame.image.load("ufo.jpg")
pygame.display.set_icon(icon)
#PLAYER
playerImg = pygame.image.load("player.png")
playerX = PLAYER_START_X
playerY = PLAYER_STARTER_Y
playerX_change = 0
#ENEMY
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))#64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
#BULLET
bulletImg = pygame.image.load("bullett.png")
bulletX = 0
bulletY = PLAYER_STARTER_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"
#SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
#GAME OVER TEXT
over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    #DISPLAY THE CURRENT SCORE ON THE SCREEN
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    #DISPLAY GAME OVER TEXT 
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    #DRAW PLAYER ON THE SCREEN
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    #DRAW ENEMY ON THE SCREEN
    screen.blit(enemyImg[i], (x, y))
def fire_bullet(x, y):
    #FIRE A BULLET FROM THE PLAYER' POSITION
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    #CHECK IF A COLLISION OCCURED
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY)**2)
    return distance<COLLISION_DISTANCE
#GAME LOOP
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0
    #Player movement
    playerX += playerX_change
    playerX = max(0,min(playerX, SCREEN_WIDTH - 64)) #64 is the size of the player
    #ENEMY MOVEMENT
    for i in range(num_of_enemies):
        if enemyY[i] > 340: #GAME OVER CONDITION
            for j in range (num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
        #COLLISION CHECK
        if  isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_STARTER_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemyX[i], enemyY[i], i)
    #BULLET MOVEMENT
    if bulletY <=0:
        bulletY = PLAYER_STARTER_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
    