import numpy
import pygame
import pygame.camera
from pygame.locals import *
import os, sys
import time

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


    def array(self):
        filenames = ['image_fastforward.jpg', 'image_play.jpg', 'image_restart.jpg',
                     'image_stop.jpg']
        count = 1
        for filename in filenames:
            image = pygame.image.load(filename)
            array = pygame.surfarray.pixels_red(image)
            print(array, str(count))
            count += 1
        return array


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
                    # f for fast forward
                    if event.key == K_f:
                        picture = 'fastforward'
                        pygame.image.save(self.screen, "image_" + picture + ".jpg")
                    # r for restart
                    if event.key == K_r:
                        picture = 'restart'
                        pygame.image.save(self.screen, "image_" + picture + ".jpg")

if __name__ == '__main__':
    camera = Capture()
    main_method = camera.main()
    array = camera.array()

class Music_Player():

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.display = pygame.display.set_caption('Music Player')
        self.blue = (0, 0, 255)
        self.size = [640,480]
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def filesfolder(self):
        files = []
        path = '/home/anikapayano/InteractiveProgramming'
        directory = os.listdir(path)
        for filename in directory:
            if filename.endswith(".wav"):
                files.append(filename)
        files.sort()
        return files

    def picksong(self):
        song = '09.wav'
        return song

    def sound(self):
        sound = pygame.mixer.Sound(self.picksong())
        return sound

    def playsound(self):
        """Play sound through default mixer channel in blocking manner.
        This will load the whole sound into memory before playback.
        """
        song = self.sound()
        song.play()

    def stopsound(self):
        song = self.sound()
        song.stop()


musicplayer = Music_Player()
sound = musicplayer.sound()

def events(player, sound):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    sound.play()
                    display.blit()
                if event.key == pygame.K_s:
                    sound.stop()
        player.screen.fill(player.blue)
        pygame.display.update()


musicplayer = Music_Player()
files = musicplayer.filesfolder()

print('press p - play sound')
print('press s - stop playing instantly')
events(musicplayer,sound)
