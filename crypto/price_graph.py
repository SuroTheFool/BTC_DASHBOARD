import tkinter as tk
from tkinter import ttk

class PriceGraph(ttk.Frame):
    def __init__(self,parent,width=300,height=120,max_points=100):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.max_points = max_points
        self.prices = []

        self.canvas = tk.Canvas(self,width=self.width,height = self.height, bg="black")
        self.canvas.pack(fill="both",expand=True)
    def add_price(self,price:float):
        self.prices.append(price)
        if len(self.prices) > self.max_points:
            self.prices = self.prices[-self.max_points:]
        self._redraw()
    def _redraw(self):
        self.canvas.delete("all")
        if len(self.prices) < 2:
            return
        min_p = min(self.prices)
        max_p = max(self.prices)

        if max_p == min_p:
            max_p = min_p + 1e-8

        n = len(self.prices)
        # Horizontal spacing between 2 points
        x_step = self.width / (n - 1)

        def price_to_y(p):
            ratio = (p - min_p) / (max_p - min_p)
            return self.height - ratio * self.height
        for i in range(1,n):
            p0 = self.prices[i-1]
            p1 = self.prices[i]
            x0 = (i - 1) * x_step
            x1 = i * x_step
            y0 = price_to_y(p0)
            y1 = price_to_y(p1)

            color = "green" if p1 >= p0 else "red"
            self.canvas.create_line(x0,y0,x1,y1, fill=color, width=2)