import pygame
from settings import HEIGHT, WIDTH, ground_space

pygame.mixer.init()

class Bird:
    def __init__(self, screen):
        self.screen = screen
        self.size = 40
        self.bird_image = pygame.image.load('assets/bird/bluebird-midflap.png')
        self.bird_image = pygame.transform.scale(self.bird_image, (55, 40))
        self.background = pygame.image.load('assets/background/background-day.png').convert()
        self.bg_scaled = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.jump_sound = pygame.mixer.Sound('assets/audio/audio_wing.ogg')
        self.x = (WIDTH - self.size) // 2
        self.y = ((HEIGHT + ground_space) - self.size) // 2
        self.move_distance = 0.8
        self.gravity = 0.005
        self.velocity = 1

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def jump(self):
        self.jump_sound.play()
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
        self.screen.blit(self.bg_scaled, (0, 0))

        bg_scaled = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.screen.blit(bg_scaled, (0, 0))

        self.screen.blit(self.bird_image, self.rect)

    def update(self):
        self.apply_gravity()
        self.draw()
