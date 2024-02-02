import pygame
from player import Player

player1 = Player(is_left=True)
player2 = Player(is_left=False)

# Sprite Groups
players = pygame.sprite.Group()
balls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
