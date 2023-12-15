import pygame

pygame.init()

# creating game window
display = pygame.display
display.set_mode((600,600))

running = True
while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False

