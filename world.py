from bird import Bird

class World:
    def __init__(self, screen):
        self.player = Bird(screen)

    def update(self, player_input=None):
        if player_input == "jump":
            self.player.jump()

        # Update bird's position with gravity and draw it
        self.player.update()
