import pygame
import random
from settings import WIDTH, HEIGHT, pipe_pair_sizes, pipe_size, pipe_gap, ground_space


class Pipe:
    def __init__(self, screen):
        self.screen = screen
        self.x = float(WIDTH)
        self.speed = 0.6
        self.passed = False

        self.image = pygame.image.load('assets/pipe/pipe-green.png').convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        size_pair = random.choice(pipe_pair_sizes)
        top_size = size_pair[0] * pipe_size
        bottom_size = size_pair[1] * pipe_size

        self.top_pipe_rect = pygame.Rect(int(self.x), 0, self.width, top_size)
        self.bottom_pipe_rect = pygame.Rect(int(self.x), top_size + pipe_gap, self.width, bottom_size)

        self.top_pipe_image = pygame.transform.flip(self.image, False, True)

        self.bottom_pipe_image = pygame.transform.scale(self.image, (self.width, HEIGHT // 1.5))

        self.ground_image = pygame.image.load('assets/background/base.png').convert()

    def move(self):
        self.x -= self.speed
        self.top_pipe_rect.x = int(self.x)
        self.bottom_pipe_rect.x = int(self.x)

    def draw(self):
        self.screen.blit(self.bottom_pipe_image, (self.x, self.bottom_pipe_rect.y))

        self.screen.blit(self.top_pipe_image, (self.x, self.top_pipe_rect.bottom - self.height))

        self.ground_image = pygame.transform.scale(self.ground_image, (WIDTH, ground_space))
        self.screen.blit(self.ground_image, (0, HEIGHT))

    def is_off_screen(self):
        return self.top_pipe_rect.right < 0
