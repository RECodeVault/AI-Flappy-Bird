# TODO: THIS CLASS WILL BE FOR THE SETTINGS (VALUES AND SETTING UP GAME/IMPORTS)

WIDTH, HEIGHT = 600, 650

pipe_pair_sizes = [
    (1, 7),
    (2, 6),
    (3, 5),
    (4, 4),
    (5, 3),
    (6, 2),
    (7, 1)
]

pipe_size = HEIGHT // 10
pipe_gap = (pipe_size * 2) + (pipe_size // 2)
ground_space = 50