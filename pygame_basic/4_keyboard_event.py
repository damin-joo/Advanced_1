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

#character position
character_x_pos = screen_width / 2 - character_width / 2     #place character in the middle of screen width
character_y_pos = screen_height - character_height        #place character in the bottom of screen height

#moving coordinates
to_x =0
to_y =0

#event loop
running = True      #check if game is running
while running:
    for event in pygame.event.get():        #get event
        if event.type == pygame.QUIT:           #if windows closed
            running = False

        if event.type == pygame.KEYDOWN:        #if key is pressed
            if event.key == pygame.K_LEFT:          #move character
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        
        if event.type == pygame.KEYUP:      #stop if key is not pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0 

    character_x_pos += to_x
    character_y_pos += to_y  

    #width window constraint 
    if character_x_pos < 0: 
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #height window constraint
    if character_y_pos < 0: 
        character_y_pos =0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))     #draw backgrounds

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()         #update display while running

#quite pygame
pygame.quit()