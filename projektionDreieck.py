import pygame
from linearAlgebra import *



pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

clock = pygame.time.Clock()

p1 = np.array([3, 4, 2, 1])
p2 = np.array([2, 1, 1, 1])
p3 = np.array([1, 5, 3, 1])

triangle = [p1, p2, p3]

is_running = True
rotX = 0
rotY = 0
rotZ = 0
while is_running:



    points = []
    for p in range(len(triangle)):
        vec2d = threeD2Screen(triangle[p], rotX, rotY, rotZ, 0, 0, 0, 0, 0, 7, 2, 2, 1, 20, 800, 600)
        points.append((vec2d[0], vec2d[1]))

    pygame.draw.polygon(background, (255, 0, 255), points)
        

    #rotX += 1
    rotY += 2
    
        #print((vec2d[0], vec2d[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             is_running = False

    window_surface.blit(background, (0, 0))
    background.fill(pygame.Color('#000000'))
    
    pygame.display.update()
    clock.tick(60)
