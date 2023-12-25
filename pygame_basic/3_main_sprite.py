import pygame      #import pygame

pygame.init()           #initialize pygame (must)

#set screen size
screen_width = 480      #width
screen_height = 640         #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title
pygame.display.set_caption("Nado Game")     

#upload background image (right click on image file>copy path)
background = pygame.image.load("/Users/min/Desktop/Nadocoding/Pythonworkspace/Advanced_1/‎Background.png")

#upload character
character = pygame.image.load("/Users/min/Desktop/Nadocoding/Pythonworkspace/Advanced_1/character.png")
character_size = character.get_rect().size      #get image size
character_width = character_size[0]         #get character width
character_height = character_size[1]        #get character height
character_x_pos = screen_width / 2 - character_width / 2     #place character in the middle of screen width
character_y_pos = screen_height - character_height        #place character in the bottom of screen height

#event loop
running = True      #check if game is running
while running:
    for event in pygame.event.get():        #get event
        if event.type == pygame.QUIT:           #if windows closed
            running = False
    screen.blit(background, (0, 0))     #draw backgrounds

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()         #update display while running

#quite pygame
pygame.quit()