import tkinter as tk
import turtle
import math


def draw_triangle(*args):
    
    # Get sides from entry fields
    side1 = side1_entry.get()
    side2 = side2_entry.get()
    side3 = side3_entry.get()

    # Auto positions to next entry field after inputting a value
    if side1 == "":
        side1_entry.focus()

    elif side2 == "":
        side2_entry.focus()

    elif side3 == "":
        side3_entry.focus()

    else:
        
        try:
            side1 = float(side1)
            side2 = float(side2)
            side3 = float(side3)

            # Store original sides for error message
            orig_side1, orig_side2, orig_side3 = sorted([side1, side2, side3])

        except ValueError:
            result.config(
                font=("Arial", 10, "bold"),
                text="Invalid input. Please enter a valid number.",
                fg="red",
            )
            return
        # Size if Input is too small or large
        try:
            if side1 < 10 and side2 < 10 and side3 < 10:
                scale = 8
                side1 *= scale
                side2 *= scale
                side3 *= scale

            elif side1 > 200 or side2 > 200 or side3 > 200:
                scale = 0.5
                side1 *= scale
                side2 *= scale
                side3 *= scale
        except ValueError:
            result.config(
                font=("Arial", 10, "bold"),
                text="Invalid input. Please enter a valid number.",
                fg="red",
            )
            return
        # Sorted for the Longest side
        sides = sorted([side1, side2, side3])

        # Check for Zero
        if 0 in sides:
            result.config(
                font=("Arial", 10, "bold"),
                text=f"Invalid Triangle...\n\nSide Cannot be Zero!",
                fg="red",
            )
            return

        # Triangle checking
        if not (sides[0] + sides[1] > sides[2]):
            result.config(
                font=("Arial", 10, "bold"),
                text=f"Invalid Triangle...\n\n{orig_side1} + {orig_side2} does not exceed {orig_side3}",
                fg="red",
            )
            return

        # Calculate angles
        try:
            A = math.degrees(
                math.acos(
                    (sides[1] ** 2 + sides[2] ** 2 - sides[0] ** 2) / (2.0 * sides[1] * sides[2])))

            B = math.degrees(
                math.acos(
                    (sides[0] ** 2 + sides[2] ** 2 - sides[1] ** 2) / (2.0 * sides[0] * sides[2])))

            C = math.degrees(
                math.acos(
                    (sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) / (2.0 * sides[0] * sides[1])))

        except ValueError:
            result.config(
                font=("Arial", 10, "bold"),
                text=f"Invalid Triangle...\n\n{orig_side1} + {orig_side2} does not exceed {orig_side3}",
                fg="red",
            )
            return

        else:
            # Right checking
            if A <= 90.5 and A >= 89.5:
                result.config(
                    font=("Arial", 10, "bold"),
                    text=f"Right Triangle\nThe provided side lengths adhere to the Pythagorean Theorem\n\n{orig_side1}\u00B2 + {orig_side2}\u00B2 = {orig_side3}\u00B2",
                    fg="green1",
                )
                color = "green1"
                
            elif B <= 90.5 and B >= 89.5:
                result.config(
                    font=("Arial", 10, "bold"),
                    text=f"Right Triangle\nThe provided side lengths adhere to the Pythagorean Theorem\n\n{orig_side1}\u00B2 + {orig_side2}\u00B2 = {orig_side3}\u00B2",
                    fg="green1",
                )
                color = "green1"

            elif C <= 90.5 and C >= 89.5:
                result.config(
                    font=("Arial", 10, "bold"),
                    text=f"Right Triangle\nThe provided side lengths adhere to the Pythagorean Theorem\n\n{orig_side1}\u00B2 + {orig_side2}\u00B2 = {orig_side3}\u00B2",
                    fg="green1",
                )
                color = "green1"

            elif sides[0] == sides[1] == sides[2]:
                result.config(
                    font=("Arial", 10, "bold"),
                    text=f"Equilateral Triangle\nAll three sides are equal.\n\n{orig_side1} = {orig_side2} = {orig_side3}",
                    fg="gold",
                )
                color = "gold"

            else:
                result.config(
                    font=("Arial", 10, "bold"),
                    text=f"NOT Right Triangle\nThe provided side lengths do not satisfy the Pythagorean Theorem\n\n{orig_side1}\u00B2 + {orig_side2}\u00B2 is not equal to {orig_side3}\u00B2",
                    fg="red",
                )
                color = "firebrick1"

            # Check if the turtle graphics window is still open, then CLEARS the Screen
            if turtle.getscreen() is not None:
                turtle.clearscreen()  # Clear the screen

            # Turtle global
            global screen
            screen = turtle.Screen()
            screen.title("Triangle Drawer")
            screen.bgcolor("#00425A")
            screen.setup(783, 500, startx=495, starty=0)

            screen.cv._rootwindow.protocol("WM_DELETE_WINDOW", exit_event2)

            global board
            # Color
            board = turtle.Turtle()
            board.fillcolor(color)
            board.pencolor("white")
            board.begin_fill()
            board.pendown()

            # Calculate vertices of the triangle
            x0, y0 = 0, 0
            x1, y1 = sides[1], 0
            x2, y2 = sides[1] * math.cos(math.radians(C)), sides[1] * math.sin(
                math.radians(C)
            )

            # Move to the starting point
            board.goto(x0, y0)

            # Draw the triangle
            board.goto(x1, y1)
            board.goto(x2, y2)
            board.goto(x0, y0)

            # Text will be below the Center of the Triangle
            x_center = (x0 + x1 + x2) / 3
            y_center = -50

            # Move the turtle to the centroid
            board.penup()
            board.goto(x_center, y_center)

            # Define the conditions for each type of triangle
            is_right = (
                A <= 90.5
                and A >= 89.5
                or B <= 90.5
                and B >= 89.5
                or C <= 90.5
                and C >= 89.5
            )
            is_equilateral = sides[0] == sides[1] == sides[2]

            # Set the color and write the type of triangle
            if is_right:
                board.pencolor("green1")
                triangle_type = "Right Triangle"

            elif is_equilateral:
                board.pencolor("yellow")
                triangle_type = "Equilateral Triangle"

            else:
                board.pencolor("firebrick1")
                triangle_type = "NOT Right Triangle"

            # Write
            board.pendown()
            board.write(triangle_type, align="center", font=("Arial", 12, "bold"))

            # Close the turtle graphics window
            board.end_fill()
            board.hideturtle()
            screen.cv._rootwindow.protocol("WM_DELETE_WINDOW", exit_event2)
            screen.cv._rootwindow.bind("<F11>", toggle_fullscreen1)
            window.protocol("WM_DELETE_WINDOW", exit_event3)


