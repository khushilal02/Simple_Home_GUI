from tkinter import *

# Create root wndows 
root = Tk()
root.title("Sweet Home")
can = Canvas(root, bg="#091e42", height=700, width="1200")

 #Create house 
can.create_polygon(600, 250, 700, 200, 800, 250, 800, 400, 600, 400, 
        width=2, fill="yellow", outline="red")

can.create_line(600, 250, 800, 250, width=2, fill="red")
can.create_rectangle(650, 275, 750, 375, fill="red")

# Create 3 bushes at left side of house
x1, y1 = 0, 350
x2, y2 = 200, 450

for i in range(3):
    can.create_arc(x1, y1, x2, y2, start=0, extent=180, fill="green")
    x1+=200
    x2+=200

# Create two bushes at right side of house
can.create_arc(800, 350, 1000, 450, start=0, extent=180, fill="green")
can.create_arc(1000, 350, 1200, 450, start=0, extent=180, fill="green")

can.pack()
root.mainloop()

