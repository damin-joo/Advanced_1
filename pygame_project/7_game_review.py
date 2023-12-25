import os
import pygame      #import pygame
import random
####################################################################
#0. Intialization (MUST)
pygame.init()           #initialize pygame (must)

#set screen size
screen_width = 640    #width
screen_height = 480         #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title
pygame.display.set_caption("Nado Review - Flappy Bird + Nado Pang") 

#FPS
clock = pygame.time.Clock()
####################################################################
#1. User game initialization (background, game image, coordinates, font, speed, etc)
current_path = os.path.dirname(__file__)    #getes current file location
image_path = os.path.join(current_path, "images")   #gets images folder

#background
background = pygame.image.load(os.path.join(image_path, "background.png"))

#build pipe
pipe = pygame.image.load(os.path.join(image_path, "pipe.png"))
pipe_size = pipe.get_rect().size
pipe_width = pipe_size[0]
pipe_height = pipe_size[1]
pipe_x_pos = screen_width
pipe_y_pos = 0
pipes = []

#pipe stage gap length (next level after x time)
stage_gap = [100, 80, 60]

#pipe direction
pipe_to_x = 0

#pipe speed
pipe_speed = 3

#character 
character = pygame.image.load(os.path.join(image_path, "bird.png"))
character_size = character.get_rect().size
character_height = character_size[1]
character_width = character_size[0]
character_x_pos = (screen_width /2) - (character_width /2)
character_y_pos = (screen_height /2) - (character_height /2)

#character direction + speed
character_to_y = 0
character_speed = 5

#gravity
gravity = 2

#stage level
stage_level = 0


#text font 
game_font = pygame.font.Font(None, 40)

#time
total_time = 10
start_ticks = pygame.time.get_ticks()   #starting time

#game over message: Misson complete, Game over
game_result = "Game Over"


running = True      #check if game is running
while running:
    dt = clock.tick(30)         #set frame rate to 30 (lower the slower, higher faster)

####################################################################
    #2. Event process
    for event in pygame.event.get():        #get event
        if event.type == pygame.QUIT:           #if windows closed
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character_to_y -= character_speed

        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                character_to_y = 0

####################################################################
    #3. Gamer character position
    character_y_pos += character_to_y

    #gravity like 
    character_y_pos += gravity

    #pipe transition
    pipe_x_pos -= pipe_speed

    #stay within screen border
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #pipe alignment: random int from 0-(480-stage_level) (1st pipe: random_int - 240, 2nd pipe: random_int + 100)
    elapsed_time = (pygame.time.get_ticks() - start_ticks) /1000    #ms -> s


    if(int(elapsed_time) % total_time == 0):
        random_int = random.randint(0, 480 - stage_gap[stage_level])
        pipe_x_pos = screen_width

    pipe_y1 = random_int - 440
    pipe_y2 = random_int + stage_gap[stage_level]   


####################################################################
    #4. Collision

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    pipe_rect1 = pipe.get_rect()
    pipe_rect1.left = pipe_x_pos
    pipe_rect1.top = pipe_y1

    pipe_rect2 = pipe.get_rect()
    pipe_rect2.left = pipe_x_pos
    pipe_rect2.top = pipe_y2

    if character_rect.colliderect(pipe_rect1):
        game_result = "Mission Failed"
        running = False

    if character_rect.colliderect(pipe_rect2):
        game_result = "Mission Failed"
        running = False



####################################################################
    #5. Draw to screen
    screen.blit(background, (0, 0))

    screen.blit(pipe, (pipe_x_pos, pipe_y1))
    screen.blit(pipe, (pipe_x_pos, pipe_y2))

    screen.blit(character, (character_x_pos, character_y_pos))

    #timer
    timer = game_font.render("Time : {}".format(int(elapsed_time)), True, (255,255,255)) 
    screen.blit(timer, (10, 10))

####################################################################
    pygame.display.update()         #update display while running

pygame.quit()