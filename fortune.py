import pygame, sys, os, pygame.mixer
from pygame.locals import *

pygame.init();

pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.music.set_volume(1)
# pygame.mixer.music.load("doorbell.ogg")

size = width, height = 640,480

window = pygame.display.set_mode(size, pygame.FULLSCREEN)
#window = pygame.display.set_mode((1366/2, 768/2))

# pygame.display.set_caption('Fortune Teller')

screen = pygame.display.get_surface()
bg = pygame.image.load('background.jpg')
bg = pygame.transform.scale(bg, size)

screen.blit(bg, (0, 0))
pygame.display.update()
pygame.mouse.set_visible(0)
mystic = pygame.mixer.music.load('mystic.mp3')
pygame.mixer.music.play()

def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
        	print "random shite"		
        	pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            print "------------------------------------\nGoodbye!\n"
            sys.exit(0)


while True:
    input(pygame.event.get())