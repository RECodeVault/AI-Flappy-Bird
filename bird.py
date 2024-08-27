import pygame
from settings import HEIGHT, WIDTH

pygame.mixer.init()


class Bird:
    def __init__(self, screen):
        self.screen = screen
        self.size = 40

        # Load all flap images
        self.bird_images = [
            pygame.image.load('assets/bird/bluebird-upflap.png'),
            pygame.image.load('assets/bird/bluebird-midflap.png'),
            pygame.image.load('assets/bird/bluebird-downflap.png')
        ]
        # Scale all images
        self.bird_images = [pygame.transform.scale(img, (55, 40)) for img in self.bird_images]

        self.background = pygame.image.load('assets/background/background-day.png').convert()
        self.bg_scaled = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.jump_sound = pygame.mixer.Sound('assets/audio/audio_wing.ogg')
        self.x = (WIDTH - self.size) // 2
        self.y = (HEIGHT - self.size) // 2
        self.move_distance = 0.8
        self.gravity = 0.005
        self.velocity = 1

        self.animation_time = 5
        self.animation_count = 0
        self.current_image = 0

        self.rotation_angle = 0

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def jump(self):
        self.jump_sound.play()
        self.velocity = -self.move_distance

    def apply_gravity(self):
        self.velocity += self.gravity
        self.y += self.velocity

        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > HEIGHT - self.size:
            self.y = HEIGHT - self.size
            self.velocity = 0

        if self.velocity < 0:
            self.rotation_angle = min(25, self.rotation_angle + 5)
        else:
            self.rotation_angle = max(-30, self.rotation_angle - 5)

    def animate(self):
        # Update the animation frame
        self.animation_count += 1
        if self.animation_count >= self.animation_time:
            self.animation_count = 0
            self.current_image = (self.current_image + 1) % len(self.bird_images)

    def draw(self):
        self.screen.blit(self.bg_scaled, (0, 0))

        bird_image = self.bird_images[self.current_image]

        rotated_image = pygame.transform.rotate(bird_image, self.rotation_angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)

        self.screen.blit(rotated_image, rotated_rect.topleft)

    def update(self):
        self.apply_gravity()
        self.animate()
        self.draw()
