import pygame
import random
from pygame.locals import *
import time
#import boardenter
pygame.init()
screen = pygame.display.set_mode((640,640))
pygame.display.set_caption('click as fast as possible')
blue=(0,0,255)
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
fps=pygame.time.Clock()
playerli=pygame.sprite.Group()
blocksli=pygame.sprite.Group()
bullli=pygame.sprite.Group()
start=time.time()
stt=0

"""ef makeg():
    global stt
    boardenter.board(stt)"""

class block(pygame.sprite.Sprite):
    def __init__ (self, color):
        super().__init__()
        self.image=pygame.Surface([10,15])
        self.image.fill(color)
        self.rect=self.image.get_rect()

class player(pygame.sprite.Sprite):
    def __init__ (self, color):
        super().__init__()
        self.image=pygame.Surface([10,15])
        self.image.fill(color)
        self.rect=self.image.get_rect()
    def update (self):
        pos=pygame.mouse.get_pos()
        self.rect.x=pos[0]

class Bullet(pygame.sprite.Sprite):
    def __init__ (self, color):
        super().__init__()
        self.image=pygame.Surface([10,15])
        self.image.fill(color)
        self.rect=self.image.get_rect()
    def updatee (self):
        self.rect.y-=5
        
def txt(msg,x,y,color):
    fontobj= pygame.font.SysFont("freesans", 32)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
    
def text(msg,x,y,color):
    fontobj= pygame.font.SysFont("freesans", 12)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def toppers(leaders):
    com=400
    for p in range (0,3):
        y=str(leaders[p][1])+", "+str(leaders[p][0])
        txt(y,230,int(com),red)
        com=int(com)+30
        
for i in range (30):
    bloc=block(blue)
    bloc.rect.x=random.randrange (630)
    bloc.rect.y=random.randrange (580)
    blocksli.add(bloc)
    playerli.add(bloc)

player=player(red)
playerli.add(player)
player.rect.y= 600

while True:
    end=time.time()
    duration=end-start

    
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            bullet=Bullet(black)
            bullet.rect.x=player.rect.x
            bullet.rect.y=player.rect.y
            bullli.add(bullet)
            playerli.add(bullet)
        

    for bullet in bullli:
        hit_list=pygame.sprite.spritecollide(bullet,blocksli,True)
        for block in hit_list:
            bullli.remove(bullet)
            playerli.remove(bullet)
            blocksli.remove(block)
        if bullet.rect.y<-10:
            bullli.remove(bullet)
            playerli.remove(bullet)

    for bullet in bullli:
        bullet.updatee()
            
    player.update()
    playerli.draw(screen)

    v=len(blocksli)
    if v == 0:
        screen.fill(black)
        txt("GAME OVER",230,320,red)
        txt("You are really rad",180,290,red)
        text(str(int(cd)),0,620,red)
        stt=cd
        pygame.display.update()
        print ('1')
        time.sleep(3)
        #if stt>=35:
        makeg()
        #toppers(leaders)
        pygame.display.update()
        break 
        
    cd=60-duration
    text(str(int(cd)),0,620,red)
    if int(cd) == 0:
        screen.fill(black)
        txt("GAME OVER",230,320,red)
        txt("You are pretty bad",180,290,red)
        text(str(int(cd)),0,620,red)
        pygame.display.update()
        time.sleep(10)
        break
    
    pygame.display.update()
    fps.tick(60)

            
