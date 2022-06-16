import I2C_LCD_driver
import random, pygame, sys
from pygame.locals import *
import menus

# Declaración de constantes y variables
WHITE = (255, 255, 255)
mylcd = I2C_LCD_driver.lcd()
OPTIONS = [
	{
		'option':1,
		'text': 'Velocidad'
	},
	{
		'option':2,
		'text': 'Sentido'
	},
	{
		'option':3,
		'text': '# Vueltas'
	},
	{
		'option':4,
		'text': 'Iniciar'
	}
]
selected = 0;

# Funcion para mostrar el menu con Scroll
def mostrar_menu(is_going_down):
	
	mylcd.lcd_clear()
	new_options = OPTIONS[selected-is_going_down:selected+2-is_going_down]
		
	mylcd.lcd_display_string(new_options[0].get('text'), 1)
	mylcd.lcd_display_string(new_options[1].get('text'), 2) 
	mylcd.lcd_display_string('*', is_going_down+1, 15)


# Función principal del juego
def main():
	global selected
	# Se inicializa el juego
	pygame.init()
	pygame.display.set_caption("Título del juego")
	screen = pygame.display.set_mode((480,360))
	mostrar_menu(0)
	
	# Bucle principal
	while True:
		
		
		# 1.- Se dibuja la pantalla
		screen.fill(WHITE)

		# 2.- Se comprueban los eventos
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit(0)
		  
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN and len(OPTIONS)>selected+1:
					selected+=1
					mostrar_menu(1)
				elif event.key == pygame.K_UP and 0<selected:
					selected-=1
					mostrar_menu(0)
			
			

    # 3.- Se actualiza la pantalla
		pygame.display.update()

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
	
	main()