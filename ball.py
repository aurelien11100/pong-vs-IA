import pygame
from pygame.math import Vector2

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, pos):
        self.hitbox = pygame.Rect(pos, (20, 20))
        self.screen = screen
        self.pos = pos
        self.speed = 5

        self.direction = Vector2(1, 1)

        

        print("hello")
    
    
    def update(self):
        #pygame.draw.rect(self.screen, (255, 255, 255), self.hitbox)

        self.hitbox.x += self.direction.x * self.speed
        self.hitbox.y += self.direction.y * self.speed

        self.rebond()


        #pygame.draw.rect(self.screen, "RED", self.hitbox, 1)
        pygame.draw.circle(self.screen, (255, 255, 255), self.hitbox.center, 10)
    
    def rebond(self):
        if(self.hitbox.right > self.screen.get_width()):
            self.direction.x = -1

        if(self.hitbox.bottom > self.screen.get_height()):
            self.direction.y = -1

        if(self.hitbox.left < 0):
            self.direction.x = 1

        if(self.hitbox.top < 0):
            self.direction.y = 1
    
        