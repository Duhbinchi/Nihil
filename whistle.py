import tkinter as tk
import turtle
import math
from random import seed, randint

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
            result.config(font = ("Arial", 10, 'bold'), text="Invalid input. Please enter a valid number.", fg="red")

        # Size if Input is too small or large
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

        # Sorted for the Longest side
        sides = sorted([side1, side2, side3]) #100 200 300
        # 


        # Check for Zero
        if 0 in sides:
            result.config(font = ("Arial", 10, 'bold'), text=f"Invalid Triangle...\n\nSide Cannot be Zero!", fg="red")
            return
    
        # Triangle checking
        if not (sides[0] + sides[1] > sides[2]):# 200 200 300
            result.config(font = ("Arial", 10, 'bold'), text=f"Invalid Triangle...\n\n{orig_side1} + {orig_side2} does not exceed {orig_side3}", fg="red")
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
            result.config(font = ("Arial", 10, 'bold'), text=f"Invalid Triangle...\n\n{orig_side1} + {orig_side2} does not exceed {orig_side3}", fg="red")
            return


        else:
            # Right checking
            if A <= 90.5 and A >= 89.5:
                result.config(font = ("Arial", 10, 'bold'), text=f"Right Triangle\nThe provided side lengths adhere to the Pythagorean Theorem\n\n{orig_side1}\u00B2 + {orig_side2}\u00B2 = {orig_side3}\u00B2", fg="green1")
                color = "green1"
            elif B <= 90.5 and B >= 89.5:
                result.config(font = ("Arial", 10, 'bold'), text=f"Right Triangle\nThe provided side lengths adhere to the Pythagorean Theorem\n\n{orig_side1}\u00B2 + {orig_side2}\u00B2 = {orig_side3}\u00B2", fg="green1")
                color = "green1"
            elif C <= 90.5 and C >= 89.5:
                result.config(font = ("Arial", 10, 'bold'), text=f"Right Triangle\nThe provided side lengths adhere to the Pythagorean Theorem\n\n{orig_side1}\u00B2 + {orig_side2}\u00B2 = {orig_side3}\u00B2", fg="green1")
                color = "green1"

            elif sides[0] == sides[1] == sides[2]:
                result.config(font = ("Arial", 10, 'bold'), text=f"Equilateral Triangle\nAll three sides are equal.\n\n{orig_side1} = {orig_side2} = {orig_side3}", fg="gold")
                color = "gold"

            else:
                result.config(font = ("Arial", 10, 'bold'), text=f"NOT Right Triangle\nThe provided side lengths do not satisfy the Pythagorean Theorem\n\n{orig_side1}\u00B2 + {orig_side2}\u00B2 is not equal to {orig_side3}\u00B2", fg="red", )
                color = "firebrick1"

            # Check if the turtle graphics window is still open, then CLEARS the Screen
            if turtle.getscreen() is not None:
                turtle.clearscreen()  # Clear the screen

            # Turtle global
            global screen
            screen = turtle.Screen()
            screen.title("Triangle Drawer")
            screen.bgcolor("white")
            screen.setup(783, 500, startx=495, starty=0)

            screen.cv._rootwindow.protocol("WM_DELETE_WINDOW", exit_event2)
            global board

            # Color
            board = turtle.Turtle()
            board.fillcolor(color)
            board.begin_fill()
            board.pendown()

            # Calculate vertices of the triangle
            x0, y0 = 0, 0
            x1, y1 = sides[1], 0
            x2, y2 = sides[1] * math.cos(math.radians(C)), sides[1] * math.sin(math.radians(C))

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
            is_right = (A <= 90.5 and A >= 89.5 or B <= 90.5 and B >= 89.5 or C <= 90.5 and C >= 89.5)
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



# tkinter window
window = tk.Tk()

# Title
window.title("Right Triangle Checker")

# Size
window.geometry("500x300+-6+0")

# Columns
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)


