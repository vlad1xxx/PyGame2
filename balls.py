import pygame

pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
fps = 100
r = 10
clock = pygame.time.Clock()
running = True
circle = False
pos_circle = None
circles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            ball = {'x': event.pos[0], 'y': event.pos[1], 'move_x': False, 'move_y': True}
            circles.append(ball)
    screen.fill((0, 0, 0))
    for elem in circles:
        elem['x'] += 1 if elem['move_x'] else -1
        elem['y'] += 1 if elem['move_y'] else -1
        if elem['x'] >= width or elem['x'] <= 0:
            elem['move_x'] = not elem['move_x']
        if elem['y'] >= height or elem['y'] <= 0:
            elem['move_y'] = not elem['move_y']
        pygame.draw.circle(screen, (255, 255, 255), (elem['x'], elem['y']), 10)
    pygame.display.flip()
    clock.tick(fps)