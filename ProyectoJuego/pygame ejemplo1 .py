import pygame
import sys
from pathlib import Path
#inicializar pygame
pygame.init()
#configurar la pantalla
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Ejemplo de Pygame")

#bucle piencipla del juego 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
#Logica del juego
          
# Dibujar en la pantalla 
screen.fill((255,255,255))
pygame.display.flip()

#Salir del programa 
pygame.quit()
sys.exit()

# Pon esto en la sección #2, defininiendo una consante
BASE_PATH = Path(__file__).resolve().parent
 
# Construye una ruta absoluta para el archivo ball.png
pathToBall = str(BASE_PATH) + '/images/ball.png'