# Labels (stick='we' will center)
intro = tk.Label(font = ("Arial", 10), text="This program takes the three side lengths of a triangle then determines\nwhether it's a Right Triangle in accordance to the Pythagorean Theorem.")

intro.grid(column=0, row=0, columnspan=2, sticky="we")

spacer2 = tk.Label(window, text="")  # Blank Line
spacer2.grid(column=0, row=1)

label1 = tk.Label(font = ("Arial", 10), text="\u2192 Side 1: ")
label1.grid(column=0, row=2, sticky="we")

label2 = tk.Label(font = ("Arial", 10), text="\u2192 Side 2: ")
label2.grid(column=0, row=3, sticky="we")

label3 = tk.Label(font = ("Arial", 10), text="\u2192 Side 3: ")
label3.grid(column=0, row=4, sticky="we")

# ENTRY FIELDS
side1_entry = tk.Entry(window)
side1_entry.grid(column=1, row=2, sticky="we")

side2_entry = tk.Entry(window)
side2_entry.grid(column=1, row=3, sticky="we")

side3_entry = tk.Entry(window)
side3_entry.grid(column=1, row=4, sticky="we")

spacer2 = tk.Label(window, text="")  # Blank Line
spacer2.grid(column=0, row=5)

# Create a button to draw the triangle
def on_enter(e):
    draw_button['background'] = '#00965C'  # Color when mouse is hovered on the button

def on_leave(e):
    draw_button['background'] = '#00E18B'  # Original color

def on_press(e):
    draw_button['background'] = '#00643E'  # Color when button is clicked

def on_release(e):
    draw_button['background'] = '#00C87B'  # Color when button is released

draw_button = tk.Button(window, bg="#00E18B", text="Draw Triangle", command=draw_triangle, activebackground='#00643E')
draw_button.grid(column=0, row=6, columnspan=2, sticky="we")

draw_button.bind("<Enter>", on_enter)
draw_button.bind("<Leave>", on_leave)
draw_button.bind("<Button-1>", on_press) # Button 1 is Left-Click
draw_button.bind("<ButtonRelease-1>", on_release)

# For the use of Enter Key
window.bind("<Return>", draw_triangle) 

spacer3 = tk.Label(window, text="")  # Blank Line
spacer3.grid(column=0, row=7)

# Displays the Results
result = tk.Label(window, text="")
result.grid(column=0, row=8, columnspan=2, sticky="we")

spacer4 = tk.Label(window, text="")  # Blank Line
spacer4.grid(column=0, row=9)



# For exit window
def exit_event1():
    exitmsg = tk.messagebox.askquestion("Quit?", "Are you sure you want to exit the app?", icon="warning")

    if exitmsg == "yes":
        window.destroy()

    else:
        pass


def exit_event2(): # Ask for exit confirmation
    exitmsg = tk.messagebox.askquestion("Quit?", "Are you sure you want to exit the app?", icon="warning")

    if exitmsg == "yes":
        window.destroy()
        board.getscreen().bye()

    else:
        pass

def exit_event():
    exitmsg = tk.messagebox.askquestion("Quit?", "Are you sure you want to exit the app?", icon="warning")

    if exitmsg == "yes":
        window.destroy()
        if turtle.getscreen() is not None:
            turtle.bye()
    else:
         pass

# To exit using Esc key
window.bind('<Escape>', lambda event=None: exit_event())

# Make it toggle fullscreen
def toggle_fullscreen(event=None):
    state = not window.attributes('-fullscreen')
    window.attributes('-fullscreen', state)


# Bind F11 key to toggle_fullscreen function
window.bind('<F11>', toggle_fullscreen)


# Window maximize disabler
window.resizable(False, False)
# 
window.attributes('-toolwindow', True)

# NO EXIT
window.protocol("WM_DELETE_WINDOW", exit_event1)



import tkinter as tk
from random import seed, randint
import winsound

