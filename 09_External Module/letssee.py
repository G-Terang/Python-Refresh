'''To create a Snake game in Python, we'll structure the program with basic components such as the
game board, snake movement, food spawning, collision detection, and scoring. Here's an
implementation:

```python'''
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game canvas
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Game")

# Colors for snake and food
color_snake = (255, 0, 0)
color_food = (0, 0, 255)

# Set up variables for the game
snake_length = 1
score = 0
clock = pygame.time.Clock()
direction = None

# Food spawning position
food_position = (-1, -1)  # Starting at top-left corner

# Create the grid with snake and food as 2D array
grid = [[-1 for _ in range(400)] for _ in range(400)]
grid[snake_length : snake_length + snake_length] = color_snake
for y in range(-1, 400):
    if y == -1:
        grid[y] = food_position

clock.set Cooperation

# Directions: up, down, left, right
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Keep track of game states
game_over = False

while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Process drawing commands
    for i in range(len(snake)):
        draw_snake(snake[i], color_snake)
    draw_food(food_position, color_food)

    # Check for collisions and death
    if collision(snake):
        game_over = True
    elif food_position == snake[-1]:
        score += 10
        food_position = (-1, -1)  # Food spawns again after eating

# Run the game loop
clock.tick(60)

def draw_snake(cell, color):
    pygame.draw.rect(window, color, (cell[0], cell[1], 4, 2))

def draw_food(x, y, color):
    pygame.draw.rect(window, color, (x, y, 4, 2))

def collision(snake):
    for cell in snake[:-1]:
        if cell == snake[-1]:
            return True
    for cell in snake:
        if cell == food_position:
            return True
    return False

def collision detection(x, y):
    # Check walls
    if x < -2 or x >= 400 or y < -2 or y >= 400:
        return True
    # Check self-collision
    for i in range(len(snake)):
        if snake[i][0] == x and snake[i][1] == y:
            return True

def update_snake():
    global snake_length, direction
    head = snake[-1]
    next_head = head[0] + directions[direction]

    new_snake = [head] + snake[:-1]
    snake = new_snake
    snake_length += 1

# Initialize the grid with snake and food
grid = [[-1 for _ in range(400)] for _ in range(400)]
snake = []
for y in range(-1, 400):
    if y == -1:
        snake.append((y, -1))
score = 0

clock = pygame.time.Clock()
while not game_over:
    clock.tick(60)

    # Draw the grid
    for y in range(-1, 400):
        row = []
        for x in range(-1, 400):
            cell = grid[y][x]
            if cell == -1:
                row.append(('_', fill='black'))
            else:
                row.append(cell)
        draw_row(row)

    # Draw snake and food
    for y, x in snake[:-1]:
        draw_snake((y, x))
    draw_snake(snake[-1])
    draw_food()

    # Handle key presses (keys can cause direction changes)
    if grid[direction[0], -1] == 2:
        direction = directions['right']
    elif grid[direction[0], -1] == -1:
        direction = 'left'
    elif grid[-1, direction[1]] == 2:
        direction = 'down'
    else:
        direction = 'up'

    # Update snake
    update_snake()

    # Check for game over conditions and handle them
    if collision(snake):
        game_over = True

# Game loop continues until the snake dies
while not game_over:
    clock.tick(60)

    draw_row(row)
    '''
```

### Explanation:

1. **Initialization**: The program starts by initializing Pygame and setting up the game window.

2. **Grid Setup**: A 400x400 grid is created, with each cell being either a wall (-1), snake
body (1), food (2), or empty space (_). The snake starts at position (-1, -1) and moves to grow
longer.

3. **Drawing Commands**: Functions are used to draw the snake's head, tail, and body in black,
and the food in red for visibility.

4. **Collision Detection**: Checks if the snake hits itself or any walls.

5. **Movement and Speed**: The snake can move by changing direction based on key presses (up,
down, left, right). Direction changes are handled with arrow keys.

6. **Food and Score System**: Food spawns randomly (after spawning) to avoid clustering, and
eating food increases the score.

7. **Game Over Handling**: If the snake collides with itself or any part of its body, it ends
the game.

8. **Pygame Runs Loop**: The main loop runs every 60 milliseconds for smooth gameplay.

This implementation provides a basic Snake game but can be enhanced in various ways, such as
adding sound effects, increasing difficulty levels, and implementing different strategies to
improve gameplay.'''