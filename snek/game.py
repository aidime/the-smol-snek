import snek
import board
try:
    import tkinter as tk  # assume Python 3
except ImportError:
    import Tkinter as tk  # nope, Python 2

test1 = makeBoard(40, 40)


colorMatrix = [[0 for x in range(40)] for y in range(40)]
for x in range(40):
        for y in range(40):
                colorMatrix[x][y] = test1.tiles[x][y].color

#print(colorMatrix)

width, height = 600, 600

root = tk.Tk()
root.title("snek")

frame = tk.Frame()
frame.pack()

canvas = tk.Canvas(frame, width=width, height=height)
rows, cols = len(colorMatrix), len(colorMatrix[0])

rect_width, rect_height = width // rows, height // cols
for y, row in enumerate(colorMatrix):
        for x, color in enumerate(row):
                x0, y0 = x * rect_width, y * rect_height
                x1, y1 = x0 + rect_width-1, y0 + rect_height-1
                canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
canvas.pack()

root.mainloop()