# seed random number generator
seed(randint(0, 999))

def random_color():
    return f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"

def create_window(color, master, ascii_art):
    win = tk.Toplevel(master)
    win.title("C̶̮̩͓̹͗̎̄̑̈́̃̾̎̂̐͒͘ä̵͖̜͕̼̮̜̣̭͍́̓ͅn̵̝͋́ ̷̦͈̙͓̈́̌̈́̈́̋̓̂̀̕͠͠Y̵̦̬̮̯̮̘̯͍̻̠͙̪̜̣̪͊͛̒̔̈́͗̂̅͘͝͠ǫ̷̛̮̞̗̞̖͉̼̞̯̻͖͔̔͒̐͑̏̔͂ů̵̼͖̞͔̮̟̻͈̩̘̗͒̽̓̕̚ ̷̛̦͇͖̳̥̫́̑͛̎͊͐̀̂͆͂͜b̸̯̈́͊͆̀̓̔̀̃̍̀̕̕ḻ̴̛̛͙͌̉̀̋͌́̍̅̇̓̕͝ờ̴͎̞̻́͋͊̎̈́͗̽͗͂̉̈̈w̶̢̛̩̗̯̙̣̺̗̉̐͂̇͆͑̎͝͝ ̸͕͚̟̠̣͙̯͈͎̠̩̭̥̇͜m̵̨̢̛̤̈́͒̑̊́̚͜y̸̢̠̙͉̠͚̬͑̊̅̓̐͊͜͠͝ ̷̘̗͔̠̯͖̩̟̹̦̭̤̦̠̹͂͗̃̄̍̑̈́̊͑̈́͛̉͘͝ẅ̵̨̛̫̬̯̟͎̖̯͖͙̻͍͔̫́̉͛h̶̨̢̫̦̟̖̰̭̀͒̆̎̑̄̊͊̍̇̋̓̚ͅi̴̛stle baby")
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = randint(0, screen_width - 500)
    y = randint(0, screen_height - 500)
    win.attributes('-disabled', True)
    win.geometry(f"500x400+{x}+{y}")  # Increased window size to fit ASCII art
    win.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable the close button
    win.attributes('-toolwindow', True)  # Make it a tool window
    canvas = tk.Canvas(win, bg=color)
    canvas.pack(fill='both', expand=True)
    
    # Add ASCII art in the middle of the canvas
    ascii_text = canvas.create_text(250, 250, text=ascii_art, fill="black", font=('Courier', 5, 'bold'), anchor='center')
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    return win


# ! ADJUST INDEX; HOW MANY WINDOWS WILL BE OPENED
def schedule_windows(index, master, delay, ascii_art, windows):

    number_of_windows = 3  # Adjust the number of windows you want to open

    if index < number_of_windows:
        color = random_color()
        win = create_window(color, master, ascii_art)
        windows.append(win)
        if delay > 20:  # Set a minimum delay to prevent windows from opening too quickly
            delay -= 400  # Decrease the delay by 100ms each time
        master.after(delay, schedule_windows, index + 1, master, delay, ascii_art, windows)



        # Destroy
        if len(windows) > 1000:
            old_win = windows.pop(0)
            old_win.destroy()

