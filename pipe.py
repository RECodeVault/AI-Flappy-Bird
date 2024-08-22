import pygame
import random
from settings import WIDTH, HEIGHT, pipe_pair_sizes, pipe_size, pipe_gap


class Pipe:
    def __init__(self, screen):
        self.screen = screen
        self.width = 80
        self.color = (0, 255, 0)
        self.x = float(WIDTH)
        self.speed = 0.2
        self.passed = False

        size_pair = random.choice(pipe_pair_sizes)
        top_size = size_pair[0] * pipe_size
        bottom_size = size_pair[1] * pipe_size

        self.top_pipe_rect = pygame.Rect(int(self.x), 0, self.width, top_size)
        self.bottom_pipe_rect = pygame.Rect(int(self.x), top_size + pipe_gap, self.width, HEIGHT - (top_size + pipe_gap))

    def move(self):
        self.x -= self.speed
        self.top_pipe_rect.x = int(self.x)
        self.bottom_pipe_rect.x = int(self.x)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.top_pipe_rect)
        pygame.draw.rect(self.screen, self.color, self.bottom_pipe_rect)

    def is_off_screen(self):
        return self.top_pipe_rect.right < 0
