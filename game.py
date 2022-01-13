import pygame

# Asentaa pygamen
pygame.init()

# Luo näytön pelille
ruutu = pygame.display.set_mode((800, 600))

#Ruudun taustaväri RGB
ruutu.fill ((32, 32, 32))
pygame.display.update()

# Nimi ja kuvake

pygame.display.set_caption("Pyton")
icon = pygame.image.load('ico.jpg')
pygame.display.set_icon(icon)

pygame.display.update()

#Pelaaja
playerImg = pygame.image.load('pelaaja.png')
playerX = 370
playerY = 480

def player():
    ruutu.blit(playerImg, (playerX, playerY))

#Piirtää pelaajan ruudulle.
player()
pygame.display.update()


# Pelin Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False