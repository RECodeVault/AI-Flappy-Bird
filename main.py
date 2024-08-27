import pygame
from settings import HEIGHT, WIDTH
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.game_state = "waiting"
        self.main_screen = pygame.image.load('assets/background/background-day.png').convert()
        self.bg_scaled_main_screen = pygame.transform.scale(self.main_screen, (WIDTH, HEIGHT))
        self.main_screen_message = pygame.image.load('assets/background/main_screen_message.png')
        self.scaled_main_screen_message = pygame.transform.scale(self.main_screen_message, (276, 400))

    def main(self):
        world = World(screen)
        clock = pygame.time.Clock()
        self.screen.blit(self.bg_scaled_main_screen, (0, 0))
        self.screen.blit(self.scaled_main_screen_message, (165, 75))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.game_state == "waiting":
                            self.game_state = "playing"
                        if self.game_state == "playing":
                            world.update("jump")

            if self.game_state == "playing":
                if world.update():
                    self.game_state = "waiting"
                    self.screen.blit(self.bg_scaled_main_screen, (0, 0))
                    self.screen.blit(self.scaled_main_screen_message, (165, 75))

            pygame.display.flip()
            clock.tick(900)


if __name__ == '__main__':
    play = Main(screen)
    play.main()
