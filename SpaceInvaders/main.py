import pygame
import random
import math
from pygame import mixer
import sys

# ---------------------- Game setup ----------------------

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

# Level
level_value = 1
font = pygame.font.Font('freesansbold.ttf', 32)
levelX = 10
levelY = 45

# enemy set up
enemy_icons = ['chrome.png', 'css-3.png', 'javascript.png', 'sql-server.png', 'python.png', 'hashtag.png']
num_of_enemies = 6
enemy_speed = 0.5 * level_value
enemies_per_level = 3
winning_score = enemies_per_level * num_of_enemies
# ---------------------- Classes ----------------------


# Player
class Player:
    Img = pygame.image.load('circlelogo-white.png')
    X = 370
    Y = 480
    X_change = 0

    def show_player(self, x, y):
        screen.blit(self.Img, (x, y))  # blit means to draw (Icon, tuple with coordinates)


# Enemy
class Enemy:
    def __init__(self):
        self.Img = pygame.image.load(enemy_icons[level_value - 1])
        self.X = random.randint(0, 736)
        self.Y = random.randint(50, 150)
        self.X_change = 2
        self.Y_change = 40

    def show_enemy(self, x, y):
        screen.blit(self.Img, (x, y))


# Bullet
class Bullet:
    Img = pygame.image.load('checked.png')
    X = 0
    Y = 480
    X_change = 0
    Y_change = 10
    state = "ready"  # ready means you can't see the bullet on the screen, fire means it is moving

    def fire(self, x, y):
        self.state = "fire"
        screen.blit(self.Img, (x + 16, y + 10))  # The coordinates are changed to center the bullet

    def reload(self):
        self.state = "ready"
        self.Y = 480


# ---------------------- Text Creation and Display----------------------
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


def start_game_text():
    start_text = start_font.render("Press ENTER", True, (0, 0, 0))
    screen.blit(start_text, (220, 230))


def level_up_text():
    level_text = level_font.render("LEVEL UP", True, (0, 0, 0))
    screen.blit(level_text, (260, 230))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (230, 230))


def win_game_text():
    win_text = win_font.render("YOU WIN!", True, (0, 0, 0))
    screen.blit(win_text, (260, 230))


# ---------------------- Game mechanic functions ----------------------
# collision detecting function
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    # Distance formula. If distance less than 27 then it is a collision
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 27:
        return True
    else:
        return False


# function that creates an array of enemies
def enemy_creation(number_of_enemies):
    list_of_enemies = []
    for i in range(num_of_enemies):
        list_of_enemies.append(Enemy())
    return list_of_enemies


# function that brings up the start menu
def start(state):
    starting = True
    while starting:
        start_game_text()  # display start text
        for event in pygame.event.get():
            # Allow the user to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Have the user press enter to begin the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = 'ready'
                    return state
        # Draw the player, score and level while waiting
        player.show_player(player.X, player.Y)
        show_score(scoreX, scoreY)
        show_level(levelX, levelY)
        pygame.display.update()


# function that brings up the level-up menu
def level_up(level):
    leveling = True
    while leveling:
        level_up_text()  # display level-up text
        for event in pygame.event.get():
            # Allow the user to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Have the user press enter to start the next level
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # update level and enemy speed
                    level += 1
                    speed = 0.5 * level
                    state = 'ready'
                    return state, level, speed
        # Draw the player, score and level while waiting
        player.show_player(player.X, player.Y)
        show_score(scoreX, scoreY)
        show_level(levelX, levelY)
        pygame.display.update()


# function that ends the game and allows for a reset
def win():
    winning = True
    while winning:
        win_game_text() # display level-up text
        # Allow the user to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Have the user press enter to play again
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = 'ready'
                    # reset level, score, and enemy speed
                    level = 1
                    score = 0
                    speed = 0.5 * level_value
                    return state, level, score, speed
        # Draw the player, score and level while waiting
        player.show_player(player.X, player.Y)
        show_score(scoreX, scoreY)
        show_level(levelX, levelY)
        pygame.display.update()


