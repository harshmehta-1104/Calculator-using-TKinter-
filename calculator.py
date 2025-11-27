from tkinter import *

# Opening window
window = Tk()
window.title("Simple Calculator")
window.geometry('260x330')
window.resizable(False, False)

# Entry box
entrybox = Entry(window, width=18, borderwidth=5,
                 font=("Arial", 18), justify="right")
entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def click(ch):
    """Append a character (digit or operator) to the entry."""
    current = entrybox.get()
    entrybox.delete(0, END)
    entrybox.insert(0, str(current) + str(ch))


def equal():
    """Evaluate the full expression in the entry box."""
    expr = entrybox.get()
    try:
        # Basic restriction of eval (still not for untrusted input on internet)
        result = eval(expr, {"__builtins__": None}, {})
        entrybox.delete(0, END)
        entrybox.insert(0, str(result))
    except ZeroDivisionError:
        entrybox.delete(0, END)
        entrybox.insert(0, "Divide by 0")
    except Exception:
        entrybox.delete(0, END)
        entrybox.insert(0, "Error")


def clear():
    """Clear the entire entry."""
    entrybox.delete(0, END)


def backspace():
    """Delete last character from entry."""
    current = entrybox.get()
    entrybox.delete(0, END)
    entrybox.insert(0, current[:-1])


# Button configuration: (text, row, column)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("⌫", 5, 1),
]

for (text, r, c) in buttons:
    if text == "=":
        cmd = equal
    elif text == "C":
        cmd = clear
    elif text == "⌫":
        cmd = backspace
    else:
        def cmd(ch=text): return click(ch)

    Button(window, text=text, width=5, height=2, command=cmd).grid(
        row=r, column=c, padx=5, pady=5)


# Keyboard bindings
window.bind("<Return>", lambda event: equal())
window.bind("<BackSpace>", lambda event: backspace())

window.mainloop()
