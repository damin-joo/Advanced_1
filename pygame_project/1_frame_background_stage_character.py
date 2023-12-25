import os
import pygame      #import pygame
####################################################################
#0. Intialization (MUST)
pygame.init()           #initialize pygame (must)

#set screen size
screen_width = 640     #width
screen_height =480         #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title
pygame.display.set_caption("Nado Pang") 

#FPS
clock = pygame.time.Clock()
####################################################################
#1. User game initialization (background, game image, coordinates, font, speed, etc)
current_path = os.path.dirname(__file__)    #getes current file location
image_path = os.path.join(current_path, "images")   #gets images folder

#background
background = pygame.image.load(os.path.join(image_path, "background.png"))

#build stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]    #for later use for character y position

#character 
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_height = character_size[1]
character_width = character_size[0]
character_x_pos = (screen_width /2) - (character_width /2)
character_y_pos = screen_height - character_height - stage_height

running = True      #check if game is running
while running:
    dt = clock.tick(30)         #set frame rate to 30 (lower the slower, higher faster)

####################################################################
    #2. Event process
    for event in pygame.event.get():        #get event
        if event.type == pygame.QUIT:           #if windows closed
            running = False
####################################################################
    #3. Gamer cahracter position
####################################################################
    #4. Collision
####################################################################
    #5. Draw to screen
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

####################################################################
    pygame.display.update()         #update display while running

pygame.quit()