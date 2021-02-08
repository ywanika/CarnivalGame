import pygame#import pygame into repl
import random
from pygame.locals import *
import time
from PIL import Image#allows to import images later
pygame.init()#intialize game
screen = pygame.display.set_mode((640,640))#set the screen dimentions
pygame.display.set_caption("pick a lucky duck!")#sets the caption to explains directions
blue=(0,0,255)#sets the color blue 
lightblue= (179, 213, 255)#sets a light blue color
black=(0,0,0) #sets the color black
red=(255,0,0) #sets the color red
white=(255,255,255) #sets the color white 
ducksli=pygame.sprite.Group()#creates the sprite on the game
fps=pygame.time.Clock()#creates a clock to use the start feature
start=time.time()#starts the game
stt=0#sets the starting time to 0

basewidth = 600#sets the screen size
img = Image.open('pool.png')#imports file image
wpercent = (basewidth / float(img.size[0]))#resets the width of the image based on screen width
hsize = int((float(img.size[1]) * float(wpercent)))#resets the height of the image based on screen height
img = img.resize((basewidth, hsize), Image.ANTIALIAS)#resizes it according to the above lines
img.save('resized_pool.png')#saves as a new resized image

basewidth = 100 #sets the base of a new image
img = Image.open('duck.png') #imports file image
wpercent = (basewidth / float(img.size[0])) #resets image width based on given size
hsize = int((float(img.size[1]) * float(wpercent)))#resets image height based on given size
img = img.resize((basewidth, hsize), Image.ANTIALIAS)#resizes accordingly
img.save('resized_duck.png')#saves as a new resized image

poolImg = pygame.image.load('resized_pool.png')#uploads the pool image
def pool():#creates the pool on the screen at the given coordinates
    screen.blit(poolImg, (50, 50))

def text_big(msg,x,y,color):#makes a text method that will later be used to show up text on screen
    fontobj= pygame.font.SysFont("freesans", 32)#sets the font to be freesans and size 32
    msgobj = fontobj.render(msg,False,color)#asks the caption to have a message and color
    screen.blit(msgobj,(x,y))#asks for the coordinates of the message
    time.sleep(2)#how long the message will delay for
    
def text_small(msg,x,y,color):#makes a smaller text method used later to show up text on the screen
    fontobj= pygame.font.SysFont("freesans", 12)#sets the font and size of the message to be freesans and 12
    msgobj = fontobj.render(msg,False,color)#asks for the message and color of the text
    screen.blit(msgobj,(x,y))#asks for coordinates of the text  
    time.sleep(2)#how long the message will delay for


class Duck(pygame.sprite.Sprite): #duck class
    def __init__ (self):#initializes
        super().__init__()#initializes
        self.image = pygame.image.load("resized_duck.png")#uploads new image
        self.rect = self.image.get_rect()
        self.isStar = False#intially sets isStar method to false
        #print (self.rect, self.rect.x)
    def setToStar (self):#defines set to star method
        self.isStar = True #makes the is Star method true
    def isStar (self):
        return self.isStar#return whether the duck is a star duck or not

for i in range(0,10,1):#creates 10 ducks
    duck=Duck()#uses the duck class to intiliaze
    duck.rect.x=random.randrange(100, 500, 3)#creates ducks and sets x coordinates in this range
    duck.rect.y=random.randrange(100, 500, 3)#creates ducks and sets y coordinates in this range
    ducksli.add(duck)#adds ducks to the list
ducks_list = ducksli.sprites()#creates a list of ducks sprites
#starDuck = random.randint(0, 10)
ducks_list[0].setToStar()#sets 3 of the ducks to be star ducks
ducks_list[1].setToStar()
ducks_list[2].setToStar()


while True:#runs the while true statement when game starts
    screen.fill(white)#sets the background color to white
    pool()#creates the resized pool
    end=time.time()#ends time
    duration=end-start#keeps track of duration

    for event in pygame.event.get():
        if event.type == QUIT:#if you quit, end game
            pygame.quit()
            exit()#exit when quit
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:#keep track of when clicked the mousebutton
            pos=pygame.mouse.get_pos()#get position of the mouse
            #print (pos)
            for x in ducks_list:#for loop to go through the ducks
                if x.rect.collidepoint(pos[0],pos[1]): #if the mouse is clicked on the duck
                    if (x.isStar):#if the duck is a star duck
                        screen.fill(white)#fill screen white
                        text_big("Congrats you got the lucky duck!",70,320,lightblue)#show the text that you won
                        pygame.display.update()#update
                        time.sleep(10)#end game by delaying
                        break#end
                    else: #if it is not a starduck
                      screen.fill(black)#make the screen black
                      text_big("Sorry:( you didn't get the lucky duck",70,320,red)#display text saying you lost
                      pygame.display.update()#update
                      time.sleep(10)#end game
                      break#end

                


    
    ducksli.draw(screen)#display ducks 
    pygame.display.update()#final update