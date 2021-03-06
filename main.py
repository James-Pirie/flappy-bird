from tkinter import *
import random
i = 0


class Bird:
    def __init__(self, canvas, window):
        self.canvas = canvas
        self.player_object = self.canvas.create_rectangle(200, 0, 270, 70, fill="gold2")
        self.velocity = 0
        self.window = window
        # self.can_jump = True

    def jump(self, event):
        # if self.can_jump:
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
    def __init__(self, canvas, window, list_of_pipes, bird):
        self.canvas = canvas
        self.pipe_object_top = "placeholder"
        self.pipe_object_bottom = "placeholder"
        self.window = window
        self.list_of_pipes = list_of_pipes
        self.player = bird

    def spawn(self):
        self.list_of_pipes.append(self)
        x_location = random.randint(275, 750)
        self.pipe_object_top = self.canvas.create_rectangle(810, x_location, 880, 900, fill="green2")
        self.pipe_object_bottom = self.canvas.create_rectangle(810, x_location - 270, 880, 0, fill="green2")

    def move_pipe(self):
        self.canvas.move(self.pipe_object_bottom, -2, 0)
        self.canvas.move(self.pipe_object_top, -2, 0)

    def destroy_pipe(self):
        if self.canvas.coords(self.pipe_object_top)[2] < -44:
            self.canvas.delete(self.pipe_object_bottom, self.pipe_object_top)
            self.list_of_pipes.pop(0)
            return True
        else:
            return False

    def collision(self):
        pass


def main():
    window = Tk()
    canvas = Canvas(window, width="800", height="800", background="sky blue")
    canvas.pack()
    list_of_pipes = []
    player = Bird(canvas=canvas, window=window)
    pipe = Pipe(canvas=canvas, window=window, list_of_pipes=list_of_pipes, bird=player)
    pipe.spawn()
    pipe_counter = 0
    while True:
        pipe_counter += 1

        if pipe_counter == 200:
            new_pipe = Pipe(canvas=canvas, window=window, list_of_pipes=list_of_pipes, bird=player)
            new_pipe.spawn()
            pipe_counter = 0

        for x in range(len(list_of_pipes)):
            list_of_pipes[x].move_pipe()
            if list_of_pipes[x].destroy_pipe():
                break   # potential bad coding practice, maybe fix?

        canvas.after(1)
        player.velocity += 0.8
        player.compile_movement()
        canvas.update()

  
if __name__ == '__main__':
    main()
