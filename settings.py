# TODO: THIS CLASS WILL BE FOR THE SETTINGS (VALUES AND SETTING UP GAME/IMPORTS)

WIDTH, HEIGHT = 600, 650

pipe_pair_sizes = [
    (1, 4),
    (2, 4),
    (3, 4),
    (4, 4),
    (4, 3),
    (4, 2),
    (4, 1)
]

pipe_size = HEIGHT // 10
pipe_gap = (pipe_size * 4) + (pipe_size // 4)
ground_space = 50