# Pong Game 🎮

A classic Pong game implementation built with Python's `turtle` module. This is a learning project to master core Python concepts including object-oriented programming, game development, and collision detection.

## Features

- **Two-player gameplay**: Control paddles with keyboard inputs (Arrow keys & Z/S)
- **Realistic ball physics**: Ball bounces off walls and paddles with speed acceleration
- **Score tracking**: Automatic scoreboard that tracks both players
- **Collision detection**: Accurate detection for wall bounces and paddle hits
- **Clean architecture**: Code organized into separate classes for Ball, Paddle, and Scoreboard

## Game Board

<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; background: url('data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 800 400%22><rect width=%22800%22 height=%22400%22 fill=%22%231a1a1a%22/></svg>'); background-color: #fafafa;">
  <defs>
    <style>
      @media (prefers-color-scheme: dark) {
        rect.board-bg { fill: #1a1a1a; }
        line, .court-line { stroke: #444; }
        rect.paddle { fill: #a0a0a0; }
        circle.ball { fill: #00d9ff; }
        text { fill: #e0e0e0; }
      }
      @media (prefers-color-scheme: light) {
        rect.board-bg { fill: #fafafa; }
        line, .court-line { stroke: #ddd; }
        rect.paddle { fill: #888; }
        circle.ball { fill: #00a8cc; }
        text { fill: #333; }
      }
      [data-theme="dark"] rect.board-bg { fill: #1a1a1a; }
      [data-theme="dark"] line, [data-theme="dark"] .court-line { stroke: #444; }
      [data-theme="dark"] rect.paddle { fill: #a0a0a0; }
      [data-theme="dark"] circle.ball { fill: #00d9ff; }
      [data-theme="dark"] text { fill: #e0e0e0; }
      
      [data-theme="light"] rect.board-bg { fill: #fafafa; }
      [data-theme="light"] line, [data-theme="light"] .court-line { stroke: #ddd; }
      [data-theme="light"] rect.paddle { fill: #888; }
      [data-theme="light"] circle.ball { fill: #00a8cc; }
      [data-theme="light"] text { fill: #333; }
      
      text.label { font-size: 14px; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; font-weight: 500; }
      text.score { font-size: 24px; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; font-weight: 600; }
    </style>
  </defs>
  
  <!-- Board background -->
  <rect class="board-bg" width="800" height="400"/>
  
  <!-- Court border -->
  <rect x="50" y="50" width="700" height="300" fill="none" stroke-width="2" class="court-line"/>
  
  <!-- Center line (dashed) -->
  <line x1="400" y1="50" x2="400" y2="350" stroke-width="1" stroke-dasharray="5,5" class="court-line"/>
  
  <!-- Left paddle -->
  <rect class="paddle" x="30" y="150" width="20" height="100" rx="4"/>
  <text class="label" x="20" y="380" text-anchor="end">Player 1</text>
  
  <!-- Right paddle -->
  <rect class="paddle" x="750" y="150" width="20" height="100" rx="4"/>
  <text class="label" x="780" y="380" text-anchor="start">Player 2</text>
  
  <!-- Ball -->
  <circle class="ball" cx="400" cy="200" r="8"/>
  
  <!-- Score displays -->
  <text class="score" x="200" y="100" text-anchor="middle">0</text>
  <text class="score" x="600" y="100" text-anchor="middle">0</text>
  
  <!-- Labels -->
  <text class="label" x="400" y="380" text-anchor="middle">Arrow Keys / Z-S to Move</text>
</svg>

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

## Future Improvements

- AI opponent for single-player mode
- Difficulty levels with adjustable ball speed
- Sound effects
- Game pause functionality
- High score tracking

---
Created as part of Python learning journey focusing on game development fundamentals.
