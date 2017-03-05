class Music_Player():
    def __init__(self):
        file = "01.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        load(object)
        pygame.mixer.music.play(loops=0, start=0.0) # plays the loaded music stream
        while pygame.music.get_busy() == True:
            pygame.time.Clock.tick(framerate=0)
        pygame.mixer.music.rewind() # rewinds the music to the beginning
        pygame.mixer.music.pause() # pauses the music if it is playing
        pygame.mixer.music.unpause() # unpauses the music after it is paused
