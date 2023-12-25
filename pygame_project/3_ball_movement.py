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

#character direction
character_to_x = 0

#character speed
character_speed = 5

#weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_height = weapon_size[1]
weapon_width = weapon_size[0]

#multiple weaons fired
weapons = []

#weapon speed
weapon_speed = 10

#make balls
ball_images = [
    pygame.image.load(os.path.join(image_path, "ball1.png")),
    pygame.image.load(os.path.join(image_path, "ball2.png")),
    pygame.image.load(os.path.join(image_path, "ball3.png"))]

#initial speed for each ball
ball_speed_y = [-18, -15, -12]  

#balls
balls = []

#first ball init
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "image_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_spd_y":ball_speed_y[0]})


running = True      #check if game is running
while running:
    dt = clock.tick(30)         #set frame rate to 30 (lower the slower, higher faster)

####################################################################
    #2. Event process
    for event in pygame.event.get():        #get event
        if event.type == pygame.QUIT:           #if windows closed
            running = False
        
        if event.type == pygame.KEYDOWN:    #if key pressed
            if event.key == pygame.K_LEFT:      #move character left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width /2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])    #add current weapon position
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

####################################################################
    #3. Gamer cahracter position
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #change weapon position
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]       #move weapons up

    #hide weaons when ceiling hit
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]      #only list weapons that have not yet reach ceiling

    #ball position
    for ball_idx, ball_val in enumerate(balls):     #print out ball_val for each index
        ball_pos_x = ball_val["pos_x"] 
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["image_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #change direction when wall hit (bounce back)
        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        #change direction when hit stage (bounce back) and decrease speed consecutively (parabola) so acts like gravity
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
        

####################################################################
    #4. Collision
####################################################################
    #5. Draw to screen
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["image_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))    

####################################################################
    pygame.display.update()         #update display while running

pygame.quit()