import tkinter as tk
import time
import threading

class TsunamiSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("sound wave Simulator")
        self.canvas_size = 640
        self.grid_size = 16
        self.cell_size = self.canvas_size // self.grid_size

        self.canvas = tk.Canvas(self, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()

        self.circle1_radius = 30
        self.circle2_radius = 20

        self.draw_grid()
        self.draw_coastline()
        self.draw_circles()

        self.update_circles()

    def draw_grid(self):
        for i in range(self.grid_size + 1):
            x = i * self.cell_size
            y = i * self.cell_size
            self.canvas.create_line(x, 0, x, self.canvas_size, fill="black")
            self.canvas.create_line(0, y, self.canvas_size, y, fill="black")

    def draw_coastline(self):
        coastline_x = self.canvas_size - 2 * self.cell_size
        self.canvas.create_line(coastline_x, 0, coastline_x, self.canvas_size, fill="blue", width=3)
        self.canvas.create_text(coastline_x + 20, self.canvas_size / 2, text="receiver", angle=90, anchor="w")

    def draw_circles(self):
        center_x = self.canvas_size // 2
        center_y = self.canvas_size // 2

        self.canvas.delete("circles")
        
        self.canvas.create_oval(
            center_x - self.circle1_radius,
            center_y - self.circle1_radius,
            center_x + self.circle1_radius,
            center_y + self.circle1_radius,
            outline="blue", width=2, tags="circles"
        )

        self.canvas.create_oval(
            center_x - self.circle1_radius,
            center_y - 5,
            center_x + self.circle1_radius,
            center_y + 5,
            outline="blue", width=2, tags="circles"
        )

    def update_circles(self):
        self.circle1_radius += 5
        
        if self.circle1_radius > 500:
            self.circle1_radius=20
        
        self.draw_circles()
        self.after(500, self.update_circles)

if __name__ == "__main__":
    app = TsunamiSimulator()
    app.mainloop()

