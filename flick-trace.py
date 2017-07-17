import pygame
import time
import signal
import flicklib

@flicklib.move()
def move(x, y, z):
    global xyztxt
    global xyz
    xyztxt = '{:5.3f} {:5.3f} {:5.3f}'.format(x,y,z)
    xyz=(x, y, z)
    print("XYZ: "+xyztxt)

pygame.init()

gameDisplay = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Flick Demo')
a = 1

def disp(x,y):
    gameDisplay.blit(Img, (x,y))
gameDisplay.fill((0,0,0))
global xyztxt
xyztxt = ''
global xyz
xyz = (0, 0, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.set_at((int(xyz[0]*1000), (1000-(int(xyz[1]*1000)))), (255,255,255))
    pygame.display.update()
    time.sleep(0.05)

pygame.quit()
quit()
