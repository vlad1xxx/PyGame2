import pygame

pygame.init()
pygame.display.set_caption('Движущийся круг 2')
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 255))
fps = 60
r = 10
clock = pygame.time.Clock()
running = True
circle = False
pos_circle = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((0, 0, 255))
            r = 10
            pos_circle = event.pos
            circle = True
    if circle:
        r += 10
        pygame.draw.circle(screen, (255, 255, 0), pos_circle, r)
    pygame.display.flip()
    clock.tick(fps)