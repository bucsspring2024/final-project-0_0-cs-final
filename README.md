[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14592278&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Highway Showdown>>
## CS110 Final Project  << Spring , 2024 sophmore>>

## Team Members

<< Derrick Poon >>

***

## Project Description

<< You just robbed somebodys dog and now you're on the run. The person you stole the dog from is chasing you and you go onto the wrong highway where the cars are coming at you. The car will proceed to go faster making it more difficult as if this was a real life chase and you are going faster and faster. Your goal is to avoid all these cars and make it out with the dog alive.>>

***    

## GUI Design

### Initial Design
1. game over screen
2. Campaign
3. random events
4. fundraisers
5. polls

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design
class Bullet:
    def __init__(self, x, y, img_file):
        """
        Initializes the bullet object.
        args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
            - img_file : str - path to the image file
        """

    def move_up(self):
        """
        Moves the bullet up by decreasing the y-coordinate.
        args: None
        return: None
        """



### Features

1. << Start Button >>
2. << Moving Car >>
3. << Obstacle Collisions >>
4. << Exit Button >>
5. << Pause Button >>

### Classes

- << You should have a list of each of your classes with a description >>

## ATP

Step 1- Action: Go to terminal and run code with python3 main.py. 
        Result: Pygame launches and a start button shows up so you can begin the game

Step 2- Action: Press start button. 
        Result: Game should begin and bring you to screen on you on a highway with a yellow car that you are "driving" You should see the cars coming at you, your score on the left along with a pause button.

Step 3- Action: Use your left and right arrow keys to control car so it does not crash or hit anything. 
        Result: Your score will go up and game speed will increase making difficulty harder. 

Step 4- Action: While using your left and right arrows keys to control the car you hit a car coming at you or go off the highway. 
        Result: The game ends and a black screen shows up saying Game Over and Thanks for Playing! It will also include an option for you to either restart the game from the beginning or exit the game

Step 5- Action: You decide to play again and hit the red restart button.      
        Result: It will bring you straight back to the beginning where you see the yellow car you control with the left and right arrow keys and you keep playing again.

Step 6- Action: You have to sneeze and youre scared that youre gonna lose. There is a pause button on the top left that you can click anytime to stop the game for however long you need. 
        Result: Three red buttons show up giving you the options to either resume, restart or exit the game

Step 7- Action: You lost again and you dont want to play the game anymore. You will see the red exit button on the screen. Click on that with your mouse or trackpad. 
        Result: The game will close properly and bring you back to the screen/application you were last on.
