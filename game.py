import pygame
import sys
import random

pygame.font.init()
final_state = "lose"




white = (255, 255, 255)
black = (0,0,0)

class screen():
    def __init__(self):
        self.width = 1440   
        self.height = 810
        self.screen = pygame.display.set_mode((self.width, self.height))

# init screen
WIN = screen()











# archived animation

"""# bg anim
class background:
    def __init__(self):
        
        
        self.total_frames = 64
        
        self.bg_frames = [pygame.image.load(f"bg/ocean{i}.png") for i in range(1, self.total_frames + 1)]
        
        self.bg_frame_index = 0
        self.bg_frame_delay = 200  # Delay between frame changes (in milliseconds)
        self.last_frame_change = pygame.time.get_ticks()
        
        self.bg_resized = pygame.transform.scale(self.bg_frames[self.bg_frame_index], (WIN.width, WIN.height))
        
    def draw(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_change >= self.bg_frame_delay:
            self.last_frame_change = current_time
            
            self.bg_frame_index = (self.bg_frame_index + 1) % len(self.bg_frames)
            self.bg_resized = pygame.transform.scale(self.bg_frames[self.bg_frame_index], (WIN.width, WIN.height))
        
        WIN.screen.blit(self.bg_resized, (0, 0))

bg = background()"""










class background:
    def __init__(self):
        self.image = pygame.image.load("newocean.png")
        self.bg_resized = self.bg_resized = pygame.transform.scale(self.image, (WIN.width, WIN.height))
    def draw(self):
        WIN.screen.blit(self.bg_resized, (0, 0))

bg = background()


# proportion percentage
valuex, valuey = bg.bg_resized.get_width() - bg.image.get_width(), bg.bg_resized.get_height() - bg.image.get_width()
percentagex, percentagey =  bg.image.get_width() / bg.bg_resized.get_width(), bg.image.get_height() / bg.bg_resized.get_height()



