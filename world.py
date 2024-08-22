import pygame
from bird import Bird
from pipe import Pipe
from game_components import GameComponents
from settings import WIDTH, HEIGHT, ground_space


class World:
    def __init__(self, screen):
        self.screen = screen
        self.player = Bird(screen)
        self.pipes = []
        self.pipe_timer = 0
        self.pipe_interval = 200
        self.pipe_spacing = WIDTH // 2
        self.game_components = GameComponents()

    def add_pipe(self):
        if len(self.pipes) < 2:
            new_pipe = Pipe(self.screen)
            if not self.pipes or (self.pipes and self.pipes[-1].x < WIDTH - self.pipe_spacing):
                self.pipes.append(new_pipe)

    def update_pipes(self):
        for pipe in self.pipes:
            pipe.move()
            if pipe.is_off_screen():
                self.pipes.remove(pipe)

            if not pipe.passed and self.player.x > pipe.x + pipe.width:
                pipe.passed = True
                self.game_components.add_score()
                print(self.game_components.score)

    def draw_pipes(self):
        for pipe in self.pipes:
            pipe.draw()

    def check_collision(self):
        for pipe in self.pipes:
            if self.player.rect.colliderect(pipe.top_pipe_rect) or self.player.rect.colliderect(pipe.bottom_pipe_rect):
                return True

        if self.player.rect.bottom >= HEIGHT:
            return True

        return False

    def reset(self):
        self.__init__(self.screen)

    def update(self, player_input=None):
        if player_input == "jump":
            self.player.jump()

        self.player.update()
        self.pipe_timer += 1
        if self.pipe_timer > self.pipe_interval:
            self.add_pipe()
            self.pipe_timer = 0

        self.update_pipes()

        if self.check_collision():
            self.reset()
            self.player.x = (WIDTH - self.player.size) // 2
            self.player.y = ((HEIGHT + ground_space) - self.player.size) // 2
            self.player.draw()
            return True

        self.draw_pipes()

        return False
