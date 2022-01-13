import pygame

# Asentaa pygamen
pygame.init()

# Luo näytön pelille
screen = pygame.display.set_mode((800, 600))

# Nimi ja kuvake

pygame.display.set_caption("Pyton")
icon = pygame.image.load('ico.jpg')
pygame.display.set_icon(icon)

# Pelin Loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Taustanväri Punainen, Vihreä, Sininen (RGB)
screen.fill ((0, 0, 0))