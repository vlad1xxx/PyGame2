import pygame

pygame.init()
pygame.display.set_caption('Движущийся круг 2')
size = width, height = 200, 200
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
fps = 60
clock = pygame.time.Clock()
running = True
count = 0
font = pygame.font.Font(None, 100)


while running:
    screen.fill((0, 0, 0))
    text = font.render(str(count), True, (255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEOEXPOSE:
            count += 1
    screen.blit(text, (75, 75))
    pygame.display.flip()
    clock.tick(fps)