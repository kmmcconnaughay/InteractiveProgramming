import pygame
import sys
import time
import random
import os
os.getcwd()

white = (255, 255, 255)

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Shuffle Music')
size = [640, 480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()



print('press 1 - play sound')
print('press 2 - play sound continuously in a loop')
print('press 3 - play sound but start with 3 seconds fade-in effect')
print('press 4 - play sound for 5 seconds')
print('press 5 - play sound 3 more times')
print('press 9 - stop playing with 3 seconds fadeout effect')
print('press 0 - stop playing instantly')

def filesfolder():
    files = []
    path = '/home/kerry/InteractiveProgramming'
    directory = os.listdir(path)
    for filename in directory:
        if filename.endswith(".wav"):
            files.append(filename)
    files.sort()
    return files

def picksong():
    files = filesfolder()
    songnum = random.randint(0, 14)
    song = files[songnum]
    print(song)
    return song

def playsound():
    # load sound file
    sound = pygame.mixer.Sound('01.wav')
    sound = pygame.mixer.Sound(self.picksong())
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        sound.play()
                        while pygame.mixer.get_busy():
                            clock.tick(1000)
                            if event.key == pygame.K_2:
                                sound.play(-1)
                            if event.key == pygame.K_3:
                                sound.play(-1, fade_ms=3000)
                            if event.key == pygame.K_4:
                                sound.play(-1, 5000)
                            if event.key == pygame.K_5:
                                sound.play(3)
                            if event.key == pygame.K_9:
                                sound.fadeout(3000)
                            if event.key == pygame.K_0:
                                sound.stop()
    screen.fill(white)
    pygame.display.update()
    clock.tick(20)