# ASCII art as a string
ascii_art = str("Z?++????????II7$$7$MMMMMMMMMMMMMMMNND8OZ$$777IIII??????+++++++++======+++=++=++????I7Z8ZIII$77$$8MMMMMMMNMNNI?????????????????+?+++?+++++++++++??+++++++++++++$M\nZ+??++++??????III77Z8NNNNNNNNNNNNNDDD8OZ$$7II?????????++++++++++++++++++??+7+I$Z8OD8O8DNN8O$$$77$8NNNNDNNDI7??+++++++++++++++++++++++++++++++++++++++++++++++?$M\nZ+?+++++??+++????I7$8NNNNNNNNNNNNNNDDD8OZ$I7I?I?+???++++?+++++++++++++++=78DNNDNNDNO$OOO8NDN8Z$77ONNNNNNND7?I?+++++?+??I+?++++++++++++++++++++++++++++++++++++$M\nZ??+++++??+++???II7ODNNNNNNNNNNNNDDDD8$7Z$7IIIII????++????++++++++???IIZONNNNNNO$$$7$ZZ88$88Z$$7ZNNNNNNN$7??+++++++++++??+O+?+?++++++++++++++++++++++++++++++$M\nZ???++????++++????IIZDNNNNNNNNNNNNDDDDOODNDNN8D88D8DN8$O7I???????+??I7$ODDDDNDDND8NNDNDOOZ88OZ$$7$NNNNN8OI$??+++++++++8?I?DNZ++++++++++++++++++++++++++++++++?$M\nZ??+??????+++++????I$ONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN8Z77??????I7ZDDDODN8DDMMNDOOZDNN8OZZZZ$7$DNNNZZ$+7?+?+++++?+IMN$=NN=D=+++?+++++++++???????++?++???+++$M\nZ??+????????+??????I$$DNNNNNNNNNNNNNNNNNNNNNNNNNDNMNNNNDNNNDZI??+++?I$OZ7OZD8NNNNNM8NNDD88OZ7$$7778NNN7II+7??+???++????N=???7N+8I??+??????????????????????????$M\nZ??+???????????????I77DNNNNNNNNNNNNNNNNNNNNNNNNNMN8DMNNNNNNN87+++++?I7$7?+8$=ZNNNM$77DNDZOZ777$$7$8NNNZII=$+?+????+?????8DDD$NDNNI+???????????????????II??????$M\nZ??????????????????II78ODNNNNNNNNNNNNNNNNNNNNNNDNDNDM$ONOZ8N88?++++?7II+=?+??IIII$OZOOOOI7IIII77I7ONN8Z?+I7?++????+?????ND?ONNNNNII????????I??IIIIIIIIIII?IIIIZM\nZI?III?????????????IIZ8ONNNNNNNNNNNNNNNNNNNNNN$$I8$?I??77I?788$I+++??I??+??I$Z$$$$ZZ7IIII??IIIII77$NO7$I+$I+++????++?+?+NN???NODN7IIII77II777IIIII7777777$7$$7OM\nOII7777III????????II$ONNNNNNNNNNNNDDND8DDDNDNNDDOZ7I?777I?I7ZO7I+++?I7I????????IIII??????????II777ONI$I++$?++???????????ZN$II788DO$77777$$$Z$$$$$$$$$ZZZZZZZZO8N\nD$7$7777IIIIIIIIIIII87?7DNNNNNNNNNNDD8OOZ$O8O888ZZ$Z7I?I??I$Z$7?++=+?III??++++++????????????III77$OZOI?7$I?++???????IIIIIDNI7I7ZDN$7$$$ZZZOOOO88888888888888DDNM\nD8$$$$$77777777777$7DI7$8NNNNNNNNNDDD8Z$7I7I77777I??II????I7Z$$7?+=+?III???++++++++++++?+???III77ZO$I+I77I+++????IIII77I$$NDDZO8NNNDOO888888DDDDDDDDDDDDDDDDDNNM\nN8888ZOOOOOOOZZZZOZ$DI+7NNNNNNNNNNNDD8ZZ77II?III?????????I7$ZZ$7?+=+?IIII??++++++++++????????I77$ZNZ+?I?7I+++???III7$Z$ZOO8NNNNNNNNNNDDDDDDDDNNNNNND8ZZZZ$$$$$8N\nMDNNNDDNNNNNDDDDDD8N87Z8NNNNNNNNNNNND8OZ$7II?????????????I7$ZZZ7??+?+?III?+++++++++++???????II77ZOD7I+??$?++?????I7$ZO8DDDNNNNO$77II???????????++????????????IZM\nMNNNNNNNNNNNNNNNNDDD8$88NNNNNNNNNNNNN8OOZ77I????I???????II7Z7$$???++??I?II??+++++++++???????I?7$O8O?II77I???????I7Z8NDD8$7I?IIIIII????????II????I????????????IZN\nMNNNNNNNNNNNNNNNNNDOZ8DNNNNNNNNNNNNNNDOOZ$7III????????????7$$Z7??+++++??I???+++++++++???????II7$OO8I?ODOI???7ZZODND8OZOZZ$$$777777IIIIIIIIIIIIIIIIIIIIIIIIIIIIZM\nMNNNNNNNNNNNNND8Z888ONNNMNNNNNNNNNNNND8OZ$7III???????????I$77ZII?+++++??I???+++++++++??????II7$OOONNNDO$I??IZNDNNNDNNDDD888OOZZZZ$$$$$77777777777777777777777$OM\nMNNNNNNNNNNNNNNNDDDN8NNNNNNNNNNNNNNNNDOZ$$7III??????????+I$I7$II?++=++??II?I+++++++++??????II7ZOZONNDN$77II$NNNNNNNNDNNDDDDD8888OOOZZZZ$$$$$$$$$$$$$$$$$$$$$Z$OM\nMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN8OZ$77IIII???????+?IZ7ZIII?++=+?II777I+++++++++???????77$Z$8DNNDZ$7$8NNNNNNNNNNNNNNNNNNNNDDDDDD8888888OOOOOOOOOOOOOOOO88DN\nMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDDO$$7IIII???????I?7DOODD8$II??$DDD8NI+++++?????????II7$$$$8NNDOOODNNNNNNNNNNNNNNNNNNNNNNNDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDNM\nMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDZ$$77IIIII??????$DNNDNNND888DDNND7????++?????????I77777$ONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDDDDNNNNM\nMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN8O$$777III?????II$8NNNNNDDDNDOO7???????+???????I777III77ONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNM\nMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDDD8Z$$777II??????III$$8O8NND8I???++????????????II7IIIIII7ZNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMM\nMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDDD8OZ$$7IIIIIIIIIII?IIII$$$$???+?+?I???+???IIII7IIIII?I7ZNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDDNNNNZN\nMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDD888Z$$$7I777I77III????+++?++++????II$OO7????II7III???I7ONNNNNNNNNNNNNNNNNNNDDDDDDDDDDDDDDDDNNNNNNNNNNNNNNNNNNNDNN8=+ZN\nMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDD8OO88ZZ$77$Z88DDZ$ZODNNDO$7ONNNNNNDNNOI?II+??77$II???II7ONNNNNNNNNNNNNNDD8OOOOOOOZZOOOOOOOO88DDDDDDDDDDDNNNNNDN8?????ZN\nNDD88888DDNNNNNNNNNNNNNNNNNNNNNNNNNNNNNND8OO8D8Z77?$$$$ONNDNNNNDNNNNDZ7$$?I7II???????I77II??III7ZDNNNNNNNNNDD8OOZ$$$77777777777777$$$$ZZZOO8O8888DDDDNN?+++???$M\nDZZZZZZZOO88DDNNNNNNNNNNNNNNNNNNNNNNNNNND8OOO8DDZ7?????I77$$77I???I?+??II?II?+?????II777???II77$ONNNNNNNND8O$$777IIIIIIIIIIIIIIIIIII7III777$$ZZOOO888D+?+++???$M\nO7$7$Z7$$$Z$ZO88DDNDNNNNNNNNNNNNNNNNNNNNDD8OZO8DDZ7?I77II7I777III????III?I??II????III7III?III7ZO8NNNNDDD8Z$$7IIII?????II??????????+++++??I?+++++++++??+++?++?+ZM\nO???$7I777I777$ZOO8888DDDDDDDNNNNNNNNNNNNDD8OO88D8Z7I7II777$$$$$7ZZZZ7I7IIIII???IIIII7IIIIII7O8DD$NNDDOZ$77II?I??????I7I?+++++++++++?II??$?+++++++??+????????+ZM\nZ???+??+II$Z7I????$OOOO88O8DNNNNNNNNNNNNNNND8OOO88O$77III7II7$777IIII??????????IIIIIIIIIII7$O8D8887DOZ$7IIII???????7?+++++I+++++++????++?7+++++++++?+++??+???+ZM\nZI????$?????=D?=+?????I???II7I$Z8NNNNNNNNNNNDD8OO88O$777IIIIIIII?????????????????I?III7I77Z8DNNDDZ?Z$7IIII??????+II?+++++?I?++++++????+++?++++++++??+++++?????ZM\nZ?7+???7????+IZ$?+???+I???????II7$8DNNNNNNNNNNNDD8OOZ$77I7IIII?????++++++??????????III77$ODNNNDDNIIIII??????++==II?++++++?I?+++++++++++++?++++++++I++++++?????ZM\nZ????++7+???+?+?I++I++I++????IIII$Z8NNNNNNNNNNNNDDDOO$$777III???????++++++?????????I77$ZDDNNN8DDOI7I7??I?++++++II?=++++++II?+++++++++II?+?+++++++?+++++++?????ZM\nZ?I+??+I++???+??D+?????????+?I??I7$8NNNNNNNNNNNNNDDD8OZ$777I???+?+++++++++???????II7$ODNNNNNDDD$I7IIII+?$I++++?I+++++++++I?++++++++???++??+++++++?++++++??????ZM\nZ?I++++?+???+?+?ZI+????????+?????7$8NNNNNNNNNNNNNNNDDD8O$$77II??+?????+++???????II7Z8DNNNNNDNO?III??I7?+O77?=I??++++++++?I++++++++???+++?+++++++I?++??++??????ZM\nZ?I++++++?????I??7I??++++??+??II?I$8NNNNNNNNNNNNNNNNNND8Z$7III??+??????+????I???I$Z8NNNNNNNDD??II??II$?=O$$$II?+++++++++?I++++++??+++++?++++++++I+++??++??????ZM\nZ?7+++++?+++?????N7?+++++??????III$ONNNNNNMNNNNNNNNNNNNNNOO$$I???+??I??????II77$Z8DNNNNNDNN7???????II7?+$$ZI??++++++++++I?+++++++++++??++++++=++7++?++++??????$M\nZ?I+++++???++?????N7?+++++??????II7DNNNNNNMNNNNNNNNNNNNNNNNOZZ77IIII77I77777$Z88NDNNNNNNN7??+?++??II7I7I+I$+?++++++++++???+++++++++++??++++++==DI+??+?????????$M\nZ??+++++I++??????ION?++?++??????I$$NNNDNNNNNNNNNNNNNNNNNNNNDDDDD8888DDDD888DNNNNNNNNNNDOI++++++???IIII7?++??++++++++++???+++++++++++++++++++?+8I++??++????????$M\nZI?+++++I++??????+?D8?+++++??+??IDNNNNNDNDNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDDDNNNNNNNNNNZ???+++++++???????++?++++++?+++++??+++++++++++++++++++++?I+++??++????????$M\nZ7?+++++I++??????++$N7???++??++?7NNNNNND8NNNNNDNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMNNOII?+++++++++++??II+++?++++++?++++?I+++++++++++++++++++++?8++++++++????????$M\nZ$?+?+++7+++????+++?N8I+?+++????INNNNNNDOONDNDDDDDDNNNNNNNNNNNNNNNNNNNNNNNNNNMNNN87II?+++++++++?????I?++?+++++??+++++I?+++++++++++++++++++++7?++++?+??????????ZM\nZI?+??+?7+++??+++++?ZMII++++????INNNNNNN$7NND8888OO8DNNNNNNNNNNNNNNNNNNNNNNNNNN87I??++++++++++??????II+?++++++??+++++I+++++++++++++++++++++?Z?++++?++???I?????ZM\nO?I???+?$?++??+++++??NZ7I+++????INNNNNN87I8DOOZOOZZ$Z88DNNNNNNNNNNNNNNNNNNNNDZ77I???++++++++++?????I?7??+++++???++++???+++++++????++++++++?????+++I++???I?????ZM\nO????+?+Z??+?+++++++?ON8I?++?+?IIDINZDND7II8OZZZZ$$$$$ZZ8DNNNNNNNNNNNNNNNNDO$7?????++++++++++????????N??++++????++++I?++++++++????+++++++??Z+?++++I++???I?????ZM\nZI?????+Z?++++++++??+INNI?++?????7?$ZZDN7?+IOZ$$$77$$$7$$ZOODNNNNNNNNNN8D$7I?????++++++++++++?????+???+++++?????++++?++++++++????+++++++++?I+?++?+I++???I??II?ZM\nZ???????Z?++++++++?++?DNZ??+++??II?I7$ON$??+7Z$$77777777777777DDDNNZ$DNNNMZI+?+??+++++++++++???+++++7?+++++?I??++++?++++++++++???+++++++++7++?++I+I++???II???IZM\nZ???????Z??+++++++?++?ONDI?++????III778N7????$$$77777IIIIIII$NDNZNDMNND88MDM++?~=+++++++++++??++++++O++++++?I??++++I?++++++++++??++++++??7$++?++I+??+???II??IIZM\nZ???II??Z??+++++++?++?7OD7?++????I????7D$I???I$7777IIIIIII?IDM78DNND8NNNNNDMND++++++++++++++?+++++?I+?+++??II?++++?++++++++??++++++++?II?II++?++I++??????I?IIIZM\nZ????I?I8?+?+++++??????$NZ?++????I????IZ$??++?IIIIIII?I???7DMND7DZNNNNNNNDNNMN8M+++?=++++++++++++++$?++++?II??++++I?+++++++??+++++++?I????7?+I+??+?I?+?I?7?IIIZM\nZ???II?I8?+?????+++++???DDI+?++??I????I?8???+?IIII?I??I7?INMNNNNDNNNNNNMNNNNMNDMM?+??+++++++++++++?+++++??7I?+++++?++++++++?+++++++?I?++II???I++??I7?I??I7II77ZM\nZ???III7DI+??????++++???$N7+?++??I????+IN?+?+?????????II+NNNMNNNNNNNNNNNNNNNNMDMNNN==+++++++++++++$+++++?II?++++???+++++++++++++++I77+?+$7..~=+=:?~~=~+~~++?7$OM\nZI?I7I77N7+++++++?+++???$DZ??+++???+?+?IO????+???I???I??MNNMNNNNNNNNNNNNNNNNNNNNNNNMI++++++++?+++??++++?III?++++=?++++++++++++++?I77?+???777I$II+$$77III7$$II$OM\nZI?I7777NII?????????????I88I??????????+?7????????I??I?NMNMMNNNNNNNNNMMMMMMMMMMMMMMNNM$++++++++++?7++++?I7I????++?I++++++++++++++?77?????$?77?7?77II?IIIII77$8\nMMMMMMNNNMMMMMMMMMMMMMMMMNMMMMMMMMMNMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMNMMNMMMMMMMMMNMNMMMMMMMMMMMMMMNNMNMMMMMMMMMMMMMMMMMMMNMMMMMMMMMNMMMNMMMMMMMMMMN\n")

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Start scheduling the windows with an initial delay
initial_delay = 2000  # Start with a 1-second delay
windows = []
root.after(initial_delay, schedule_windows, 0, root, initial_delay, ascii_art, windows)

# Start the Tkinter event loop
root.mainloop()


# Run the program
window.mainloop()
