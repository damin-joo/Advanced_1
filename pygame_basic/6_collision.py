import pygame      #import pygame

pygame.init()           #initialize pygame (must)

#set screen size
screen_width = 480      #width
screen_height = 640         #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title
pygame.display.set_caption("Nado Game") 

#FPS
clock = pygame.time.Clock()

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

#moving  speed
character_speed = 0.5

#enemy character
enemy = pygame.image.load("/Users/min/Desktop/Nadocoding/Pythonworkspace/Advanced_1/enemy.png")
enemy_size = enemy.get_rect().size      #get image size
enemy_width = enemy_size[0]         #get enemy width
enemy_height = enemy_size[1]        #get enemy height
enemy_x_pos = screen_width / 2 - enemy_width / 2     #place character in the middle of screen width
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)      #place character in the bottom of screen height

#event loop
running = True      #check if game is running
while running:
    dt = clock.tick(60)         #set frame rate to 30 (lower the slower, higher faster)

    for event in pygame.event.get():        #get event
        if event.type == pygame.QUIT:           #if windows closed
            running = False

        if event.type == pygame.KEYDOWN:        #if key is pressed
            if event.key == pygame.K_LEFT:          #move character
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP:      #stop if key is not pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0 

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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

    #collide event rect info update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #check collision
    if character_rect.colliderect(enemy_rect):
        print("collision occured")
        running = False

    screen.blit(background, (0, 0))     #draw backgrounds

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()         #update display while running

#quite pygame
pygame.quit()