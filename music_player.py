import pygame
import multiprocessing
import os
import sys
import random
import threading
from queue import Queue
import time

class Music_Player():

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def exampleJob(worker):
        time.sleep(0.5)

    def threader(self):
        while True:
            worker = q.get()
            self.exampleJob(worker)
            q.task_done()

    def threading(self):
        lock = threading.Lock() #locks thread if variables are used between threads
        q = Queue()
        for x in range(2): #how many threads I want
            t = threading.Thread(target = threader)
            t.daemon = True
            t.start()

        start = time.time()
        for worker in range(20):
            q.put(worker)

        q.join

        print('Entire job took:', time.time()-start)


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
        files = self.filesfolder()
        songnum = random.randint(0, 14)
        song = files[songnum]
        print(song)
        return song

    def playsound(self):
        """Play sound through default mixer channel in blocking manner.
        This will load the whole sound into memory before playback.
        """
        sound = pygame.mixer.Sound(self.picksong())
        clock = pygame.time.Clock()
        sound.play()
        while pygame.mixer.get_busy():
            #print ("Playing...")
            clock.tick(1000)

    def stopsound(self):
        self.playsound.stop()

    def playnext(self):
        i = self.files.index(self.song)
        pygame.mixer.Sound(self.files[i + 1])
        clock = pygame.time.Clock()
        sound.play()
        while pygame.mixer.get_busy():
            print ("Playing...")
            clock.tick(1000)

    def playprevious(self):
        pygame.mixer.Sound(files[self.i - 1])
        clock = pygame.time.Clock()
        sound.play()
        while pygame.mixer.get_busy():
            print ("Playing...")
            clock.tick(1000)

    def events(self):
        playing = True
        while playing:
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        self.stopsound()
                        playing = False


    def getmixerargs(self):
        pygame.mixer.init()
        freq, size, chan = pygame.mixer.get_init()
        return freq, size, chan


    def initMixer(self):
        BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
        FREQ, SIZE, CHAN = getmixerargs()
        pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)


musicplayer = Music_Player()
files = musicplayer.filesfolder()
#print(files)
playWAV = musicplayer.playsound()


#if __name__ == "__main__":
#    p1 = multiprocessing.Process(target= musicplayer.playsound, args())

#playWAV = musicplayer.playsound(input('WAV File:'))
#playsong = musicplayer.playsound()
