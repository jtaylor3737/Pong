from enum import Enum
import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH, BALL_SPEED, BALL_SIZE
import random
from global_stuff import player1, player2, players

# Sound Effect Call


class LastHit(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2


def play_sound(Sound):
    unused_channel = pygame.mixer.find_channel()
    if unused_channel:
        unused_channel.play(pygame.mixer.Sound("Assets/" + Sound))


# Pong Ball Class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()

        self.surf = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.surf.fill((255, 100, 180))
        self.rect = self.surf.get_rect()
        self.rect.y = SCREEN_HEIGHT / 2 - BALL_SIZE
        self.rect.x = SCREEN_WIDTH / 2 - BALL_SIZE
        self.BallSpeed = BALL_SPEED
        self.SpeedRange = (-self.BallSpeed, self.BallSpeed)
        self.BallSpeedX = random.choice(self.SpeedRange)
        self.BallSpeedY = random.choice(self.SpeedRange)
        self.last_hit = LastHit.NONE

    def update(self):
        def on_reset():
            self.rect.y = SCREEN_HEIGHT / 2 - BALL_SIZE
            self.rect.x = SCREEN_WIDTH / 2 - BALL_SIZE
            self.last_hit = LastHit.NONE
            play_sound("peeeeeep.ogg")

        self.rect.move_ip(self.BallSpeedX, self.BallSpeedY)

        paddle = pygame.sprite.spritecollideany(self, players)

        if paddle:
            match self.last_hit:
                case LastHit.NONE:
                    self.last_hit = LastHit.LEFT if paddle.is_left else LastHit.RIGHT
                case LastHit.LEFT:
                    if paddle.is_left:
                        return
                    self.last_hit = LastHit.RIGHT
                case LastHit.RIGHT:
                    if not paddle.is_left:
                        return
                    self.last_hit = LastHit.LEFT

            if (self.rect.top < paddle.rect.top
                        or self.rect.bottom > paddle.rect.bottom
                    ):
                self.BallSpeedY = -self.BallSpeedY
            else:
                self.BallSpeedX = -self.BallSpeedX * 1.05
                self.BallSpeedY = self.BallSpeedY * 1.05
                player1.PlayerSpeed = player1.PlayerSpeed * 1.05
                player2.PlayerSpeed = player2.PlayerSpeed * 1.05
                play_sound("beeep.ogg")

        if (self.rect.y < 0) or (self.rect.y > SCREEN_HEIGHT):
            self.BallSpeedY = -self.BallSpeedY
            play_sound("plop.ogg")
        if self.rect.x < 0:
            player2.score = player2.score + 1
            on_reset()
        if self.rect.x > SCREEN_WIDTH:
            player1.score = player1.score + 1
            on_reset()


ball = Ball()
