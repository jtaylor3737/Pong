import pygame
from config import ScreenHeight, ScreenWidth, players, BallSpeed, BallSize
import random
from players import Player1, Player2

player1 = Player1()
player2 = Player2()


# Sound Effect Call
def SoundEffect(Sound):
    unused_channel = pygame.mixer.find_channel()
    if unused_channel:
        unused_channel.play(pygame.mixer.Sound("Assets/" + Sound))


# Pong Ball Class


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()

        self.surf = pygame.Surface((BallSize, BallSize))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.y = ScreenHeight / 2 - BallSize
        self.rect.x = ScreenWidth / 2 - BallSize
        self.BallSpeed = BallSpeed
        self.SpeedRange = (-self.BallSpeed, self.BallSpeed)
        self.BallSpeedX = random.choice(self.SpeedRange)
        self.BallSpeedY = random.choice(self.SpeedRange)

    def update(self):
        self.rect.move_ip(self.BallSpeedX, self.BallSpeedY)

        if pygame.sprite.spritecollideany(self, players):
            paddles = pygame.sprite.spritecollideany(self, players)
            self.rect.move_ip(0, -self.BallSpeedY * 2)
            if (
                self.rect.top < paddles.rect.top
                or self.rect.bottom > paddles.rect.bottom
            ):
                self.BallSpeedY = -self.BallSpeedY
            else:
                self.BallSpeedX = -self.BallSpeedX
                self.BallSpeedX = self.BallSpeedX * 1.05
                self.BallSpeedY = self.BallSpeedY * 1.05
                player1.PlayerSpeed = player1.PlayerSpeed * 1.05
                player2.PlayerSpeed = player2.PlayerSpeed * 1.05
                SoundEffect("beeep.ogg")
        if (self.rect.y < 0) or (self.rect.y > ScreenHeight):
            self.BallSpeedY = -self.BallSpeedY
            SoundEffect("plop.ogg")
        if self.rect.x < 0:
            player2.score = player2.score + 1
            self.rect.y = ScreenHeight / 2 - BallSize
            self.rect.x = ScreenWidth / 2 - BallSize
            SoundEffect("peeeeeep.ogg")
        if self.rect.x > ScreenWidth:
            player1.score = player1.score + 1
            self.rect.y = ScreenHeight / 2 - BallSize
            self.rect.x = ScreenWidth / 2 - BallSize
            SoundEffect("peeeeeep.ogg")


ball = Ball()
