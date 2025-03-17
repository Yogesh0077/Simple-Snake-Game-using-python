import tkinter as tk
import random


GAME_WIDTH = 700
GAME_HEIGHT = 600
SPEED = 150
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "blue"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "pink"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.square = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.square.append(square)

class Food:
    def __init__(self):

        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_Turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.square.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.square[-1])
        del snake.square[-1]

    if check_Collisions(snake):
        game_Over()
    else:
        window.after(SPEED, next_Turn, snake, food)

def change_Direction(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def check_Collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_Over():
    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="GAME OVER", fill="red", tags="game")

window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = tk.Label(window, text="Score:{}".format(score), font=('consolas', 20))
label.pack()

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_Width = window.winfo_width()
window_Height = window.winfo_height()
screen_Width = window.winfo_screenwidth()
screen_Height = window.winfo_screenheight()

x = int(screen_Width / 2) - int(window_Width / 2)
y = int(screen_Height / 2) - int(window_Height / 2)

window.geometry(f"{window_Width}x{window_Height}+{x}+{y}")

window.bind('<Left>', lambda event: change_Direction('left'))
window.bind('<Right>', lambda event: change_Direction('right'))
window.bind('<Up>', lambda event: change_Direction('up'))
window.bind('<Down>', lambda event: change_Direction('down'))

snake = Snake()
food = Food()

next_Turn(snake, food)

window.mainloop()
