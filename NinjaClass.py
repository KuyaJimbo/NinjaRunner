# when game starts, initiate player
# if player is touching the ground, make the player run
# else, make player jump (up = up animation), (down = down), (landing = land animation - Must override run)

import pygame


class Ninja(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.test = pygame.image.load('graphics/Ninja/Blue.png').convert_alpha()
        # Running graphics
        run0 = pygame.image.load('graphics/Ninja/NinjaRun1/Run0.png').convert()
        run1 = pygame.image.load('graphics/Ninja/NinjaRun1/Run1.png').convert()
        run2 = pygame.image.load('graphics/Ninja/NinjaRun1/Run2.png').convert()
        run3 = pygame.image.load('graphics/Ninja/NinjaRun1/Run3.png').convert_alpha()
        run4 = pygame.image.load('graphics/Ninja/NinjaRun1/Run4.png').convert_alpha()
        run5 = pygame.image.load('graphics/Ninja/NinjaRun1/Run5.png').convert_alpha()
        self.ninja_run = [run0, run1, run2, run3, run4, run5]
        self.ninja_run_index = 0
        self.image = self.ninja_run[self.ninja_run_index]

        # Jump graphics
        jump0 = pygame.image.load('graphics/Ninja/NinjaJump1/Jump0.png').convert()
        jump1 = pygame.image.load('graphics/Ninja/NinjaJump1/Jump1.png').convert()

        # rect attributes
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 300

        self.ninja_jump = [jump0, jump1]

        self.gravity = 1
        self.velocity = 0
        self.jump_sound = pygame.mixer.Sound('audio/audio_jump.mp3')
        self.jump_sound.set_volume(0.1)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 520:  # touching the ground
            self.velocity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.bottom >= 520:
            self.rect.bottom = 520

    # animation states
    def run(self):
        self.ninja_run_index += 0.2
        if self.ninja_run_index >= len(self.ninja_run):
            self.ninja_run_index = 0
        self.image = self.ninja_run[int(self.ninja_run_index)]

    def jump(self):
        if self.velocity <= 0:
            self.image = self.ninja_jump[0]
        elif self.velocity > 0:
            self.image = self.ninja_jump[1]

    def animation_state(self):
        if self.rect.bottom < 520:
            self.jump()
        else:
            self.run()

    # hitbox put image after
    # update
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        #self.image = self.test
