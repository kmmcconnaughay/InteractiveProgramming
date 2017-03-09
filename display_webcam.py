import numpy
import pylab
import pygame
import pygame.camera
from pygame.locals import *

DEVICE = '/dev/video0'
SIZE = (640, 480)


def camstream():
    pygame.init()
    pygame.camera.init()
    display = pygame.display.set_mode(SIZE, 0)
    camera = pygame.camera.Camera(DEVICE, SIZE)
    camera.start()
    screen = pygame.surface.Surface(SIZE, 0, display)
    capture = True
    while capture:
        screen = camera.get_image(screen)
        display.blit(screen, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                capture = False
                camera.stop()
                pygame.quit()
            if event.type == KEYDOWN:
                # s for stops
                if event.key == K_s:
                    picture = 'stop'
                    pygame.image.save(screen, "image_" + picture + ".jpg")
                # p for play
                if event.key == K_p:
                    picture = 'play'
                    pygame.image.save(screen, "image_" + picture + ".jpg")
                # f for fast forward
                if event.key == K_f:
                    picture = 'fastforward'
                    pygame.image.save(screen, "image_" + picture + ".jpg")
                # r for restart
                if event.key == K_r:
                    picture = 'restart'
                    pygame.image.save(screen, "image_" + picture + ".jpg")
    return

def grayscale():
    filenames = ['image_fastforward.jpg', 'image_play.jpg', 'image_restart.jpg',
                 'image_stop.jpg']
    for filename in filenames:
        image = pygame.image.load(filename)
        arr = pygame.surfarray.array3d(image)
        #luminosity filter
        avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
        arr = numpy.array([[[avg,avg,avg] for avg in col] for col in avgs])
        print(arr)
    return pygame.surfarray.make_surface(arr)

if __name__ == '__main__':
    camstream()
    grayscale()
