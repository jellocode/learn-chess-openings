import pygame

pygame.init()

# creating game window
display = pygame.display
surface = display.set_mode((600,600))
surface.fill((215,200,250))
display.flip()

running = True
while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False