# tkinter window
window = tk.Tk()

# Title
window.title("Right Triangle Checker")

# Size
window.geometry("500x320+-6+0")
window.configure(bg="#00425A")

# Columns
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)

# Labels (stick='we' will center)
introframe = tk.Frame(window, bg="#1F8A70", width=50, height=50)
introframe.grid(column=0, row=0, columnspan=2, sticky="n")
intro = tk.Label(
    introframe,
    bg="#FC7300",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=16,
    text="This program takes the three side lengths of a triangle then determines\nwhether it's a Right Triangle in accordance to the Pythagorean Theorem.",
)

intro.grid(column=0, row=0)

spacer2 = tk.Label(window, bg="#00425A", text="")  # Blank Line
spacer2.grid(column=0, row=1)

labelframe1 = tk.Frame(window, width=50, height=50)
labelframe1.grid(column=0, row=2, sticky="we")

label1 = tk.Label(labelframe1, bg="#ECF8F9", pady=8, font=("Arial", 10), text="   Side 1:  ")
label1.grid(column=0, row=2)

labelframe2 = tk.Frame(window, width=50, height=50)
labelframe2.grid(column=0, row=3, sticky="we")

label2 = tk.Label(labelframe2, bg="#ECF8F9", pady=8, font=("Arial", 10), text="   Side 2:  ")
label2.grid(column=0, row=3, sticky="we")

