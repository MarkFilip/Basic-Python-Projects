import pygame
import random
import math
from pygame import mixer

# Initialize  pygame
pygame.init()

# create the screen. Takes a tuple containing width, height (X,Y) Top left is (0,0)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Background Sound
# mixer.music.load('background.wav')  # Sets the sound. Music instead of sound because it plays longer
# mixer.music.play(-1)  # Play the sound. -1 allows it to loop

# Title and ICon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Game State options are start, ready, level-up
game_state = "start"

# Player
playerImg = pygame.image.load('circlelogo-white.png')
playerX = 370
playerY = 480
playerX_change = 0

# Level
level_value = 1
font = pygame.font.Font('freesansbold.ttf', 32)
levelX = 10
levelY = 45

# Enemy
enemy_icons = ['chrome.png', 'css-3.png', 'javascript.png', 'sql-server.png', 'python.png', 'hashtag.png']
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemy_speed = 0.75 * level_value

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(enemy_icons[level_value-1]))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('checked.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"  # ready means you can't see the bullet on the screen, fire means it is moving

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 10
scoreY = 10


# Start text
start_font = pygame.font.Font('freesansbold.ttf', 48)

# Level up text
level_font = pygame.font.Font('freesansbold.ttf', 48)

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 48)

# You win text
win_font = pygame.font.Font('freesansbold.ttf', 48)


# display functions
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_level(x, y):
    level = font.render("Level " + str(level_value), True, (255, 255, 255))
    screen.blit(level, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (230, 230))


def start_game_text():
    start_text = start_font.render("Press ENTER", True, (0, 0, 0))
    screen.blit(start_text, (220, 230))


def level_up_text():
    level_text = level_font.render("LEVEL UP", True, (0, 0, 0))
    screen.blit(level_text, (260, 230))


def win_game_text():
    win_text = win_font.render("YOU WIN!", True, (0, 0, 0))
    screen.blit(win_text, (260, 230))


def player(x, y):
    screen.blit(playerImg, (x, y))  # blit means to draw (Icon, tuple with coordinates)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # The coordinates are changed to center the bullet


# collision detecting function
def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Distance formula. If distance less than 27 then it is a collision
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game loop.
running = True
while running:
    # Background color within rgb tuple
    screen.fill((0, 0, 102))
    # Background image
    screen.blit(background, (0, 0))

    # start game instructions
    if game_state == "start":
        start_game_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = 'ready'
    # Level up
    elif game_state == "level-up":
        level_up_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_value += 1
                    enemy_speed = 0.5 * level_value
                    for i in range(num_of_enemies):
                        enemyImg[i] = pygame.image.load(enemy_icons[level_value-1])
                    game_state = 'ready'
    elif game_state == 'win':
        win_game_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score_value = 0
                    level_value = 1
                    enemy_speed = 0.5 * level_value
                    for i in range(num_of_enemies):
                        enemyImg[i] = pygame.image.load(enemy_icons[0])
                    game_state = 'ready'
    else:
        # Events are any user inputs
        for event in pygame.event.get():
            # Checks to see if the user clicks the X in the window and if so, ends the loop
            if event.type == pygame.QUIT:
                running = False

            # if a keystroke is pressed, check whether it is left or right
            if event.type == pygame.KEYDOWN:  # Checks if a key is pushed
                if event.key == pygame.K_LEFT:
                    playerX_change = -5  # Moves the X coordinate left
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5  # Moves the X coordinate right
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":  # If there isn't already a bullet on the screen
                        # bullet_sound = mixer.Sound('laser.wav')  # Sets the sound of the bullet
                        # bullet_sound.play()  # Plays it once
                        bulletX = playerX  # Get's the X coordinate of the ship to give to the bullet
                        fire_bullet(bulletX, bulletY)  # Fire the bullet
            if event.type == pygame.KEYUP:  # Checks if a keystroke has been released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0  # Doesn't move the X coordinate left

        # player movement
        playerX += playerX_change

        # checks boundaries of the player
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy movement
        for i in range(num_of_enemies):

            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]

            # checks boundaries of the enemy
            if enemyX[i] <= 0:
                enemyX_change[i] = 2 + enemy_speed
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -2 - enemy_speed
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                # explosion_sound = mixer.Sound('explosion.wav')  # Sets the sound of the explosion
                # explosion_sound.play()  # Plays it once
                # Resets the bullet
                bulletY = 480
                bullet_state = "ready"
                # Update score
                score_value += 1
                if score_value > 17:
                    game_state = "win"
                elif score_value % 3 == 0:
                    game_state = "level-up"
                # Reset enemy
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            # Draw enemy
            enemy(enemyX[i], enemyY[i], i)

        # Bullet movement
        # When it reaches the end, make the bullet ready for another fire
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        # Plot the bullet when it is fired. Keep changing the Y value
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

    # Draw the player
    player(playerX, playerY)
    # Draw the score and level
    show_score(scoreX, scoreY)
    show_level(levelX, levelY)
    pygame.display.update()  # Needs to be added so the screen updates
