# Turtle Crossing Game

A simple Python game using the Turtle module, where a turtle attempts to cross the road while avoiding randomly generated cars. The cars increase in speed as the player levels up.

## How to Play
1. Use the **Up** arrow key to move the turtle forward and the **Down** arrow key to move the turtle backward.
2. Avoid the cars that move from right to left on the screen.
3. Reach the top of the screen to level up and reset the turtle's position.
4. Each time you level up, the car speed increases, making the game more challenging.
5. The game ends if the turtle collides with any car.

## Features
1. **Turtle Movement**: The turtle can move forward by pressing the **Up** arrow key and backward by pressing the **Down** arrow key. There's no left or right movement.
2. **Car Generation**: Cars are randomly generated along the y-axis and move from the right edge of the screen to the left.
3. **Leveling Up**: When the turtle reaches the top edge of the screen, it resets to its original position, and the game increases in difficulty as the cars move faster.
4. **Game Over Condition**: If the turtle collides with a car, the game stops, and a "Game Over" message is displayed.

## Files in the Project
- **main.py**: The core game logic that controls the turtle, cars, and gameplay.
- **player.py**: Defines the turtle player, including movement and crossing detection.
- **car_manager.py**: Manages the car objects, including car creation, movement, and increasing speed.
- **scoreboard.py**: Manages the display of the player's level and game-over messages.

## How to Run
1. Clone or download the project to your local machine.
2. Make sure you have Python installed. If not, download it from [here](https://www.python.org/downloads/).
3. Install any required packages (such as `turtle` if you're using a non-standard environment).
4. Run the `main.py` file using a Python interpreter.

```bash
python main.py
