# Pong - The Famous Arcade Game

A Python implementation of the classic Pong arcade game using the Turtle graphics library.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Breakdown](#project-breakdown)
- [Steps Implemented](#steps-implemented)
- [License](#license)

## Overview

This project is a recreation of the classic Pong arcade game using Python's Turtle graphics. The goal is to make the ball bounce between two paddles, where each player controls one paddle. Players gain a point if the ball misses the opponent's paddle. The first player to reach the target score wins.

## Features

- 🎮 Two paddles controlled by players
- 🏓 Ball that moves across the screen and bounces off walls and paddles
- 📊 Score tracking for each player
- 🎯 Collision detection with walls and paddles
- 🚩 Game over when one player misses the ball

## How to Play

- **Player 1** (left paddle) uses the `W` key to move the paddle up and the `S` key to move it down.
- **Player 2** (right paddle) uses the `Up` and `Down` arrow keys to move the paddle up and down.
- The objective is to prevent the ball from going past your paddle. If it does, your opponent gets a point.

## Project Breakdown

1. **Paddle Creation:** Create two paddles that players can control with keys.
2. **Ball Movement:** Create a ball that moves continuously across the screen.
3. **Collision Detection:** Detect when the ball hits the paddle or the walls and make it bounce.
4. **Scoring:** Keep track of the players' scores and update them when the ball goes past a paddle.

## Steps Implemented

### Step 1: Create the Screen
- 🖥️ Initialize a screen using the Turtle library.
- 🖌️ Set up the screen dimensions (e.g., 600x600 pixels).
- 🎨 Add background color and title.

### Step 2: Create and Move the Paddle
- 🏓 Create a paddle using the Turtle object.
- 🔄 Define movement functions to move the paddle up and down.
- ⌨️ Bind keys (`W`/`S` for player 1) and (`Up`/`Down` for player 2) to paddle movement.

### Step 3: Create Another Paddle
- 🏓 Create a second paddle on the right side of the screen.
- 🔄 Assign movement functions to player 2’s paddle.

### Step 4: Create the Ball and Make It Move
- ⚪ Create a ball using the Turtle object.
- ➡️ Define movement behavior for the ball, including speed and direction.

### Step 5: Detect Collision with Wall and Bounce
- 🎯 Detect when the ball hits the top or bottom of the screen.
- 🔄 Reverse the ball's vertical direction when it collides with the wall.

### Step 6: Detect Collision with Paddle
- 🎯 Detect when the ball hits a paddle.
- 🔄 Reverse the ball's horizontal direction upon collision with a paddle.

### Step 7: Detect When Paddle Misses
- 🚩 Detect when the ball goes past a paddle (left or right side).
- 📊 Update the score and reset the ball to the center.

### Step 8: Keep the Score Updated
- 📊 Display scores for both players on the screen.
- ➕ Increment the score of the opposing player when the ball goes past the other paddle.

## License

This project is open-source and available under the [MIT License](LICENSE).