# ---------------------- Initialization ----------------------
player = Player()
bullet = Bullet()
enemies = enemy_creation(num_of_enemies)


# ---------------------- Game loop ----------------------
running = True
while running:
    # Background color within rgb tuple
    screen.fill((0, 0, 102))
    # Background image
    screen.blit(background, (0, 0))

    # start game instructions
    if game_state == "start":
        game_state = start(game_state)

    # Level up
    elif game_state == "level-up":
        game_state, level_value, enemy_speed = level_up(level_value)
        enemies = enemy_creation(num_of_enemies)

    # Winning the game and resetting
    elif game_state == 'win':
        game_state, level_value, score_value, enemy_speed = win()
        enemies = enemy_creation(num_of_enemies)

    # During gameplay
    else:
        # Events are any user inputs
        for event in pygame.event.get():
            # Checks to see if the user clicks the X in the window and if so, ends the loop
            if event.type == pygame.QUIT:
                running = False

            # if a keystroke is pressed, check whether it is left or right
            if event.type == pygame.KEYDOWN:  # Checks if a key is pushed
                if event.key == pygame.K_LEFT:
                    player.X_change = -5  # Moves the X coordinate left
                if event.key == pygame.K_RIGHT:
                    player.X_change = 5  # Moves the X coordinate right
                if event.key == pygame.K_SPACE:
                    if bullet.state == "ready":  # If there isn't already a bullet on the screen
                        # bullet_sound = mixer.Sound('laser.wav')  # Sets the sound of the bullet
                        # bullet_sound.play()  # Plays it once
                        bullet.X = player.X  # Get's the X coordinate of the ship to give to the bullet
                        bullet.fire(bullet.X, bullet.Y)  # Fire the bullet
            if event.type == pygame.KEYUP:  # Checks if a keystroke has been released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.X_change = 0  # Doesn't move the X coordinate left

        # player movement
        player.X += player.X_change

        # checks boundaries of the player
        if player.X <= 0:
            player.X = 0
        elif player.X >= 736:
            player.X = 736

        # Enemy movement
        for i in range(num_of_enemies):

            if enemies[i].Y > 440:
                for j in range(num_of_enemies):
                    enemies[j].Y = 2000
                game_over_text()
                break
            # Update change in X. Add enemy speed so respawned enemies move at correct speed
            enemies[i].X += enemies[i].X_change + enemy_speed

            # checks boundaries of the enemy
            if enemies[i].X <= 0:
                enemies[i].X_change = 2
                enemies[i].Y += enemies[i].Y_change
            elif enemies[i].X >= 736:
                enemies[i].X_change = - (2 + 2 * enemy_speed)
                # enemy speed has to be subtracted twice to compensate for addition earlier
                enemies[i].Y += enemies[i].Y_change

            # Collision
            collision = is_collision(enemies[i].X, enemies[i].Y, bullet.X, bullet.Y)
            if collision:
                # explosion_sound = mixer.Sound('explosion.wav')  # Sets the sound of the explosion
                # explosion_sound.play()  # Plays it once
                # Resets the bullet
                bullet.reload()
                # Update score
                score_value += 1
                if score_value == winning_score:
                    game_state = "win"
                elif score_value % enemies_per_level == 0:
                    game_state = "level-up"
                # Reset enemy
                enemies[i].X = random.randint(0, 736)
                enemies[i].Y = random.randint(50, 150)

            # Draw enemy
            enemies[i].show_enemy(enemies[i].X, enemies[i].Y)

        # Bullet movement
        # When it reaches the end, make the bullet ready for another fire
        if bullet.Y <= 0:
            bullet.reload()

        # Plot the bullet when it is fired. Keep changing the Y value
        if bullet.state == "fire":
            bullet.fire(bullet.X, bullet.Y)
            bullet.Y -= bullet.Y_change

    # Draw the player
    player.show_player(player.X, player.Y)
    # Draw the score and level
    show_score(scoreX, scoreY)
    show_level(levelX, levelY)
    pygame.display.update()  # Needs to be added so the screen updates
