#import dependencies
import pygame
import random
from pygame.locals import *
import time

#set up the pygame screen
pygame.init()
screen = pygame.display.set_mode((640,640))
pygame.display.set_caption('click to pop the balloons')

#save some colors for use later
blue=(0,0,255)
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)

#groups of sprites
playerli=pygame.sprite.Group() # group of all sprites
blocksli=pygame.sprite.Group()
bullli=pygame.sprite.Group()

fps=pygame.time.Clock()#create an object to track frames per second
start=time.time() #gets current time

#creating classes for objects in game
class block(pygame.sprite.Sprite): #class for balloons
    def __init__ (self): #constructor
        super().__init__() #call parent class constructor
        self.image = pygame.image.load("balloon.png") #load image 
        #Fetch the rectangle object and set it to the image of itself
        self.rect=self.image.get_rect() 

class player(pygame.sprite.Sprite): #class for ben
    def __init__ (self): #constructor
        super().__init__() #call parent class constructor
        self.image = pygame.image.load("ben_copy.png") #load image
        #Fetch the rectangle object and set it to the image of itself
        self.rect=self.image.get_rect()
    def update (self): #make x-pos of object match the x-pos of the mouse
        pos=pygame.mouse.get_pos() #get the x&y pos of the mouse
        self.rect.x=pos[0] #set the x-pos of ben to the x-pos of the mouse

class Bullet(pygame.sprite.Sprite): #class for the bullet
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("dart.png")
        self.rect=self.image.get_rect()
    def update (self): #method to make the bullet move up
        self.rect.y-=5 #reduce y-pos by 5 each call

#function to put text on the screen given the text, coordinates, and size
def text(msg,x,y, size): 
    fontobj= pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(x,y))

#creates 10 random blocks in random places
for i in range (10): #runs 10 times
    bloc=block() #creates block
    #sets block to random location
    bloc.rect.x=random.randrange (630)
    bloc.rect.y=random.randrange (530)
    #adds block to the block list and all sprite list
    blocksli.add(bloc)
    playerli.add(bloc)

player=player() #creates 1 player
playerli.add(player) #adds player to all sprite list
player.rect.y= 590 #sets y-pos of player

while True: #runs loop until the loop is broken
    end=time.time() #get current time
    duration=end-start #find how much time has passed
    cd=15-duration #set the countdown to 15 minus the time passed
    
    screen.fill(white) #clear the screen
    #gets all the events stored in the event queue
    #runs a loop through the queue of all the Events
    for event in pygame.event.get(): 
        if event.type == QUIT: #if the person quits the widow
            pygame.quit() #quit pygame
            exit()
        #if the person left-clicks
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            bullet=Bullet() #creat a bullet
            #set the x & y to the coordiantes of the player sprite
            bullet.rect.x=player.rect.x 
            bullet.rect.y=player.rect.y
            #adds block to the block list and all sprite list
            bullli.add(bullet)
            playerli.add(bullet)

    #run a for loop through all the bullets that exist
    for bullet in bullli: 
        #get a list of all the balloons that are touching a bullet
        hit_list=pygame.sprite.spritecollide(bullet,blocksli,True)
        #loop through all the balloons that have been "hit"
        for block in hit_list: 
            #remove the blocks and bulltes from the lists
            bullli.remove(bullet)
            playerli.remove(bullet)
            blocksli.remove(block)
            playerli.remove(block)
        if bullet.rect.y<-10: #if the dart is off the screen...
            #...remove it from the lists
            bullli.remove(bullet)
            playerli.remove(bullet)

    for bullet in bullli: #loop through the remianing darts
        bullet.update() #update their location
            
    
    player.update() #update the player's location
    playerli.draw(screen) #draws objects on the screen

    v=len(blocksli) #gets the number of balloons
    if v == 0: #if there are no balloons
        screen.fill(black) #fill the screen with black
        text("GAME OVER",230,320,32) #add text
        text("you win",230,360,32)
        text(str(int(cd)),0,620,12) #show the countdown timer
        pygame.display.update() #show the screen
        time.sleep(20) #show the window for 20 seconds
        break #leave the while loop

     
    text(str(int(cd)),0,620,12) #show the countdown
    if int(cd) == 0: #if the countdown has ended
        screen.fill(black) #fill the screen with black
        text("GAME OVER",230,320,32) #add text
        text("you lose",230,360,32)
        text(str(int(cd)),0,620,12) #show the countdown timer
        pygame.display.update() #show the screen
        time.sleep(20) #show the window for 20 seconds
        break #leave the while loop
    
    pygame.display.update() #show the screen
    fps.tick(60) #set to 60 frames per second
pygame.quit() #quit pygame