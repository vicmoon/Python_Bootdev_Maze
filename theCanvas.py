from tkinter import Tk, BOTH, Canvas
from shapes import Line

class MyWindow():
    def __init__(self, width=870, height=600):
        self.root = Tk()
        self.root.title("Maze")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.shapes = []
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False # Flag to control the main loop
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        

    def redraw(self):
        self.canvas.delete("all")
        for shape, color, w in self.shapes:
            shape.draw(self.canvas, color,w)
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()


    def close(self):
        self.running = False
       
    
    def draw_line(self, line: Line, fill_color="black", width=1):
        self.shapes.append((line, fill_color, width))
        line.draw(self.canvas, fill_color, width)
    