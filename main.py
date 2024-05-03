import pygame
from time import sleep
from src.Model import Model
from src.View import CarView
from src.Controller import Controller


def main():
    global model, view
    model = Model()
    view = CarView(model)
    controller = Controller(model, view)

    while True and model.game_over == False:
        if (model.start_check == True):
            controller.handle_events()
            view.render_start_panel()
        else:
            if (model.crashed == False):
                controller.handle_events()
                if (model.game_paused == False):
                    controller.update()
                    model.count += 1
                    if model.count % 100 == 0:
                        model.enemy_car_speed += 1
                        view.scroll_speed += 1
                view.render()
                
            elif model.crashed and not model.game_over:

                controller.handle_events()
                view.render_fail_panel("GAME OVER")

            elif model.crashed and model.game_over:
                pygame.quit()
    save_high_score(model.count)

def save_high_score(score):
    file_path = "etc/high_score.txt"
    try:
        # Try to read the existing high score
        with open(file_path, "r") as file:
            existing_high_score = int(file.read())
    except FileNotFoundError:
        # If the file doesn't exist, initialize the high score to 0
        existing_high_score = 0
    
    # If the new score is higher than the existing high score, update the file
    if score > existing_high_score:
        with open(file_path, "w") as file:
            file.write(str(score))

def restart():
    model.__init__()
    view.scroll_speed = 3

if __name__ == '__main__':
    main()
