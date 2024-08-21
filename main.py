import pygame

from settings import HEIGHT, WIDTH, ground_space
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + ground_space))
pygame.display.set_caption("Flappy Bird")

class Main:
    def __init__(self, screen):
        self.screen = screen

    def main(self):
        world = World(screen)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        world.update("jump")

            world.update()

            # Update the display with the new position of the bird
            pygame.display.flip()

if __name__ == '__main__':
    play = Main(screen)
    play.main()
