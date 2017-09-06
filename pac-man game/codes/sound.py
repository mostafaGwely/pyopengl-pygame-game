
import winsound
import time,sys

okay_bye = "cl.wav"
cheese  = "eatCheese.wav"
def eat():
	winsound.PlaySound(cheese, winsound.SND_FILENAME|winsound.SND_ASYNC)
	

def bye():
	winsound.PlaySound(okay_bye, winsound.SND_FILENAME|winsound.SND_ASYNC)
	time.sleep(5)
	sys.exit()
	






# import pygame,time
# pygame.init()
# pygame.display.set_mode((1,1))
# cheese = pygame.mixer.Sound("eatCheese.wav")
# def eat():
# 	if pygame.mixer.music.get_busy()== False :
# 		cheese.play()
# 	else:
# 		print("busy")

# eat()
# eat()
# eat()
# eat()