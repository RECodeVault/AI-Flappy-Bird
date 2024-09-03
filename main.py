import os
import pygame
import neat

from settings import HEIGHT, WIDTH
from world import World
from bird import Bird

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

main_screen = pygame.image.load('assets/background/background-day.png').convert()
bg_scaled_main_screen = pygame.transform.scale(main_screen, (WIDTH, HEIGHT))
main_screen_message = pygame.image.load('assets/background/main_screen_message.png')
scaled_main_screen_message = pygame.transform.scale(main_screen_message, (276, 400))


def main(genomes, config, population):
    nets = []
    ge = []
    birds = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(screen))
        ge.append(genome)

    world = World(screen, birds)
    clock = pygame.time.Clock()
    game_state = "playing"

    while game_state == "playing":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(bg_scaled_main_screen, (0, 0))

        pipe_idx = 0
        if len(world.pipes) > 0:
            if len(world.pipes) > 1 and birds[0].x > world.pipes[0].x + world.pipes[0].width:
                pipe_idx = 1

            if 0 <= pipe_idx < len(world.pipes):
                pipe = world.pipes[pipe_idx]
                for x, bird in enumerate(birds):
                    if bird.alive:
                        ge[x].fitness += 0.1

                        if pipe.top_size < bird.y < pipe.bottom_pipe_top:
                            ge[x].fitness += 0.5
                        else:
                            ge[x].fitness -= 0.2

                        output = nets[x].activate((
                            bird.y,
                            abs(bird.y - pipe.top_size),
                            abs(bird.y - pipe.bottom_pipe_rect.top)
                        ))

                        if output[0] > 0.5:
                            ge[x].fitness += 0.1
                            bird.jump()
                            bird.update()

                        if bird.x > pipe.x + pipe.width:
                            ge[x].fitness += 5

        world.update_game_statistics_visual(population.generation)
        world.update()

        for x, bird in enumerate(birds):
            if bird.alive:
                bird.update()

                if bird.y >= HEIGHT - bird.size or world.check_collision():
                    ge[x].fitness -= 10
                    bird.alive = False

        if all(not bird.alive for bird in birds):
            world.reset()
            break

        pygame.display.flip()
        clock.tick(900)


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(lambda genomes, config: main(genomes, config, p), 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)

