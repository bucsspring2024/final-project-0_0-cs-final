import pygame
import random
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.model.crashed = True
                self.model.game_over = True
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.model.game_paused = True
                elif event.key == pygame.K_r:
                    self.model.game_paused = False
        if (self.model.crashed == False):
            keys = pygame.key.get_pressed()
            # Move the player Horizontally
            if keys[pygame.K_LEFT] and self.model.game_paused == False:
                self.model.car_x_coordinate -= 5
            if keys[pygame.K_RIGHT] and self.model.game_paused == False:
                self.model.car_x_coordinate += 5

    def update(self):
        
        self.view.scroll_y += self.view.scroll_speed

        # If the background scrolls off the screen, reset its position
        if self.view.scroll_y >= self.view.background_rect.height:
            self.view.scroll_y = 0
        

        self.model.enemy_car_starty += self.model.enemy_car_speed

        if self.model.enemy_car_starty > self.model.display_height:
            self.model.enemy_car_starty = 0 - self.model.enemy_car_height
            self.model.enemy_car_startx = random.randrange(310, 450)

        if self.model.car_y_coordinate < self.model.enemy_car_starty + self.model.enemy_car_height:
            if self.model.car_x_coordinate > self.model.enemy_car_startx and \
                    self.model.car_x_coordinate < self.model.enemy_car_startx + self.model.enemy_car_width or \
                    self.model.car_x_coordinate + self.model.car_width > self.model.enemy_car_startx and \
                    self.model.car_x_coordinate + self.model.car_width < self.model.enemy_car_startx + self.model.enemy_car_width:
                self.model.crashed = True

        if self.model.car_x_coordinate < 260 or self.model.car_x_coordinate > 490:
            self.model.crashed = True