import pygame
from ball import ball, LastHit
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BALL_SIZE, PLAYER_SPEED
from global_stuff import all_sprites, players, balls
from player import player1, player2
import random

# Import pygame.locals for easier access to key coordinates
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_n, K_y


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
# Game Loop
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("Assets/Pong.jpg"))

pygame.font.init()

my_font = pygame.font.Font("Assets/CuteFont-Regular.ttf", 50)

running = True


def WIN(who_won):
    winner_text = my_font.render(who_won + " " + "Wins!", False, (255, 255, 255))
    winner_rect = winner_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5))
    play_again = my_font.render("Play Again? (y/n)", False, (255, 255, 255))
    play_rect = play_again.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.75))
    screen.blit(winner_text, (winner_rect))
    screen.blit(play_again, play_rect)
    pygame.display.flip()
    awaiting = True
    while awaiting:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_n:
                    global running
                    running = False
                    awaiting = False
                elif event.key == K_y:
                    player1.score = 0
                    player2.score = 0
                    ball.rect.y = SCREEN_HEIGHT / 2 - BALL_SIZE
                    ball.rect.x = SCREEN_WIDTH / 2 - BALL_SIZE
                    ball.last_hit = LastHit.NONE
                    ball.BallSpeedX = random.choice(ball.SpeedRange)
                    ball.BallSpeedY = random.choice(ball.SpeedRange)
                    player1.PlayerSpeed = PLAYER_SPEED
                    player2.PlayerSpeed = PLAYER_SPEED
                    awaiting = False


all_sprites.add(player1)
players.add(player1)
all_sprites.add(player2)
players.add(player2)
all_sprites.add(ball)
balls.add(ball)


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
    if player1.score == 5:
        WIN("Player One")
    elif player2.score == 5:
        WIN("Player Two")

    pressed_keys = pygame.key.get_pressed()

    ball.update()
    players.update(pressed_keys)
    screen.fill((0, 0, 0))

    text_surface = my_font.render(
        "P1:" + str(player1.score) + " | " + "P2:" + str(player2.score),
        False,
        (255, 255, 255),
    )
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.05))
    screen.blit(text_surface, (text_rect))

    for object in all_sprites:
        screen.blit(object.surf, object.rect)

    pygame.display.flip()

    clock.tick(FPS)
