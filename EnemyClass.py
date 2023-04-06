import pygame
from random import randint, choice


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        #self.test = pygame.image.load('Gigapunzel.png').convert_alpha()  # Loads ninja cover image
        #self.test = pygame.transform.scale(self.test, (64, 64))  # Scales the image
        # self.test = pygame.image.load('graphics/Ninja/Blue.png').convert_alpha()
        if type == 'fly':
            fly_1 = pygame.image.load('graphics/Fly/Fly1.png').convert()
            fly_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 380

        else:
            snail_1 = pygame.image.load('graphics/Snail/snail1.png').convert()
            snail_2 = pygame.image.load('graphics/Snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 500

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        # self.image = self.test
        self.rect.x -= 10
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
