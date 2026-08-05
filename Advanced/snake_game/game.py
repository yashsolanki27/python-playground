"""
Snake Game (Terminal Version)
A classic snake game to learn OOP, game loops, and terminal UI.

How to Play:
1. Control the snake using arrow keys or WASD
2. Eat the food (@) to grow longer
3. Avoid hitting walls or yourself
4. Try to get the highest score!
5. Type 'quit' to exit the game.

Python Concepts:
- Object-Oriented Programming
- 2D lists/grids
- Game loop
- Input handling
- Collision detection
- Score tracking
- Terminal clearing
"""

import random
import time
import os
import sys
from typing import List, Tuple


class Point:
    """Represents a point on the grid."""
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Snake:
    """Represents the snake."""
    
    def __init__(self, start_pos: Point):
        self.body: List[Point] = [start_pos]
        self.direction: Point = Point(1, 0)  # Moving right
    
    def move(self) -> Point:
        """
        Move the snake in current direction.
        
        Returns:
            New head position
        """
        head = self.body[0]
        new_head = Point(head.x + self.direction.x, head.y + self.direction.y)
        self.body.insert(0, new_head)
        return new_head
    
    def grow(self):
        """Grow the snake by not removing tail."""
        pass  # Body already grew in move() by not removing tail
    
    def shrink(self):
        """Remove the tail segment."""
        self.body.pop()
    
    def check_collision(self) -> bool:
        """Check if snake collides with itself."""
        head = self.body[0]
        return head in self.body[1:]
    
    def change_direction(self, new_direction: Point):
        """Change direction (can't reverse)."""
        # Prevent reversing
        if self.direction.x + new_direction.x != 0 or self.direction.y + new_direction.y != 0:
            self.direction = new_direction


