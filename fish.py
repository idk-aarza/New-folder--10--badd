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
icon=pygame.image.load("ufo.png")
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
bulletImg = pygame.image.load("bullet.png")
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
    distance = math.sqrt(math.pow(enemyX - bulletX) ** 2 + (enemyY - bulletY)**2)
    return distance<COLLISION_DISTANCE
#GAME LOOP
running = True