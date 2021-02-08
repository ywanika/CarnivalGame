#import dependencies 
import pygame
import random
from pygame.locals import *
from PIL import Image
import time
#set up the pygame screen
pygame.init()
screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("click on the button as fast as you can!")
#save some colors for use later
blue=(0,0,255)
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
#sets hammer count to 0 in the beginning of game
count = 0 
#groups of sprites 
fps=pygame.time.Clock()
spritesli=pygame.sprite.Group()
buttonli=pygame.sprite.Group()
start=time.time()
stt=0

#sets up the font and color of the text that will be displayed on the screen
def text_big(msg,x,y,color):
    fontobj= pygame.font.SysFont("freesans", 32)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

#imports the image of the button and resizes it
basewidth = 400
img = Image.open('button1.png')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('resized_button.png')

#imports the image of the hammer and resizes it
basewidth = 100
img = Image.open('hammer1.png')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('resized_hammer.png')

#turns the hammer image into an object
class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("resized_hammer.png")
        self.rect=self.image.get_rect()
    #allows the hammer to follow the mouse
    def update (self):
        pos=pygame.mouse.get_pos()
        self.rect.x=pos[0] - 30
        self.rect.y=pos[1] - 30
       
#turns the button image into an object
class Button(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("resized_button.png")
        self.rect=self.image.get_rect()

#adds the button sprite
button=Button()
button.rect.x= 280
button.rect.y= 280
spritesli.add(button)

#adds the player sprite
player=Player()
spritesli.add(player)

#while the game is still running
while True:
    end=time.time()
    duration=end-start
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #whenever you click on the button, the click count goes up by 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            pos=pygame.mouse.get_pos()
            if button.rect.collidepoint(pos[0],pos[1]):
                count+=1
    #displays the text for click count; sets text, location, and color
    text_big("Click Count:"+str(count),350,200,blue)

    #creates a timer on the left bottom corner of the screen
    cd=10-duration
    text_big(str(int(cd)),20,500,red)
    #if the count click is greater than or equal to 40, the user wins
    if count >= 40:
      #if the user wins, the screen will turn black and "YOU WIN" will show up on the screen in red
      screen.fill(black)
      text_big("YOU WIN",250,320,red)
      text_big(str(int(cd)),20,600,red)
      pygame.display.update()
      time.sleep(10)
      #game ends
      break
    #if the time runs out before the user gets a click count of 40, they will lose the game
    elif int(cd) == 0:
        #if they lose, the screen will turn black and "YOU LOSE" will show up on the screen
        screen.fill(black)
        text_big("YOU LOSE",250,320,red)
        text_big(str(int(cd)),20,600,red)
        pygame.display.update()
        time.sleep(10)
        #game ends
        break

    player.update()
    spritesli.draw(screen)
    pygame.display.update()