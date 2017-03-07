import numpy
import pylab
import pygame
import pygame.camera
from pygame.locals import *

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
        # self.sub = pygame.subsurface(0, 0, 50, 50)


    def get_snapshot(self):
        self.screen = self.camera.get_image(self.screen)
        self.display.blit(self.screen, (0, 0))
        pygame.display.flip()

    """def calibrate(self):
        background = []
        for i in range(0, 5):
            background.append(self.camera.get_image(self.background))
        pygame.transform.average_surfaces(background, self.background)
        # blit to display surface
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()"""
    """def array(self):
        array = pygame.surfarray.array2d(self.display.fill(self.ccolor, (0, 0, 50, 50)))
        print(array)"""

    def array(self):
        filenames = ['image_fastforward.jpg', 'image_play.jpg', 'image_restart.jpg',
                     'image_stop.jpg']
        count = 1
        for filename in filenames:
            image = pygame.image.load(filename)
            array = pygame.surfarray.pixels_red(image)
            #luminosity filter
            #avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
            #arr = numpy.array([[[avg,avg,avg] for avg in col] for col in avgs])
            print(array, str(count))
            count += 1
        return

    """def average(self):
        filenames = ['image_fastforward.jpg', 'image_play.jpg', 'image_restart.jpg',
                     'image_stop.jpg']
        count = 1
        for filename in filenames:
            image = pygame.image.load(filename)
            # make a red rectangle on the screen
            #crect = pygame.draw.rect(self.display, (255, 0, 0), (145,105,30,30), 4)
            # get average color of area inside the rectangle
            #self.ccolor = pygame.transform.average_color(self.screen, crect)
            # fill upper left corner with that color
            # self.display.fill(self.ccolor, (0, 0, 50, 50))
            # sub = self.subsurface(crect)
            #self.display.blit(self.screen, (0,0))
            pygame.image.save(image,'' + str(count) + '.jpg')
            count += 1
            #pygame.transform.threshold(self.screen, self.screen,
                          # self.ccolor(30, 30, 30), self.threshold, 2)
            pygame.display.flip()"""

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
    # average = camera.average()
    array = camera.array()
