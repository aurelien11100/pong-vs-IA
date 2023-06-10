import pygame

class raquette:
    def __init__(self, screen, pos):
        self.hitbox = pygame.Rect(pos, (20, 20))

        screen.blit(self.hitbox)
    
    
    def update():
        pass
        