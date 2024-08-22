import pygame
from settings import HEIGHT, WIDTH, ground_space
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + ground_space))
pygame.display.set_caption("Flappy Bird")


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.game_state = "waiting"

    def main(self):
        world = World(screen)
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

            pygame.display.flip()


if __name__ == '__main__':
    play = Main(screen)
    play.main()
