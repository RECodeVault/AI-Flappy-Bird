import pygame

from settings import HEIGHT, WIDTH, ground_space

class Bird:
    def __init__(self, screen):
        self.screen = screen
        self.size = 50
        self.color = (255, 255, 255)
        self.x = (WIDTH - self.size) // 2
        self.y = ((HEIGHT + ground_space) - self.size) // 2
        self.move_distance = 2
        self.gravity = 0.01
        self.velocity = 1

    def jump(self):
        self.velocity = -self.move_distance

    def apply_gravity(self):
        self.velocity += self.gravity
        self.y += self.velocity

        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > HEIGHT + ground_space - self.size:
            self.y = HEIGHT + ground_space - self.size
            self.velocity = 0

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))

    def update(self):
        self.apply_gravity()
        self.draw()
