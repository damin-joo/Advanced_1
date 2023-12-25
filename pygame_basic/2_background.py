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

#event loop
running = True      #check if game is running
while running:
    for event in pygame.event.get():        #get event
        if event.type == pygame.QUIT:           #if windows closed
            running = False
    #screen.fill((0, 0, 255))           #RGB background fill
    screen.blit(background, (0, 0))     #draw backgrounds

    pygame.display.update()         #update display while running

#quite pygame
pygame.quit()