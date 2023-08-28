import pygame
import sys
from pyvidplayer2 import Video
import random

# Initialize Pygame
pygame.init()



# Set up display
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ocean Guardian")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Game loop
clock = pygame.time.Clock()
running = True




class Player:
    def __init__(self):
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        
    def draw(self):
        WIN.blit(self.image,(self.rect.x,self.rect.y))





class Rubbish:
    def __init__(self):
        
        
        # cloud
        # creating rubbish cloud str var
        self.bg = pygame.image.load("frame1.png")
        self.rect = self.bg.get_rect()
        self.height = self.bg.get_height()
        
        
        
        
        
        # creating current rubbish cloud int var
        self.rubbish_count = 1
        
    
        # randomize rubbish
        choices = ["g1","g2","g3","g4","g5","g6"]
        
        
        self.layer1 = pygame.image.load("oceanlayer.png")
        self.layer2 = pygame.image.load("oceanlayer.png")
        self.layer3 = pygame.image.load("oceanlayer.png")
        
        
        # x and y
        self.x, self.y = WIDTH - (WIDTH + 50),random.randint(0,HEIGHT - self.height)
        
        
    
    # increment and draw rubbish cloud
    def rub_handler(self):
        
        # increment
        self.rubbish_count += 1
        
        # load the bg file
        if self.rubbish_count == 1:
            self.bg == pygame.image.load("frame1.png")
        elif self.rubbish_count == 2:
            self.bg == pygame.image.load("frame2.png")
        elif self.rubbish_count == 3:
            self.bg = pygame.image.load("frame3.png")
        elif self.rubbish_count == 4:
            self.bg == pygame.image.load("frame4.png")
            self.rubbish_count == 1
        else:
            self.bg == pygame.image.load("frame1.png")
            self.rubbish_count == 1
    
    
    # main
    def draw(self):
        WIN.blit(self.bg,(self.x,self.y))
        self.bg.x += 1
        self.bg.y += random.randint(0,5)
    




# Creating an instance
rubbish = Rubbish()

# creating an instance
player = Player()



class Game:
    def __init__(self):
        self.screen = "intro" 
        self.oceanbg = pygame.image.load("ocean.png")
    
    
    
    def intro(self):
        self.screen = "ocean"
        print(self.screen)
        
        
    def result(self):
        pass
        
        
        
        
        
    # main game method
    def ocean(self):
        # vars
        keys = pygame.key.get_pressed()
        self.vel = 5
        
        
        
        def net_handler():
            print("clicked space")
        
        
        
        win = False
        while win == False:
            
            # controls
            if keys[pygame.K_a]:
                player.rect.x -= self.vel
                print("d")
            if keys[pygame.K_d]:
                player.rect.x += self.vel
                print("d")
            if keys[pygame.K_w]:
                player.rect.y -= self.vel
                print("w")
            if keys[pygame.K_s]:
                player.rect.y += self.vel
                print("s")
            if keys[pygame.K_SPACE]:
                net_handler()
            else:
                print("testrin")
            
            
            print("npne")
            
            
            # draw 
            rubbish.draw()
            player.draw()
            
            
            
            pygame.display.flip()
            clock.tick(60)
            
            
            print("displayed")
    
    
    def draw(self):
        if self.screen == "intro":
            self.intro()
        
        if self.screen == "ocean":
            self.ocean()
        
        if self.screen == "result":
            self.result()
















game = Game()





# main file
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    
    
    
    # Clear the screen
    WIN.fill(black)
    
    
    
    
    
    
    # Cap the frame rate
    clock.tick(60)
    game.draw()
    print(game.screen)
    
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()