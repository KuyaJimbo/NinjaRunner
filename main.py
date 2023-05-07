import pygame
from sys import exit
from random import randint, choice
from math import ceil

from NinjaClass import Ninja  # import Ninja class
from EnemyClass import Obstacle  # import Obstacles


# ------- Functions --------------
def display_score():  # Displays the score on the screen
    current_time = int(pygame.time.get_ticks() / 1000) - start_time  # calculate current time
    score_surf = test_font.render(f'Score: {current_time}', False, (255, 255, 255))  # renders text onto screen
    score_rect = score_surf.get_rect(center=(400, 50))  # ensures the center of image will exist at (400, 50)
    screen.blit(score_surf, score_rect)  # adds text to screen
    return current_time  # This value = score


def collision_sprite():  # checks if collision occurs
    if pygame.sprite.spritecollide(ninja.sprite, obstacle_group, False):
        obstacle_group.empty()  # empty obstacle group after collision occurs
        return False
    else:
        return True


# ------ Game Set Up Code --------
pygame.init()  # starts pygame
screen = pygame.display.set_mode((1000, 600))  # creates the screen and size
pygame.display.set_caption('Runner')  # Title's the screen
clock = pygame.time.Clock()  # creates a clock object to track time for the game
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)  # game font
game_active = False  # is the game started initially? no
start_time = 0  # reset start time
score = 0  # reset score
bg_music = pygame.mixer.Sound('audio/music.wav')  # background music
bg_music.set_volume(0.1)  # adjust music volume
bg_music.play(loops=-1)  # loop the music

# Groups
ninja = pygame.sprite.GroupSingle()  # creates GROUP SINGLE object sprite class
ninja.add(Ninja())  # adds the Ninja object to the ninja group

obstacle_group = pygame.sprite.Group()  # creates NORMAL GROUP object sprite class

# Load Background Graphics
forest = pygame.image.load('graphics/Forest.png').convert()  # size: (600, 600)
forest_width = forest.get_width()
scroll = 0
tiles = ceil(1000 / 600) + 1  # how many tiles fit on the screen

# Intro screen
Logo = pygame.image.load('MiyaSheesh.png').convert_alpha()  # Loads ninja cover image
Logo = pygame.transform.scale(Logo, (64, 64))  # Scales the image
Logo_rect = Logo.get_rect(center=(400, 200))  # ensures the center of image will exist at (400, 200)

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))  # renders the text onto the screen
game_name_rect = game_name.get_rect(center=(400, 80))  # ensures the center of the text will exist at (400, 80)

game_message = test_font.render('Press space to run', False, (111, 196, 169))  # renders the text onto the screen
game_message_rect = game_message.get_rect(center=(400, 330))  # ensures the center of text will exist at (400, 330)

# Obstacle Timer
obstacle_timer = pygame.USEREVENT + 1  # creates a custom pygame event
pygame.time.set_timer(obstacle_timer, 1500)  # obstacle_timer event occurs every 1.5 seconds

while True:  # run the game loop forever
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # game runs until 'QUIT'
            pygame.quit()  # closes pygame
            exit()  # closes the file here, does not run the rest of the code

        if game_active:  # game is playing
            if event.type == obstacle_timer:  # if obstacle timer occurs
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))  # randomly adds an obstacle

        else:  # menu screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # if key SPACE is down
                game_active = True  # game starts playing
                start_time = int(pygame.time.get_ticks() / 1000)  # start time increments by 1 every second

    if game_active:  # when game plays
        # Creates Scrolling background
        for i in range(0, tiles):
            screen.blit(forest, (i * 600 + scroll, 0))
        scroll -= 5
        if abs(scroll) > 600:
            scroll = 0

        score = display_score()  # Display's the score on the screen

        ninja.draw(screen)  # draw the ninja GROUP SINGLE object
        ninja.update()  # call update function on ninja object

        obstacle_group.draw(screen)  # draw the obstacle GROUP object
        obstacle_group.update()  # call update function on obstacle group object

        game_active = collision_sprite()  # end the game if collision between ninja and obstacles occur

    else:  # Menu screen
        screen.fill((94, 129, 162))  # create background fill
        screen.blit(Logo, Logo_rect)  # blit image of runner

        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))  # renders score message
        score_message_rect = score_message.get_rect(center=(400, 330))  # center of text will exist at (4000, 330)
        screen.blit(game_name, game_name_rect)  # draws game name onto screen

        if score == 0:  # initial game menu
            screen.blit(game_message, game_message_rect)
        else:  # Menu after game had started (once game has started, the score is at least 1)
            screen.blit(score_message, score_message_rect)

    pygame.display.update()  # pygame's display will update
    clock.tick(60)  # cap fps = 60

    
