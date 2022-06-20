import I2C_LCD_driver
import pygame
from pygame.locals import *
from screens.direction import Direction
# Views
from screens.home import Home
from screens.speed import Speed
from screens.direction import Direction

# Declaración de constantes y variables
WHITE = (255, 255, 255)
mylcd = I2C_LCD_driver.lcd()
numero = ''
valor = 0
menu = ''

# Función principal del juego


def main():
    speed_val = 0
    direction_val = 1
    menu = 'Home'
    # Se inicializa el juego
    pygame.init()
    pygame.display.set_caption("Cuarta Entrega")
    screen = pygame.display.set_mode((480, 360))

    # Bucle principal
    while True:

        # 1.- Se dibuja la pantalla
        # screen.fill(WHITE)
        if menu == 'Home':
            home = Home(screen, mylcd, speed_val, direction_val)
            menu = home.show_screen()
        elif menu == 'Speed':
            speed = Speed(screen, mylcd)
            speed_val = speed.show()
            menu = 'Home'
        elif menu == 'Direction':
            direction = Direction(screen, mylcd)
            direction_val = direction.show()
            menu = 'Home'

    # Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':

    main()
