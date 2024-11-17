import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")

        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(20, 20), (40, 20), (60, 20)]
        self.food = (100, 100)
        self.direction = "Right"

        self.score = 0
        self.running = True

        self.canvas.bind_all("<Key>", self.change_direction)
        self.update_game()

    def update_game(self):
        if not self.running:
            return

        self.move_snake()
        if self.check_collision():
            self.running = False
            self.canvas.create_text(200, 200, text=f"Game Over! Score: {self.score}", fill="white", font=("Helvetica", 24))
            return

        self.canvas.delete("all")
        self.draw_snake()
        self.draw_food()
        self.master.after(100, self.update_game)

    def move_snake(self):
        x, y = self.snake[-1]
        if self.direction == "Left":
            x -= 20
        elif self.direction == "Right":
            x += 20
        elif self.direction == "Up":
            y -= 20
        elif self.direction == "Down":
            y += 20

        self.snake.append((x, y))
        if (x, y) == self.food:
            self.score += 1
            self.food = (random.randint(0, 19) * 20, random.randint(0, 19) * 20)
        else:
            self.snake.pop(0)

    def check_collision(self):
        x, y = self.snake[-1]
        if x < 0 or x >= 400 or y < 0 or y >= 400 or (x, y) in self.snake[:-1]:
            return True
        return False

    def change_direction(self, event):
        new_direction = event.keysym
        all_directions = {"Left", "Right", "Up", "Down"}
        opposite_directions = {("Left", "Right"), ("Right", "Left"), ("Up", "Down"), ("Down", "Up")}

        if new_direction in all_directions and (self.direction, new_direction) not in opposite_directions:
            self.direction = new_direction

    def draw_snake(self):
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="green")

    def draw_food(self):
        x, y = self.food
        self.canvas.create_oval(x, y, x+20, y+20, fill="red")

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