class SnakeGame:
    """Main game class."""
    
    def __init__(self, width: int = 20, height: int = 15):
        self.width = width
        self.height = height
        self.snake: Snake = None
        self.food: Point = None
        self.score: int = 0
        self.game_over: bool = False
        self.quit_game: bool = False
        
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def create_grid(self) -> List[List[str]]:
        """Create the game grid."""
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Draw borders
        for x in range(self.width):
            grid[0][x] = '─'
            grid[self.height - 1][x] = '─'
        
        for y in range(self.height):
            grid[y][0] = '│'
            grid[y][self.width - 1] = '│'
        
        # Draw corners
        grid[0][0] = '┌'
        grid[0][self.width - 1] = '┐'
        grid[self.height - 1][0] = '└'
        grid[self.height - 1][self.width - 1] = '┘'
        
        # Place snake
        for segment in self.snake.body:
            if 0 < segment.x < self.width - 1 and 0 < segment.y < self.height - 1:
                grid[segment.y][segment.x] = '█'
        
        # Place food
        if self.food:
            grid[self.food.y][self.food.x] = '@'
        
        return grid
    
    def display(self):
        """Display the game."""
        self.clear_screen()
        
        # Create and display grid
        grid = self.create_grid()
        
        print("\n" + "=" * 50)
        print(" SNAKE GAME")
        print("=" * 50)
        print(f" Score: {self.score}")
        print(f" Length: {len(self.snake.body)}")
        print("-" * 50)
        
        for row in grid:
            print(''.join(row))
        
        print("-" * 50)
        print(" Controls: WASD or Arrow Keys")
        print(" Quit: 'q'")
        print("=" * 50)
    
    def spawn_food(self):
        """Spawn food at random location."""
        while True:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            food_point = Point(x, y)
            
            # Make sure food doesn't spawn on snake
            if food_point not in self.snake.body:
                self.food = food_point
                break
    
    def check_wall_collision(self, point: Point) -> bool:
        """Check if point hits wall."""
        return (point.x <= 0 or point.x >= self.width - 1 or
                point.y <= 0 or point.y >= self.height - 1)
    
    def check_food_collision(self, point: Point) -> bool:
        """Check if point hits food."""
        return self.food and point == self.food
    
    def process_input(self, key: str):
        """Process player input."""
        if key == 'q':
            self.quit_game = True
            return
        
        # Direction mapping
        directions = {
            'w': Point(0, -1),  # Up
            's': Point(0, 1),   # Down
            'a': Point(-1, 0),  # Left
            'd': Point(1, 0),   # Right
        }
        
        if key in directions:
            self.snake.change_direction(directions[key])
    
    def update(self):
        """Update game state."""
        if self.game_over or self.quit_game:
            return
        
        # Move snake
        new_head = self.snake.move()
        
        # Check wall collision
        if self.check_wall_collision(new_head):
            self.game_over = True
            return
        
        # Check self collision
        if self.snake.check_collision():
            self.game_over = True
            return
        
        # Check food collision
        if self.check_food_collision(new_head):
            self.score += 10
            self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.shrink()
    
    def display_game_over(self):
        """Display game over screen."""
        self.clear_screen()
        print("\n" + "=" * 50)
        print(" GAME OVER!")
        print("=" * 50)
        print(f" Your Score: {self.score}")
        print(f" Snake Length: {len(self.snake.body)}")
        print("-" * 50)
        
        # Performance message
        if self.score >= 100:
            print(" 🏆 Amazing! You're a Snake Master!")
        elif self.score >= 50:
            print(" 🌟 Great job! Very impressive!")
        elif self.score >= 20:
            print(" 👍 Good effort! Keep practicing!")
        else:
            print(" 💪 Nice try! You'll do better next time!")
        
        print("=" * 50)
    
    def play(self):
        """Main game loop."""
        # Initialize
        start_x = self.width // 2
        start_y = self.height // 2
        self.snake = Snake(Point(start_x, start_y))
        self.score = 0
        self.game_over = False
        self.quit_game = False
        
        # Spawn initial food
        self.spawn_food()
        
        # Game loop
        while not self.game_over and not self.quit_game:
            # Display game
            self.display()
            
            # Get input (simplified for terminal)
            try:
                # For Windows
                if os.name == 'nt':
                    import msvcrt
                    if msvcrt.kbhit():
                        key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
                        self.process_input(key)
                else:
                    # For Unix/Linux/Mac
                    import tty
                    import termios
                    fd = sys.stdin.fileno()
                    old_settings = termios.tcgetattr(fd)
                    try:
                        tty.setraw(sys.stdin.fileno())
                        ch = sys.stdin.read(1)
                        if ch:
                            self.process_input(ch.lower())
                    finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            except:
                pass
            
            # Update game
            self.update()
            
            # Control game speed
            time.sleep(0.1)
        
        # Show game over
        if not self.quit_game:
            self.display_game_over()
        
        return self.score


def display_welcome():
    """Display welcome message."""
    print("\n" + "=" * 60)
    print(" SNAKE GAME (Terminal Version)")
    print("=" * 60)
    print("\nControls:")
    print("  W / ↑  - Move Up")
    print("  S / ↓  - Move Down")
    print("  A / ←  - Move Left")
    print("  D / →  - Move Right")
    print("  Q      - Quit Game")
    print("\nObjective:")
    print("  - Eat the food (@) to grow")
    print("  - Avoid hitting walls or yourself")
    print("  - Try to get the highest score!")
    print("-" * 60 + "\n")
    input("Press Enter to start the game...")


def main():
    """Main entry point."""
    display_welcome()
    
    # Game statistics
    games_played = 0
    total_score = 0
    high_score = 0
    
    while True:
        # Create and play game
        game = SnakeGame(width=20, height=15)
        score = game.play()
        
        # Update statistics
        games_played += 1
        total_score += score
        if score > high_score:
            high_score = score
        
        # Display statistics
        print(f"\n--- Statistics ---")
        print(f"Games played: {games_played}")
        print(f"High score: {high_score}")
        if games_played > 0:
            print(f"Average score: {total_score / games_played:.1f}")
        
        # Ask to play again
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again in ['no', 'n']:
            print("\nThanks for playing! Goodbye!")
            break
        
        print("\nStarting new game...")
        time.sleep(1)
    
    print("\nFinal Statistics:")
    print(f"Total games: {games_played}")
    print(f"High score: {high_score}")
    print(f"Total score: {total_score}")


if __name__ == "__main__":
    main()