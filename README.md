# Pong Game

This is a simple Pong game implemented in Python using the `turtle` module. It includes basic paddle and ball movement, collision detection, and scoring. The game can be played by two players on the same keyboard.

## Project Structure

- **main.py**: Main game loop and screen setup.
- **paddle.py**: Paddle class with paddle movement logic.
- **ball.py**: Ball class with movement and collision logic.
- **scoreboard.py**: Scoreboard class to display and update the score.

## How to Play

1. Clone the repository or download the files.
2. Run `main.py` to start the game.
3. Player controls:
   - Left paddle: `W` to move up, `S` to move down.
   - Right paddle: `Up Arrow` to move up, `Down Arrow` to move down.
4. The first paddle to miss the ball gives a point to the opponent.

## Code Details

### main.py

This file contains the main game loop, which:

- Sets up the screen and initializes the paddles, ball, and scoreboard.
- Listens for keyboard inputs to control the paddles.
- Manages ball movement, wall collisions, paddle collisions, and score updates.

### ball.py

The `Ball` class, inheriting from `Turtle`, is responsible for:

- Initializing the ball shape and color.
- Moving the ball at a constant speed, with collision checks for bouncing off walls and paddles.
- Resetting the ball position and direction when it reaches the left or right edge.

Key Methods:

- `move()`: Moves the ball across the screen.
- `bounce_x()`: Reverses the ball's x-direction when it hits a paddle.
- `bounce_y()`: Reverses the ball's y-direction when it hits the top or bottom wall.
- `reset()`: Resets the ball to the center of the screen and reverses direction.

### paddle.py

The `Paddle` class, inheriting from `Turtle`, is responsible for:

- Creating a paddle at a specified position on the screen.
- Moving the paddle up or down based on player input.

Key Methods:

- `go_up()`: Moves the paddle up by 20 units.
- `go_down()`: Moves the paddle down by 20 units.

### scoreboard.py

The `Scoreboard` class, inheriting from `Turtle`, is responsible for:

- Displaying and updating the score for each player.

Key Methods:

- `update_scoreboard()`: Clears and redraws the current score.
- `l_point()`: Increases the left player's score by 1 and updates the display.
- `r_point()`: Increases the right player's score by 1 and updates the display.

## Requirements

- Python 3.x
- `turtle` module (included with Python standard library)

## Running the Game

1. Open a terminal in the project directory.
2. Run the game with the following command:

   ```bash
   python main.py
