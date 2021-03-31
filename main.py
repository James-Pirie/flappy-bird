from tkinter import *
import time
import random
from multiprocessing import Process
i = 0


class Bird:
    def __init__(self, canvas, window):
        self.canvas = canvas
        self.player_object = self.canvas.create_rectangle(200, 0, 270, 70, fill="pale green")
        self.velocity = 0
        self.window = window
        self.can_jump = True

    def jump(self, event):
        if self.can_jump:
            self.velocity = 0
            for x in range(7):
                self.canvas.after(2)
                self.velocity -= 1.8
                self.canvas.move(self.player_object, 0, self.velocity)
            self.canvas.update()

    def collide_with_ground(self):
        """
        if self.canvas.coords(self.player_object)[1] <= 3:  # Top wall
            self.velocity = abs(self.velocity)
            self.can_jump = False
        if self.canvas.coords(self.player_object)[1] >= 3:
            self.can_jump = True
        """
        if self.canvas.coords(self.player_object)[3] > 800:  # Bottom wall
            self.velocity = 0

    def gravity(self):
        self.collide_with_ground()
        terminal_velocity = 30
        if self.velocity > terminal_velocity:
            self.velocity = terminal_velocity
        self.canvas.move(self.player_object, 0, self.velocity)

    def compile_movement(self):
        self.window.bind("<space>", self.jump)
        self.gravity()


class Pipe:
    def __init__(self, canvas, window):
        self.canvas = canvas
        self.player_object_top = "placeholder"
        self.player_object_bottom = "placeholder"
        self.velocity = 3
        self.window = window

    def spawn(self):
        x_location = random.randint(275, 550)
        self.player_object_top = self.canvas.create_rectangle(730, x_location, 800, 900, fill="orange")
        self.player_object_bottom = self.canvas.create_rectangle(730, x_location - 270, 800, 0, fill="orange")

    def move_pipe(self):
        self.canvas.move(self.player_object_bottom, -2, 0)
        self.canvas.move(self.player_object_top, -2, 0)


def main():
    window = Tk()
    canvas = Canvas(window, width="800", height="800", background="sky blue")
    canvas.pack()
    pipe = Pipe(canvas=canvas, window=window)
    pipe.spawn()
    player = Bird(canvas=canvas, window=window)
    pipe_counter = 0
    while True:
        pipe_counter += 1
        if pipe_counter == 300:
            new_pipe = Pipe(canvas=canvas, window=window)
            new_pipe.spawn()
            pipe_counter = 0
            new_pipe.move_pipe()
            canvas.update()

        pipe.move_pipe()
        canvas.after(8)
        player.velocity += 0.8
        player.compile_movement()
        canvas.update()


if __name__ == '__main__':
    main()
