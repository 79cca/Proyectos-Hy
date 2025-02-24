# pygame demo 0 - window only
# 1 - Import packages
#  Este código es una plantilla generica  para usar como punto de partida
#  este programa  abre una ventana y pinta todo su contenido negro.  


import pygame
from pygame.locals import *
import sys
# 2 - Definimos constantes
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
# 3 - Iniciamos el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

clock = pygame.time.Clock()
  # 4 - Cargamos asssets: imagenes(s), sonido(s), etc.
ballImage = pygame.image.load('images/ball.png')

  # 5 - Inicializamos variables

  # 6 - Loop por siempre
while True:
  # 7 - Verificar y manejar los eventos
  for event in pygame.event.get():
    # ¿Se hizo clic en el botón de cerrar? Salir de pygame y finalizar el programa
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # 8 - Realizar acciones "por cuadro"
    # 9 - Limpiar la ventana
    window.fill(BLACK)
    # 10 - Dibujar todos los elementos de la ventana
    window.blit(ballImage, (100,200))
    # 11 - Actualizar la ventana
    pygame.display.update()
    # 12 - Ralentizar un poco las cosas
    clock.tick(FRAMES_PER_SECOND)
    
# Ruta (absoluta (relativa ))

from pathlib import Path
# Pon esto en la sección #2, defininiendo una consante
BASE_PATH = Path(__file__).resolve().parent
 
# Construye una ruta absoluta para el archivo ball.png
pathToBall = str(BASE_PATH) + '/images/ball.png'