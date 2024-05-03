import os
import pygame
import random
import src.button

class CarView:
    def __init__(self, model):
        pygame.init()
        self.model = model
        self.gameDisplay = pygame.display.set_mode((self.model.display_width, self.model.display_height))
        pygame.display.set_caption('Car Racing')
        self.clock = pygame.time.Clock()
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        
        # Use os.path.join for all file paths
        assets_folder = "Assets"  # Assuming 'Assets' is at the same level as 'src' directory
        self.carImg = pygame.image.load(os.path.join(assets_folder, "car.png"))
        enemy_car_index = random.randint(1, 2)
        self.enemy_car = pygame.image.load(os.path.join(assets_folder, f"enemy_car_{enemy_car_index}.png"))
        self.bgImg = pygame.image.load(os.path.join(assets_folder, "back_ground.jpg")).convert()
        self.background_rect = self.bgImg.get_rect()
        self.background_x = (800 - self.background_rect.width) // 2
        self.scroll_speed = 3
        self.scroll_y = 0
        self.font = pygame.font.SysFont("arialblack", 40)
        self.TEXT_COL = (255, 255, 255)

        # Loading buttons with dynamic paths
        self.start_img = pygame.image.load(os.path.join(assets_folder, "StartButton.png")).convert_alpha()
        self.pause_img = pygame.image.load(os.path.join(assets_folder, "PauseButton.png")).convert_alpha()
        self.resume_img = pygame.image.load(os.path.join(assets_folder, "ResumeButton.png")).convert_alpha()
        self.restart_img = pygame.image.load(os.path.join(assets_folder, "RestartButton.png")).convert_alpha()
        self.exit_img = pygame.image.load(os.path.join(assets_folder, "ExitButton.png")).convert_alpha()

        # Buttons
        self.start_button = src.button.Button(255, 150, self.start_img, 0.8)
        self.pause_button = src.button.Button(230, 25, self.pause_img, 0.5)
        self.resume_button = src.button.Button(290, 150, self.resume_img, 0.6)
        self.restart_button = src.button.Button(278, 250, self.restart_img, 0.7)
        self.restart_button2 = src.button.Button(278, 250, self.restart_img, 0.7)
        self.exit_button = src.button.Button(250, 340, self.exit_img, 0.9)

    def render(self):
        if (self.model.game_paused == False):
            
            self.gameDisplay.fill(self.black)
            self.gameDisplay.blit(self.bgImg, (self.background_x, self.scroll_y - self.background_rect.height))
            self.gameDisplay.blit(self.bgImg, (self.background_x, self.scroll_y))

            self.gameDisplay.blit(self.carImg, (self.model.car_x_coordinate, self.model.car_y_coordinate))
            self.gameDisplay.blit(self.enemy_car, (self.model.enemy_car_startx, self.model.enemy_car_starty))
            self.highscore()
        else:
            self.gameDisplay.fill(self.black)
            if self.resume_button.draw(self.gameDisplay):
                if (self.model.game_paused == True):
                    self.model.game_paused = False
            if self.restart_button.draw(self.gameDisplay):
                self.model.__init__()
                self.model.start_check = False
                self.scroll_speed = 3
            if self.exit_button.draw(self.gameDisplay):
                self.model.crashed = True
                self.model.game_over = True
        if self.pause_button.draw(self.gameDisplay) and self.model.game_paused == False:
            self.model.game_paused = True
            
        pygame.display.update()
        self.clock.tick(60)

    def render_fail_panel(self, msg):      
        self.gameDisplay.fill(self.black)
        if self.restart_button2.draw(self.gameDisplay):
            self.model.__init__()
            self.model.start_check = False
            self.scroll_speed = 3
            self.model.crashed = False
        if self.exit_button.draw(self.gameDisplay):
            self.model.crashed = True
            self.model.game_over = True
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 200 - text.get_height() // 2))
        self.display_credit()
        pygame.display.update()
        self.clock.tick(60)
    
    def render_start_panel(self):
        self.gameDisplay.fill(self.black)      
        if self.start_button.draw(self.gameDisplay):
            self.model.start_check = False
        pygame.display.update()
        self.clock.tick(60)

    def highscore(self):
        font = pygame.font.SysFont("arial", 40)
        text = font.render("Score : " + str(self.model.count), True, self.white)
        self.gameDisplay.blit(text, (30, 220))

    def display_credit(self):
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("Thanks for playing!", True, self.white)
        self.gameDisplay.blit(text, (600, 520))
    
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.gameDisplay.blit(img, (x, y))