class Player():
    def __init__(self):
        
        # Load the image
        self.original_image = pygame.image.load("ship.png").convert_alpha()
        
        
        
        
        
        # Scale the image
        scaled_image = pygame.transform.scale(self.original_image, (self.original_image.get_width() * (4 + percentagex), self.original_image.get_width() * (4 + percentagey) ))
        
        # Rotated image
        self.rotated_image = pygame.transform.rotate(scaled_image, 90)
        
        # new image
        self.image = self.rotated_image
        
        
        self.image.set_colorkey((0,0,0))
        
        
        # height and width
        self.rect = self.image.get_rect()
        
        # initial pos
        self.x =  (WIN.width // 2) + ((WIN.width // 2) // 2 )
        self.y = WIN.height // 2
        
        # vel
        self.vel = 7
        self.back_vel = self.vel - 1
        self.front_vel = self.vel + 1
        
        # score
        self.score = 0
        
        
        
        
        
        
        
    def draw(self):
        WIN.screen.blit(self.image,(self.x,self.y))

# init player
player = Player()
player_rect = player.rect





class Rubbish():
    def __init__(self):
        
        
        
        
        # Load the image
        original_image = pygame.image.load(f"rubbish/rubbish{random.randint(1,3)}.png").convert_alpha()
        
        # Scale the image
        self.scaled_image = pygame.transform.scale(original_image, (316, 308))
        
        # Rotated image
        self.rotated_image = pygame.transform.rotate(self.scaled_image, 0)
        
        # new image
        self.image = self.rotated_image
        
        
        self.image.set_colorkey((255,255,255))
        
        
        # height and width
        self.rect = self.image.get_rect()
        
        # initial pos
        self.x =  0
        self.y = random.randint(0, WIN.height - self.rect.height)
        
        #vel
        self.vel = 10
        
        
        # state moving
        self.exist = True
        
        
        
        
        
    def update(self):
        self.x += self.vel
    def draw(self):
        WIN.screen.blit(self.image, (self.x, self.y))


# init rubbish
rubbish = Rubbish()






class Menu:
    def __init__(self):
        self.return_mode = ""
        
        # button atts
        
        
        self.button_image = pygame.image.load("continue.png").convert_alpha()
        self.button_image.set_colorkey(black)
        
        
        
        self.widthimageproportional = self.button_image.get_width() * (4 + percentagex)
        self.heightimageproportional = self.button_image.get_height() * (4 + percentagey)
        
        self.button_rect = pygame.Rect(WIN.width//2 - 100, WIN.height//2 - 50, self.widthimageproportional, self.heightimageproportional)
        self.newbutton = pygame.transform.scale(self.button_image, (self.widthimageproportional, self.heightimageproportional))
        
        
        
    def draw_main_menu(self,bg):
        
        self.image = pygame.image.load(bg)
        # bg
        self.bg_resized = self.bg_resized = pygame.transform.scale(self.image, (WIN.width, WIN.height))
        WIN.screen.blit(self.bg_resized, (0, 0))
        
        
        
        # button display
        WIN.screen.blit(self.newbutton, self.button_rect)
        print(self.newbutton.get_width(), self.newbutton.get_height())
        
        
        
        
        pygame.display.flip()
        
        
        
        
        
        
        # logo
        
        
        
    def clicked(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu.button_rect.collidepoint(event.pos):
                        print("Button clicked!")
                        # Handle the button click action here
                        self.return_mode = "mode_selection"
            pygame.display.flip()
            
            
            
            
            
    def clicked_mode_selection(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        print("Button clicked!")
                        # Handle the button click action here
                        self.return_mode = "ocean"
            pygame.display.flip()










# init menu
menu = Menu()

# init mode selection
mode_selection = Menu()










width = WIN.width
height = WIN.height


start_time = pygame.time.get_ticks()


class Intro:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.input = "Created by frankie, manling and Chien"
    # draw
    def draw(self):
        
        
        # draw bg
        WIN.screen.fill(black)
        
        pygame.time.delay(3000)
        
        
        # draw text
        self.text = self.font.render(self.input, False, white)
        self.text_width = self.text.get_width()
        self.text_height = self.text.get_height()
        
        WIN.screen.blit(self.text, (width // 2 - (self.text_width // 2), height // 2))
        
        pygame.display.flip()
        
        pygame.time.delay(3000)
        
        


intro = Intro()





class ocean_game():
    def __init__(self):
        self.goal_time = 0
        self.rubbish_list = []  # List to hold Rubbish objects
        self.win = False
    def start_game(self):
        self.goal_time = pygame.time.get_ticks() + 5000  # Set initial goal time
        
    def check_collision(self):
        player_rect = player.rect  # Get player's rectangle
        for rubbish_obj in self.rubbish_list:
            if rubbish_obj.rect.colliderect(player_rect):
                return True
        return False
        
        
        
    def draw(self):
        
        # emd state
        end = False
        
        # additional vars
        
        
        
        
        while not self.win:
            while not end:
                
                
                # initialize the bg
                bg.draw()
                
                
                # event tracking
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit
                        sys.exit
                        end = True
                
                
                
                
                
                
                keys = pygame.key.get_pressed()
                
                # keys handling
                if keys[pygame.K_a]:
                    player.x -= player.front_vel
                if keys[pygame.K_d]:
                    player.x += player.back_vel
                if keys[pygame.K_w]:
                    player.y -= player.vel
                if keys[pygame.K_s]:
                    player.y += player.vel
                
                
                
                
                
                if self.goal_time == 0:
                    self.start_game()

                # Create a new Rubbish object if goal time is reached
                if pygame.time.get_ticks() > self.goal_time:
                    new_rubbish = Rubbish()
                    self.rubbish_list.append(new_rubbish)
                    self.goal_time = pygame.time.get_ticks() + 5000  # Update goal time

                # Move and draw existing Rubbish objects
                for rubbish_obj in self.rubbish_list:
                    rubbish_obj.update()
                    rubbish_obj.draw()
                
                # Check for collision
                if self.check_collision():
                    end = True  # End the game if collision occurs
                    self.win = True
                
                
                
                
                    
                player.draw()
                
                
                print(pygame.time.get_ticks(), "ideal goal:", self.goal_time)
                # update display
                pygame.display.flip()
                pygame.time.Clock().tick(60)
                





# init ocean game
ocean = ocean_game()






# win or lose methods
def lose():
    pass
    
    
    
    
    
    
def win():
    pass






class Game():
    def __init__(self):
        self.state = "intro"
        self.game_initialized = False
        
        
        
        
        
    def play_game(self):
        if self.state == "intro":
            intro.draw()
            self.state = "menu"
            print(self.state)
            Game.play_game(self)
        elif self.state == "menu":
            while self.state == "menu":
                menu.draw_main_menu("newocean.png")
                menu.clicked()
                if menu.return_mode == "mode_selection":
                    self.state = "mode_selection"
            Game.play_game(self)
        elif self.state == "mode_selection":
            
            while self.state == "mode_selection":
                # changing attr
                
                # changing attr: pos
                
                # creating var: center of bottom portion of the left side
                
                xmiddle = WIN.width // 2
                left_middle = xmiddle // 2
                
                ymiddle = WIN.height // 2
                middle_half = ymiddle // 2
                bottom_portion_middle = middle_half + ymiddle
                
                
                
                
                mode_selection.button_rect = pygame.Rect(left_middle - (mode_selection.newbutton.get_width() - 50), bottom_portion_middle, mode_selection.widthimageproportional, mode_selection.heightimageproportional)
                mode_selection.draw_main_menu("mode_selection.png")
                
                
                pygame.display.flip()
                
                # custom one
                mode_selection.clicked_mode_selection()
                
                if mode_selection.return_mode == "ocean":
                    self.state = "ocean"
            Game.play_game(self)
        elif self.state == "ocean":
            while self.state == "ocean":
                while not ocean.win:
                    if not self.game_initialized:
                        ocean.start_game()  # Start the game
                        self.game_initialized = True
                    ocean.draw()
                    self.state = "lose"
                self.state = "win"
            Game.play_game(self)
            
            
            
            
        elif self.state == "lose":
            lose()
            Game.play_game(self)
        elif self.state == "win":
            win()
            Game.play_game(self)


# inti game
game = Game()








# call for main game
game.play_game()
pygame.display.flip()






# Quit Pygame
pygame.quit()
sys.exit()