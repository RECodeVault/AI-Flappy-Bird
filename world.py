import pygame
from bird import Bird
from pipe import Pipe
from game_components import GameComponents
from settings import WIDTH, HEIGHT

pygame.mixer.init()


class World:
    def __init__(self, screen, birds):
        self.screen = screen
        self.birds = birds
        self.pipes = []
        self.pipe_timer = 0
        self.pipe_interval = 200
        self.pipe_spacing = WIDTH // 2
        self.game_components = GameComponents()

        self.score_font = pygame.font.Font(None, 74)

    def add_pipe(self):
        """Add a new pipe if conditions are met."""
        if not self.pipes or (self.pipes and self.pipes[-1].x < WIDTH - self.pipe_spacing):
            new_pipe = Pipe(self.screen)
            self.pipes.append(new_pipe)

    def update_pipes(self):
        """Update the position of pipes and remove those that go off-screen."""
        for pipe in self.pipes[:]:
            pipe.move()
            if pipe.is_off_screen():
                self.pipes.remove(pipe)

    def draw_pipes(self):
        """Draw all the pipes on the screen."""
        for pipe in self.pipes:
            pipe.draw()

    def update(self):
        """Update the world, including pipes."""
        # Increment the pipe timer and add a new pipe when the interval is met
        self.pipe_timer += 1
        if self.pipe_timer > self.pipe_interval:
            self.add_pipe()
            self.pipe_timer = 0

            for bird in self.birds:
                if bird.alive:
                    for pipe in self.pipes:
                        if not pipe.passed and bird.x > pipe.x + pipe.width:
                            pipe.passed = True
                            self.game_components.add_score()

        self.update_pipes()
        self.draw_pipes()

    def check_collision(self):
        """Check for collisions between birds and pipes."""
        for bird in self.birds:
            if not bird.alive:
                continue
            for pipe in self.pipes:
                if bird.rect.colliderect(pipe.top_pipe_rect) or bird.rect.colliderect(pipe.bottom_pipe_rect):
                    return True

            if bird.rect.bottom >= HEIGHT:
                return True

        return False

    def reset(self):
        """Reset the world and all birds."""
        self.__init__(self.screen, self.birds)
        for bird in self.birds:
            bird.reset()

    def update_game_statistics_visual(self, generation):
        score_text = self.score_font.render(f"Score: {self.game_components.get_score()}", True, (255, 255, 255))
        self.screen.blit(score_text, (20, 20))

        gen_text = self.score_font.render(f"Gen: {generation}", True, (255, 255, 255))
        self.screen.blit(gen_text, (20, 70))

        population_text = self.score_font.render(f"Alive: {sum(bird.alive for bird in self.birds)}", True, (255, 255, 255))
        self.screen.blit(population_text, (20, 120))

