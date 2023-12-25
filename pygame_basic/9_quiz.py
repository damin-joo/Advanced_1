import pygame      #import pygame
import random
####################################################################
#intialization (MUST)
pygame.init()           #initialize pygame (must)

#set screen size
screen_width = 480      #width
screen_height = 640         #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title
pygame.display.set_caption("Name of Game") 

#FPS
clock = pygame.time.Clock()
####################################################################
#1. User game initialization (background, game image, coordinates, font, speed, etc)
#background
background = pygame.image.load("/Users/min/Desktop/Nadocoding/Pythonworkspace/Advanced_1/‎Background.png")

#character
character = pygame.image.load("/Users/min/Desktop/Nadocoding/Pythonworkspace/Advanced_1/enemy.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

#moving coordinates & speed
to_x = 0
to_y = 0
speed = 10
enemy_speed = 0.5

#enemy character
enemy = pygame.image.load("/Users/min/Desktop/Nadocoding/Pythonworkspace/Advanced_1/character.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

#font
game_font = pygame.font.Font(None, 40)

#time
total_time = 60
start_ticks = pygame.time.get_ticks()

#event loop
running = True      #check if game is running
while running:
    dt = clock.tick(30)         #set frame rate to 30 (lower the slower, higher faster)

####################################################################
    #2. Event process
    for event in pygame.event.get():        #get event
        if event.type == pygame.QUIT:           #if windows closed
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
####################################################################
    #3. Gamer character position
    character_x_pos += to_x
    enemy_y_pos += to_y

    #enemy falling from the sky
    to_y += enemy_speed

    #width window contstrain
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #if enemy reaches bottom screen
    if enemy_y_pos > screen_height - enemy_height:
        #new enemy created
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0
        to_y = 0
####################################################################
    #4. Collision
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
 ####################################################################
    #5. Draw to screen   
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #timer
    elasped_time = (pygame.time.get_ticks() - start_ticks)/1000
    timer = game_font.render(str(int(total_time - elasped_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    #end game if time out
    if total_time - elasped_time <= 0:
        print("timeout")
        running = False

    pygame.display.update()         #update display while running

pygame.quit()