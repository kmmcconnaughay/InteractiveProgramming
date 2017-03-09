import pygame
import multiprocessing
import os
import sys
import random
import threading
import time

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

        #files = self.filesfolder()
        #songnum = random.randint(0, 14)
        #song = files[songnum]
        #print(song)
        #return song

    def sound(self):
        sound = pygame.mixer.Sound(self.picksong())
        return sound

    def playsound(self):
        """Play sound through default mixer channel in blocking manner.
        This will load the whole sound into memory before playback.
        """
        song = self.sound()
        song.play()
        #while pygame.mixer.get_busy():
        #    print ("Playing...")
        #    clock.tick(1000)

    def stopsound(self):
        song = self.sound()
        song.stop()

    #def playnext(self):
    #    i = self.files.index(self.song)
    #    pygame.mixer.Sound(self.files[i + 1])
    #    clock = pygame.time.Clock()
    #    sound.play()
    #    while pygame.mixer.get_busy():
    #        print ("Playing...")
    #        clock.tick(1000)

    #def playprevious(self):
    #    pygame.mixer.Sound(files[self.i - 1])
    #    clock = pygame.time.Clock()
    #    sound.play()
    #    while pygame.mixer.get_busy():
    #        print ("Playing...")
    #        clock.tick(1000)

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


#    def getmixerargs(self):
#        pygame.mixer.init()
#        freq, size, chan = pygame.mixer.get_init()
#        return freq, size, chan


#    def initMixer(self):
#        BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
#        FREQ, SIZE, CHAN = getmixerargs()
#        pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)


musicplayer = Music_Player()
files = musicplayer.filesfolder()
#print(files)
#playWAV = musicplayer.playsound()

print('press p - play sound')
print('press s - stop playing instantly')
events(musicplayer,sound)

# if __name__ == '__main__':


#    t = threading.Thread(name='daemon', target= musicplayer.events)
#    d = threading.Thread(name= 'non-daemon', target= musicplayer.playsound)
#    t.setDaemon(True)
#    d.start()
#    t.start()

#if __name__ == "__main__":
#    p1 = multiprocessing.Process(target= musicplayer.playsound, args())

#playWAV = musicplayer.playsound(input('WAV File:'))
#playsong = musicplayer.playsound()
