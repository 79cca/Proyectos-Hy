import pygame
import sys
pygame.init()
WIDTH,HEIGHT = 800,600
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Movimiento con teclado en Pygame")
x,y = 400,300
vel = 5
while True:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
keys = pygame.key.get_pressed()
if key [pygame.K_LEFT]:
    x  -= vel
if keys [pygame,K_RIGHT]:
    X+=vel
if keys[pygame.K_UP]:
    y-= vel
if keys [pygame.K_DOWN]:
    y += vel
windoy.fill((0,0,0))
pygame.draw.rect(window,(255,0,0),(x,y,50,50))
pygame.display.update()

    