import pygame
from values import *
from ball import Ball

pygame.init()

clock = pygame.time.Clock()

def main():
    screen = pygame.display.set_mode((HEIGHT, WIDTH))

    loop = True
    background = pygame.Surface(screen.get_size())

    ball = Ball(screen, (HEIGHT/2, WIDTH/2))

    while(loop):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False

        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        ball.update()

        pygame.display.flip()

        clock.tick(60)

main()
