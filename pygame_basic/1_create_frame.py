import pygame      #import pygame

pygame.init()           #initialize pygame (must)

#set screen size
screen_width = 480      #width
screen_height = 640         #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title
pygame.display.set_caption("Nado Game")     


#event loop
running = True      #check if game is running
while running:
    for event in pygame.event.get():        #get event
        if event.type == pygame.QUIT:           #if windows closed
            running = False

#quite pygame
pygame.quit()