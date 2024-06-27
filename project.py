import pygame
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
fps = 30
X = 1000
Y = 1000
# dimensi
display_surface = pygame.display.set_mode((X, Y ))

# window name
pygame.display.set_caption('Game')

# make the player
display_surface.fill(white)
pygame.draw.rect(display_surface, blue,(500, 500, 50, 50))

# infinite loop
while True :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        # Draws the surface object to the screen.
        pygame.display.update()