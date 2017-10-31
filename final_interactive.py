import numpy
import pygame
import pygame.camera
from pygame.locals import *
import os, sys
import time, random

class Capture(object):

    def __init__(self):
        # start the camera
        pygame.init()
        pygame.camera.init()
        self.device = '/dev/video0'
        self.size = (640, 480)
        self.display = pygame.display.set_mode(self.size, 0)
        self.camera = pygame.camera.Camera(self.device, self.size) #HUV
        self.camera.start()
        self.screen = pygame.surface.Surface(self.size, 0, self.display)
        self.ccolor = (248, 111, 115)
        self.threshold = (60, 10, 10)


    def get_snapshot(self):
        self.screen = self.camera.get_image(self.screen)
        self.display.blit(self.screen, (0, 0))
        pygame.display.flip()

    def main(self):
        capture = True
        while capture:
            self.get_snapshot()
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    self.camera.stop()
                    capture = False
                    # pygame.quit()
                if event.type == KEYDOWN:
                    # s for stop
                    if event.key == K_s:
                        picture = 'stop'
                        pygame.image.save(self.screen, "image_" + picture + ".jpg")
                    # p for play
                    if event.key == K_p:
                        picture = 'play'
                        pygame.image.save(self.screen, "image_" + picture + ".jpg")
                    # c for change
                    if event.key == K_c:
                        picture = 'change'
                        pygame.image.save(self.screen, "image_" + picture + ".jpg")


if __name__ == '__main__':
    camera = Capture()
    main_method = camera.main()
    # array = camera.array()


class Music_Player():

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.display = pygame.display.set_caption('Music Player')
        self.blue = (0, 0, 255)
        self.size = [640,480]
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def files(self):
        list_songs = ['1.mp3','2.mp3','3.mp3','4.mp3','5.mp3','6.mp3','7.mp3',
            '8.mp3']
        return list_songs

    def picksong(self):
        files = self.files()
        song = random.choice(files)
        print(song)
        return song

    def sound(self):
        sound = pygame.mixer.Sound(self.picksong())
        return sound


musicplayer = Music_Player()
sound = musicplayer.sound()
files = musicplayer.files()
def events(player, sound):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if os.path.isfile('image_play.jpg') == True:
                        sound.play()
                if event.key == pygame.K_s:
                    if os.path.isfile('image_stop.jpg') == True:
                        sound.stop()
                if event.key == pygame.K_c:
                    if os.path.isfile('image_change.jpg') == True:
                        sound.stop()
                        sound = musicplayer.sound()
                        sound.play()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        player.screen.fill(player.blue)
        pygame.display.update()

print('Press P - play sound')
print('Press S - stop playing instantly')
print('Press C - change song')
print('Press ESCAPE - close Music Player')
events(musicplayer,sound) # , array)
