import pygame

# Screen Resolution
ScreenWidth = 800
ScreenHeight = 600

# How fast the paddles should move
fps = 60
PlayerSpeed = 3

# Configure the ball

BallSpeed = 2
BallSize = 10
# Sprite Groups
players = pygame.sprite.Group()
balls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
