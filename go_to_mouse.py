import pygame

pygame.init()
pygame.display.set_caption('Движущийся круг 2')
size = width, height = 501, 501
screen = pygame.display.set_mode(size)
fps = 100
clock = pygame.time.Clock()
running = True
screen.fill((0, 0, 0))
circle_x, circle_y = (251, 251)
mouse_x = 251
mouse_y = 251


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            print(mouse_x, mouse_y)
            print(circle_x, circle_y)

    if circle_y > mouse_y:
        circle_y -= 1
    elif circle_y < mouse_y:
        circle_y += 1
    if circle_x < mouse_x:
        circle_x += 1
    elif circle_x > mouse_x:
        circle_x -= 1
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), 20)
    pygame.display.flip()
    clock.tick(fps)