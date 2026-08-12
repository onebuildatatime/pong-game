# Pong Game 🎮

A classic Pong game implementation built with Python's `turtle` module. This is a learning project to master core Python concepts including object-oriented programming, game development, and collision detection.

## Features

- **Two-player gameplay**: Control paddles with keyboard inputs (Arrow keys & Z/S)
- **Realistic ball physics**: Ball bounces off walls and paddles with speed acceleration
- **Score tracking**: Automatic scoreboard that tracks both players
- **Collision detection**: Accurate detection for wall bounces and paddle hits
- **Clean architecture**: Code organized into separate classes for Ball, Paddle, and Scoreboard

## Game Board

![Pong Game Board Diagram](game-board.svg)

## How to Run

```bash
python main.py
```

### Controls
- **Right Paddle**: Up Arrow & Down Arrow keys
- **Left Paddle**: Z (up) & S (down) keys

## What I Learned

### Python Concepts
✅ **Object-Oriented Programming**: Created reusable `Ball`, `Paddle`, and `Scoreboard` classes  
✅ **Inheritance**: Used `Turtle` class inheritance for game objects  
✅ **Encapsulation**: Organized attributes and methods logically within classes  
✅ **Game Loop**: Implemented event-driven programming with keyboard listeners  
✅ **Collision Detection**: Used distance calculations to detect ball-paddle and ball-wall collisions  

### Game Development Concepts
- Screen rendering and object positioning using coordinates
- Real-time object movement and animation
- Event handling for keyboard input
- Game state management

## Project Structure

```
pong-game/
├── main.py          # Main game loop and collision logic
├── ball.py          # Ball class with movement and bounce mechanics
├── paddle.py        # Paddle class with directional movement
├── scoreboard.py    # Score tracking and display
└── README.md        # This file
```

## Dependencies

- Python 3.x
- `turtle` (built-in, no installation needed)

---

## Credits

This project was built following tutorials and teachings by **Angela Yu**, whose comprehensive Python course provided the foundational knowledge for game development concepts and object-oriented programming principles used in this implementation.

📚 **Course**: [100 Days of Code - Day 22: Pong Game](https://www.udemy.com/course/100-days-of-code/learn/lecture/20342613?start=1#overview)

Created as part of Python learning journey focusing on game development fundamentals.
