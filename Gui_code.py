import pygame
import sys
import math
pygame.init()
fps=30
fpsclock=pygame.time.Clock()
sur_obj=pygame.display.set_mode((800,800))
pygame.display.set_caption("Keyboard_Input")
White=(200,200,200)
p1=10
p2=10
step=1
t1 = 90
t2 = 90
font = pygame.font.Font('freesansbold.ttf', 22)
r = 400
r1 = 400


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


def drawGrid():
    blockSize = 10 #Set the size of the grid block
    for x in range(0, 800, blockSize):
        for y in range(0, 800, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(sur_obj, WHITE, rect, 1)

while True:
    sur_obj.fill((50,50,50))
    drawGrid()
    # rec = pygame.draw.rect(sur_obj, (255,0,0), (p1, p2, 70, 65))
    pygame.draw.circle(sur_obj,(255,0,255),[0,0],r,3)
    pygame.draw.line(sur_obj,(0,0,0),(0,0),(r*math.cos(t1*(math.pi/180)),r*math.sin(t1*(math.pi/180))),7)
    pygame.draw.circle(sur_obj,(255,0,0),[0,0],20)
    pygame.draw.line(sur_obj,(0,0,0),(r*math.cos(t1*(math.pi/180)),r*math.sin(t1*(math.pi/180))),(r*math.cos(t1*(math.pi/180))+r1*math.cos(t1*(math.pi/180)+t2*(math.pi/180)),r*math.sin(t1*(math.pi/180))+r1*math.sin(t1*(math.pi/180)+t2*(math.pi/180))),6)
    pygame.draw.circle(sur_obj,(0,255,0),[r*math.cos(t1*(math.pi/180)),r*math.sin(t1*(math.pi/180))],20)
    pygame.draw.circle(sur_obj,(255,255,255),[r*math.cos(t1*(math.pi/180))+r1*math.cos(t1*(math.pi/180)+t2*(math.pi/180)),r*math.sin(t1*(math.pi/180))+r1*math.sin(t1*(math.pi/180)+t2*(math.pi/180))],8)
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed() 
    if key_input[pygame.K_LEFT] and t1<90:
        t1 += step
    if key_input[pygame.K_RIGHT] and t1>0:
        t1 -= step
    if key_input[pygame.K_UP] and -180<t2:
        t2 -= step
    if key_input[pygame.K_DOWN] and t2<180:
        t2 += step

    theta1 = font.render(str("T1 = "+str(t1)), True, (0,0,0), (255,25,0))
    theta2 = font.render(str("T2 = "+str(t2)), True, (0,0,0), (255,25,0))
    x = font.render(str("x = "+str(int(r*math.cos(t1*(math.pi/180))+r1*math.cos(t1*(math.pi/180)+t2*(math.pi/180))))),True,(255,255,255),(0,0,0))
    y = font.render(str("y = "+str(int(r*math.sin(t1*(math.pi/180))+r1*math.sin(t1*(math.pi/180)+t2*(math.pi/180))))),True,(255,255,255),(0,0,0))
    sur_obj.blit(theta1, (600,20))
    sur_obj.blit(theta2, (600,50))
    sur_obj.blit(x, (600,90))
    sur_obj.blit(y, (600,110))
    pygame.display.update()
    fpsclock.tick(fps)
