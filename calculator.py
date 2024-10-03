from tkinter import *
import math

# Function to handle basic arithmetic operations and logging
def onClick(event):
    text = event.widget.cget("text")
    try:
        if text == "=":
            if screenVal.get().isdigit():
                screenVal.set(int(screenVal.get()))
            elif "^" in screenVal.get():
                temp = screenVal.get().split("^")
                result = math.pow(int(temp[0]), int(temp[1]))
                screenVal.set(result)
                screen.update()
            else:
                log = screenVal.get()  # Save expression for logging
                result = eval(screenVal.get())
                screenVal.set(result)
                screen.update()
                # Log the calculation result
                with open("calLog", "a") as file:
                    file.write(f"{log} = {result}\n")
        elif text == "c":
            screenVal.set("")
            screen.update()
        else:
            screenVal.set(screenVal.get() + text)
            screen.update()
    except ZeroDivisionError as zd_error:
        screenVal.set("Error: Division by Zero")
        screen.update()
        print(zd_error)
    except Exception as e:
        screenVal.set("ERROR")
        screen.update()
        print(e)

# Function to handle advanced mathematical operations
def advncMath(event):
    text = event.widget.cget("text")
    try:      
        if screenVal.get().isdigit():
            if text == "sqrt":
                result = math.sqrt(int(screenVal.get()))
                screenVal.set(result)
                screen.update()
            elif text == "cos":
                result = math.cos(math.radians(int(screenVal.get())))
                screenVal.set(result)
                screen.update()
            elif text == "sin":
                result = math.sin(math.radians(int(screenVal.get())))
                screenVal.set(result)
                screen.update()
            elif text == "tan":
                result = math.tan(math.radians(int(screenVal.get())))
                screenVal.set(result)
                screen.update()
            elif text == "log":
                result = math.log10(int(screenVal.get()))
                screenVal.set(result)
                screen.update()
            elif text == "ln":
                result = math.log(int(screenVal.get()))
                screenVal.set(result)
                screen.update()
            
        else:
            screenVal.set("ERROR: Input Number First")
            screen.update()
        with open("calLog", "a") as file:
            file.write(f"{result}\n")
    except Exception as e:
        screenVal.set("ERROR")
        screen.update()
        print(e)

# Create main window
root = Tk()
root.minsize(600, 800)  # Set minimum window size
root.maxsize(600, 800)  # Set maximum window size
root.title("Calculator by Fahad Riaz")  # Set window title
root.iconbitmap("calcIcon.ico")  # Set window icon
root.configure(bg='#f3f4f6')  # Set background color of the window

# Screen widget to display input and results
screenVal = StringVar()
screen = Entry(root, textvariable=screenVal, font="consolas 40 bold", relief=SUNKEN, bg="#ffffff", fg="#333333")
screen.grid(row=0, column=0, columnspan=5, padx=20, pady=20)

# Frames for organizing buttons
f1 = Frame(root, bg="#ffffff")
f2 = Frame(root, bg="#ffffff")
f3 = Frame(root, bg="#ffffff")
f4 = Frame(root, bg="#ffffff")
f5 = Frame(root, bg="#ffffff")

# Place frames using grid layout
f1.grid(row=1, column=0, columnspan=5, sticky="nsew")
f2.grid(row=2, column=0, columnspan=5, sticky="nsew")
f3.grid(row=3, column=0, columnspan=5, sticky="nsew")
f4.grid(row=4, column=0, columnspan=5, sticky="nsew")
f5.grid(row=1, column=4, rowspan=4, sticky="ne")

# Configure grid columns and rows to expand properly
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=0)

# Create buttons in f1-f4 frames using grid layout
button_style = {'padx': 25, 'pady': 20, 'font': 'arial 15 bold', 'relief': GROOVE, 'width': 2, 'height': 1, 'bg': '#e2e2e2', 'activebackground': '#c9c9c9'}

for i, val in enumerate(["9", "8", "7", "+", "-"]):
    b = Button(f1, text=val, **button_style)
    b.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")
    b.bind("<Button-1>", onClick)

for i, val in enumerate(["6", "5", "4", "/", "*"]):
    b = Button(f2, text=val, **button_style)
    b.grid(row=0, column=i, padx=10, pady=0, sticky="nsew")
    b.bind("<Button-1>", onClick)

for i, val in enumerate(["3", "2", "1", "%", "c"]):
    b = Button(f3, text=val, **button_style)
    b.grid(row=0, column=i, padx=10, pady=0, sticky="nsew")
    b.bind("<Button-1>", onClick)

for i, val in enumerate(["0", ".", "00", "^", "="]):
    b = Button(f4, text=val, **button_style)
    if val == "=":
        b.config(bg="lightblue")  # Change background color for "=" button
    b.grid(row=0, column=i, padx=10, pady=0, sticky="nsew")
    b.bind("<Button-1>", onClick)

# Create advanced math buttons in f5 frame using grid layout
for i, val in enumerate(["sqrt", "cos", "sin", "tan", "log", "ln"]):
    b = Button(f5, text=val, font="arial 15 bold", padx=25, pady=20, bg="#007bff", fg="white", relief=GROOVE, width=2, height=1)
    b.grid(row=i, column=0, padx=5, pady=5, sticky="nsew")
    b.bind("<Button-1>", advncMath)

root.mainloop()
