import pygame
from ball import player1, player2, ball
from config import ScreenWidth, ScreenHeight, all_sprites, players, balls, fps

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
# Game Loop
screen = pygame.display.set_mode([ScreenWidth, ScreenHeight])
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("Assets/Pong.jpg"))

pygame.font.init()

my_font = pygame.font.Font("Assets/CuteFont-Regular.ttf", 50)

running = True


def WIN(x):
    winner_text = my_font.render(x + " " + "Wins!", False, (255, 255, 255))
    winner_rect = winner_text.get_rect(center=(ScreenWidth / 2, ScreenHeight / 2.5))
    screen.blit(winner_text, (winner_rect))
    pygame.display.flip()
    pygame.time.wait(10000)
    global running
    running = False


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
    text_rect = text_surface.get_rect(center=(ScreenWidth / 2, ScreenHeight * 0.05))
    screen.blit(text_surface, (text_rect))

    for object in all_sprites:
        screen.blit(object.surf, object.rect)

    pygame.display.flip()

    clock.tick(fps)
