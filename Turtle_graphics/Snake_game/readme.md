# Snake Game

A classic **Snake Game** built in Python using the **Turtle** graphics library. The snake is controlled using the arrow keys, and the objective is to eat food that appears on the screen, making the snake grow longer with each bite. The game ends when the snake collides with itself or the screen boundary.

## Table of Contents
- [Features](#features)
- [How to Play](#how-to-play)
- [Setup Instructions](#setup-instructions)
- [Game Preview](#game-preview)
- [Technologies Used](#technologies-used)
- [Challenges and Learning Outcomes](#challenges-and-learning-outcomes)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Turtle Graphics**: The game is developed using the Turtle graphics library in Python.
- **Keyboard Control**: Move the snake using the arrow keys.
- **Score Tracking**: The player’s score increases as the snake consumes food.
- **Game Over**: The game ends when the snake runs into itself or the boundary.
  
## How to Play
- Use the arrow keys to control the direction of the snake:
  - `Up Arrow` to move up.
  - `Down Arrow` to move down.
  - `Left Arrow` to move left.
  - `Right Arrow` to move right.
- The goal is to eat the food that appears on the screen to grow the snake longer.
- Avoid colliding with the snake's own body or the walls, as that will end the game.

## Setup Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/maharshiPatel9094/python_dev_100projects/tree/main/Turtle_graphics/Snake_game
    ```

2. **Install Python** (if you haven't already):
    - Download Python from [here](https://www.python.org/downloads/) and follow the instructions for your operating system.

3. **Run the game**:
    ```bash
    python main.py
    ```

## Technologies Used
- **Python**: Core programming language.
- **Turtle Graphics**: For rendering game visuals and capturing keyboard input.

## Challenges and Learning Outcomes
This project helped me deepen my understanding of:
- **Turtle Graphics**: Using the `turtle` module for graphics in Python.
- **Event-Driven Programming**: Handling keyboard events with `screen.onkey`.
- **Object-Oriented Programming**: Structuring the game into classes for the snake, food, and scoreboard.
- **Game Loops and State Management**: Controlling game flow using an infinite loop and handling state transitions like game over.

## Future Improvements
- Adding **levels** or increasing difficulty as the game progresses.
- Implementing **special food items** with varying effects (e.g., shrinking the snake, slowing it down).
- Adding **sound effects** to enhance the user experience.
- Displaying a **high score** board.

## Contributing
Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request. For any major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
