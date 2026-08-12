from turtle import Turtle
import time

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.game_started = False

    def show_title_screen(self):
        """Display animated start screen"""
        # Setup screen for title
        self.screen.clear()
        self.screen.bgcolor("black")

        # Create main title
        title = Turtle()
        title.hideturtle()
        title.color("white")
        title.speed(0)
        title.penup()

        # Animate title letters
        self._animate_title(title)

        # Create decorative bouncing balls
        self._animate_decorative_balls()

        # Create pulsing start instruction
        self._show_start_instruction()

        # Setup keyboard listener
        self.screen.listen()
        self.screen.onkey(self._start_game, "space")

        # Wait for player to start
        while not self.game_started:
            self.screen.update()
            time.sleep(0.05)

    def _animate_title(self, title):
        """Animate PONG title with scaling effect"""
        title.goto(0, 100)
        title.font = ("Arial", 80, "bold")

        # Pulsing title animation
        for _ in range(3):
            title.clear()
            title.write("PONG", align="center", font=("Arial", 80, "bold"))
            self.screen.update()
            time.sleep(0.3)
            title.clear()
            self.screen.update()
            time.sleep(0.2)

        # Final display
        title.write("PONG", align="center", font=("Arial", 80, "bold"))
        self.screen.update()

    def _animate_decorative_balls(self):
        """Create animated bouncing balls around the screen"""
        balls = []
        positions = [(-200, 200), (200, 200), (-200, -150), (200, -150)]

        for pos in positions:
            ball = Turtle()
            ball.shape("circle")
            ball.color("cyan")
            ball.penup()
            ball.goto(pos)
            balls.append(ball)

        # Animate balls - move up and down
        for cycle in range(20):
            for i, ball in enumerate(balls):
                # Bounce effect
                offset = 30 * abs(__import__('math').sin(cycle * 0.3 + i))
                if positions[i][1] > 0:
                    ball.goto(positions[i][0], positions[i][1] - offset)
                else:
                    ball.goto(positions[i][0], positions[i][1] + offset)

            self.screen.update()
            time.sleep(0.1)

    def _show_start_instruction(self):
        """Show pulsing start instruction"""
        instruction = Turtle()
        instruction.hideturtle()
        instruction.color("lime")
        instruction.speed(0)
        instruction.penup()
        instruction.goto(0, -200)

        # Pulsing text
        for cycle in range(40):
            instruction.clear()
            # Create pulsing effect
            size = 20 + int(5 * abs(__import__('math').sin(cycle * 0.1)))
            instruction.font = ("Arial", size, "normal")
            instruction.write("PRESS SPACE TO START", align="center", font=("Arial", size, "normal"))
            self.screen.update()
            time.sleep(0.05)

    def _start_game(self):
        """Start the game"""
        self.game_started = True