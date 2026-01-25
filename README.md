# 🐍 Snake Game (Pygame)

A classic **Snake game** built using **Python and the Pygame library**. In this
game, the player controls a snake that moves around the screen, eats apples, 
and grows longer with each apple consumed. The goal is to survive as long as 
possible without colliding with the boundaries or the snake's own body.

---

## 🎮 Game Features

* Smooth snake movement using keyboard controls
* Snake grows longer each time it eats an apple 🍎
* Apples spawn at random positions on the screen
* Modular and clean project structure
* Easily configurable settings (colors, speed, screen size, etc.)

---

## 🛠 Technologies & Modules Used

* **Python 3**
* **Pygame** – for graphics, events, and game loop
* **random** – for generating random apple positions

---

## 📁 Project Structure

```
snake-game/
│
├── main.py        # Entry point of the game (game loop, event handling)
├── snake.py      # Snake (player) logic and movement
├── apple.py      # Apple logic and random spawning
├── settings.py   # Game settings (colors, speed, screen size, etc.)
├── body.py       # Body of Snake
├── README.md     # Project documentation
```

---

## 📜 Module Description

### `main.py`

* Runs the entire game
* Initializes Pygame
* Handles the game loop, events, and rendering
* Coordinates interaction between the snake and the apple

### `snake.py`

* Represents the player-controlled snake
* Handles snake movement and growth
* Manages the snake body segments on the screen

### `apple.py`

* Represents the apple
* Spawns apples at random positions on the screen
* Detects collision with the snake

### `settings.py`

* Stores all configurable values such as:

  * Screen width and height
  * Colors
  * Player speed
  * Grid size or sprite size

---

## ▶️ How to Run the Game

1. Make sure Python 3 is installed
2. Install Pygame:

   ```bash
   pip install pygame
   ```
3. Run the game:

   ```bash
   python main.py
   ```

---

## 🎯 Controls

* **WASD** – Move the snake (Up, Down, Left, Right)

---

## 🚀 Future Improvements (Optional)

* Score tracking system
* Game over screen
* Sound effects and background music
* Difficulty levels
* High score saving

---

## 📌 Notes

This project is designed for learning purposes and demonstrates core game 
development concepts such as sprite management, collision detection, and 
state-based movement using Pygame.

---