labelframe3 = tk.Frame(window, width=50, height=50)
labelframe3.grid(column=0, row=4, sticky="we")

label3 = tk.Label(labelframe3, bg="#ECF8F9", pady=8, font=("Arial", 10), text="   Side 3:  ")
label3.grid(column=0, row=4, sticky="we")

label3 = tk.Label(labelframe3, bg="#ECF8F9", pady=8, font=("Arial", 10), text="   Side 3:  ")
label3.grid(column=0, row=4, sticky="we")

# ENTRY FIELDS
side1_entry = tk.Entry(window)
side1_entry.grid(column=1, row=2, sticky="we")

side2_entry = tk.Entry(window)
side2_entry.grid(column=1, row=3, sticky="we")

side3_entry = tk.Entry(window)
side3_entry.grid(column=1, row=4, sticky="we")

spacer2 = tk.Label(window, bg="#00425A", text="")  # Blank Line
spacer2.grid(column=0, row=5)


# Button Hover Functions; e = <key> as the argument
def on_enter(e):
    draw_button["background"] = "#E55807"  # Color when mouse is hovered on the button
    draw_button["foreground"] = "white"


def on_leave(e):
    draw_button["background"] = "#FC7300"  # Original color
    draw_button["foreground"] = "black"


def on_press(e):
    draw_button["background"] = "#E55807"  # Color when button is clicked
    draw_button["foreground"] = "white"


def on_release(e):
    draw_button["background"] = "#FC7300"  # Color when button is released
    draw_button["foreground"] = "black"


draw_button = tk.Button(
    window,
    bg="#FC7300",
    text="Draw Triangle",
    command=draw_triangle,
    activebackground="#FC7300",
)

# Create a Button that will Draw the Triangle
draw_button.grid(column=0, row=6, columnspan=2, sticky="we")

# Draw Button Hover Function Call
draw_button.bind("<Enter>", on_enter)
draw_button.bind("<Leave>", on_leave)
draw_button.bind("<Button-1>", on_press)  # Button 1 = Left Click
draw_button.bind("<ButtonRelease-1>", on_release)

# For the use of Enter Key
window.bind("<Return>", draw_triangle)

spacer3 = tk.Label(window, bg="#00425A", text="")  # Blank Line
spacer3.grid(column=0, row=7)

# Displays the Results
result = tk.Label(window, bg="#1F8A70", text="")
result.grid(column=0, row=8, columnspan=2, sticky="we")

spacer4 = tk.Label(window, bg="#00425A", text="")  # Blank Line
spacer4.grid(column=0, row=9)


# For exit window
def exit_event1():
    exitmsg = tk.messagebox.askquestion(
        "Quit?", "Are you sure you want to exit the app?", icon="warning"
    )

    if exitmsg == "yes":
        window.destroy()

    else:
        pass


def exit_event2():  # Ask for exit confirmation
    exitmsg = tk.messagebox.askquestion(
        "Quit?", "Are you sure you want to exit the app?", icon="warning")

    if exitmsg == "yes":
        window.destroy()
        board.getscreen().bye()

    else:
        pass


def exit_event3():
    exitmsg = tk.messagebox.askquestion(
        "Quit?", "Are you sure you want to exit the app?", icon="warning")

    if exitmsg == "yes":
        window.destroy()
        if board.getscreen() is not None:
            board.getscreen().bye()
    else:
        pass


# Make it toggle fullscreen
def toggle_fullscreen(event=None):
    state = not window.attributes("-fullscreen")
    window.attributes("-fullscreen", state)


def toggle_fullscreen1(event=None):
    state = not screen.cv._rootwindow.attributes("-fullscreen")
    screen.cv._rootwindow.attributes("-fullscreen", state)


# Bind F11 key to toggle_fullscreen function
window.bind("<F11>", toggle_fullscreen)

# Window maximize disabler
window.resizable(False, False)

# NO EXIT
window.protocol("WM_DELETE_WINDOW", exit_event1)

# Run the program
window.mainloop()
