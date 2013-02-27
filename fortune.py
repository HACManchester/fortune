import pygame, sys, os, pygame.mixer, pygame.font
from pygame.locals import *

size = width, height = 640,480
white = (255, 255, 255)
window = ''
screen = ''
bg = ''
mystic = ''

pygame.init();

pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.music.set_volume(1)

window = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen = pygame.display.get_surface()
bg = pygame.image.load('background.jpg')
mystic = pygame.mixer.music.load('mystic.mp3')

bg = pygame.transform.scale(bg, size)
screen.blit(bg, (0, 0))
pygame.display.update()
pygame.mouse.set_visible(0)

def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor):
	global screen
	# pick a font you have and set its size
	myfont = pygame.font.SysFont(Textfont, Textsize)
	# apply it to text on a label
	label = myfont.render(txtText, 1, Textcolor)
	# put the label object on the screen at point Textx, Texty
	screen.blit(label, (Textx, Texty))
	# show the whole thing
	pygame.display.flip()

def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
        	
        	printText(msg, 'Times New Roman', 30, 0, 0, white)
        	pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            print "------------------------------------\nGoodbye!\n"
            sys.exit(0)


while True:
    input(pygame.event.get())