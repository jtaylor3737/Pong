import pygame
from config import ScreenWidth, ScreenHeight, PlayerSpeed
from pygame.locals import K_DOWN, K_UP, K_a, K_z

# Player2 Class, Pong Paddle


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super(Player1, self).__init__()

        self.surf = pygame.Surface((ScreenWidth / 20, ScreenHeight / 7))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.score = 0
        self.PlayerSpeed = PlayerSpeed

    def update(self, pressed_keys):
        movements = {
            K_a: (0, -self.PlayerSpeed),
            K_z: (0, self.PlayerSpeed),
        }
        for key, (dx, dy) in movements.items():
            if pressed_keys[key]:
                self.rect.move_ip(dx, dy)
        self.rect.clamp_ip(pygame.Rect(0, 0, ScreenWidth, ScreenHeight))


# Player1 Class, Pong Paddle


class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2, self).__init__()

        self.surf = pygame.Surface((ScreenWidth / 20, ScreenHeight / 7))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.score = 0
        self.rect.y = 0
        self.rect.x = ScreenWidth - (ScreenWidth / 20)
        self.PlayerSpeed = PlayerSpeed

    def update(self, pressed_keys):
        movements = {
            K_UP: (0, -self.PlayerSpeed),
            K_DOWN: (0, self.PlayerSpeed),
        }
        for key, (dx, dy) in movements.items():
            if pressed_keys[key]:
                self.rect.move_ip(dx, dy)
        self.rect.clamp_ip(pygame.Rect(0, 0, ScreenWidth, ScreenHeight))
