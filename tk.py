import tkinter as tk
import tksvg

root = tk.Tk()
root.title("Image")

svg_img = tk.PhotoImage(file="img\BTC.png")
label = tk.Label(root,image=svg_img)
label.pack()
root.mainloop()