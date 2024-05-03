import random

class Model:
    def __init__(self):
        self.display_width = 800
        self.display_height = 600
        
        self.car_width = 49
        self.car_x_coordinate = (self.display_width * 0.45)
        self.car_y_coordinate = (self.display_height * 0.8)

        self.enemy_car_width = 49
        self.enemy_car_height = 100
        self.enemy_car_startx = random.randrange(310, 450)
        self.enemy_car_starty = -600
        self.enemy_car_speed = 5

        self.count = 0
        self.crashed = False
        self.game_paused = False
        self.game_over = False
        self.start_check = True