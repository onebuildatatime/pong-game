#!/usr/bin/env python3
"""
Capture game screenshots for documentation.
This script runs the game and takes screenshots at different game states.
Uses turtle's getcanvas() to capture window content.
"""

import time
import os
from turtle import Screen, Turtle
from tkinter import PhotoImage
import signal

from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

# Create output directory for screenshots
os.makedirs("screenshots", exist_ok=True)

def capture_turtle_screen(screen, filename):
    """Capture turtle canvas as PostScript/Image"""
    try:
        # Use turtle's built-in screen capture
        canvas = screen.getcanvas()

        # Save as PostScript first (more reliable)
        ps_file = f"screenshots/{filename.replace('.png', '.eps')}"
        canvas.postscript(file=ps_file, colormode='color')
        print(f"✓ Saved PostScript: {ps_file}")

        # If ghostscript is available, convert to PNG
        import subprocess
        png_file = f"screenshots/{filename}"
        try:
            subprocess.run([
                'gs', '-q', '-dNOPAUSE', '-dBATCH', '-dSAFER',
                '-sDEVICE=png16m', '-r150',
                f'-sOutputFile={png_file}',
                ps_file
            ], check=True, capture_output=True, timeout=5)
            print(f"✓ Converted to PNG: {png_file}")
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired, subprocess.CalledProcessError):
            print(f"⚠ Ghostscript not available - keeping PostScript format")
            print(f"  You can convert manually: gs -q -dNOPAUSE -dBATCH -sDEVICE=png16m -r150 -sOutputFile={png_file} {ps_file}")
            return True

    except Exception as e:
        print(f"✗ Could not capture {filename}: {e}")
        import traceback
        traceback.print_exc()
        return False

def run_game_with_screenshots():
    """Run game and capture screenshots at key moments"""

    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong - Screenshot Capture")
    screen.tracer(0)

    print("\n📸 Capturing Start Screen...")

    # Create start screen display
    title = Turtle()
    title.hideturtle()
    title.color("white")
    title.speed(0)
    title.penup()
    title.goto(0, 100)
    title.write("PONG", align="center", font=("Arial", 80, "bold"))

    instruction = Turtle()
    instruction.hideturtle()
    instruction.color("lime")
    instruction.speed(0)
    instruction.penup()
    instruction.goto(0, -200)
    instruction.write("PRESS SPACE TO START", align="center", font=("Arial", 28, "normal"))

    screen.update()
    time.sleep(1)

    # Capture start screen
    capture_turtle_screen(screen, "01-start-screen.png")

    # Clear and setup game
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    # Set up keyboard listeners
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "z")
    screen.onkey(l_paddle.go_down, "s")

    print("📸 Capturing Active Gameplay...")

    game_is_on = True
    frame_count = 0

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
           (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Detect R paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Detect L paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        # Auto-move paddles for demo
        if frame_count % 10 == 0:
            if frame_count % 40 < 20:
                l_paddle.go_up()
            else:
                l_paddle.go_down()

            if frame_count % 50 < 25:
                r_paddle.go_up()
            else:
                r_paddle.go_down()

        # Capture screenshots at key moments
        if frame_count == 30:  # After a few seconds of gameplay
            capture_turtle_screen(screen, "02-gameplay.png")
        elif frame_count == 60:  # Let scores increase a bit
            capture_turtle_screen(screen, "03-intense-moment.png")
            game_is_on = False

        frame_count += 1

    screen.update()
    time.sleep(1)

    print(f"\n✅ Screenshots captured!")
    print("📁 Check the 'screenshots' folder for images")

    # Close after a moment
    time.sleep(2)
    screen.bye()

if __name__ == "__main__":
    print("🎮 Pong Game Screenshot Capture Tool")
    print("====================================")

    try:
        run_game_with_screenshots()
    except KeyboardInterrupt:
        print("\n\nCapture interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()