import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED
from pygame.locals import K_DOWN, K_UP, K_a, K_z


class Player(pygame.sprite.Sprite):
    def __init__(self, is_left):
        super(Player, self).__init__()

        self.surf = pygame.Surface((SCREEN_WIDTH / 20, SCREEN_HEIGHT / 7))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.score = 0
        self.rect.x = 0 if is_left else SCREEN_WIDTH - (SCREEN_WIDTH / 20)
        self.rect.y = 0
        self.PlayerSpeed = PLAYER_SPEED
        self.is_left = is_left

    def update(self, pressed_keys):
        def get_shmovement():
            if self.is_left:
                return {K_a: (0, -self.PlayerSpeed), K_z: (0, self.PlayerSpeed)}
            else:
                return {K_UP: (0, -self.PlayerSpeed), K_DOWN: (0, self.PlayerSpeed)}

        movements = get_shmovement()
        for key, (dx, dy) in movements.items():
            if pressed_keys[key]:
                self.rect.move_ip(dx, dy)
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
