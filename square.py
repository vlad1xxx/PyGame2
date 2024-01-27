import pygame

pygame.init()
pygame.display.set_caption('Движущийся круг 2')
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
fps = 60
sq_x, sq_y = 0, 0
move_x, move_y = 0, 0
clock = pygame.time.Clock()
running = True
circle = False
pos_circle = None
drag = False

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sq_x <= event.pos[0] <= sq_x + 100 and sq_y <= event.pos[1] <= sq_y + 100:
                drag = True
                move_x = event.pos[0] - sq_x
                move_y = event.pos[1] - sq_y
        elif event.type == pygame.MOUSEBUTTONUP:
            drag = False
        elif event.type == pygame.MOUSEMOTION and drag:
            sq_x = event.pos[0] - move_x
            sq_y = event.pos[1] - move_y

    pygame.draw.rect(screen, (0, 255, 0), (sq_x, sq_y, 100, 100))
    pygame.display.flip()
    clock.tick(50)