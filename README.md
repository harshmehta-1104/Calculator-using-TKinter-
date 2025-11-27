# Simple Calculator (Tkinter GUI)

This project is a basic calculator application built using Python's Tkinter library. It provides a graphical user interface (GUI) that allows the user to perform simple arithmetic operations such as addition, subtraction, multiplication, and division.

---

## Description

The calculator opens in a fixed-size window with a display area at the top and buttons arranged in a grid layout below it. Users can enter numbers and operators using the on-screen buttons or the keyboard. The calculator evaluates the full expression shown in the display (for example, `2+3*4`) and shows the result when the user presses the equals button or the Enter key.

The interface includes:

- A display box to show the current input and results  
- Number buttons (`0–9`)  
- Operator buttons (`+`, `-`, `*`, `/`)  
- A decimal point button (`.`)  
- An equals button (`=`)  
- A clear button (`C`) to reset the display  
- A backspace button to delete the last character  
- Keyboard support for Enter (`=`) and Backspace  

---

## Features

- **Graphical User Interface**  
  Uses Tkinter to create a simple, user-friendly calculator window with a button grid.

- **Expression Entry**  
  Users can build full mathematical expressions (such as `12+3*4-5`) directly in the display.

- **Evaluation of Expressions**  
  The app evaluates the complete expression in the display and shows the result.

- **Error Handling**  
  - Shows a specific message when division by zero is attempted.  
  - Shows a generic error message if the expression cannot be evaluated.

- **Backspace Support**  
  Allows the user to delete the last character entered without clearing the entire input.

- **Keyboard Shortcuts**  
  - Pressing Enter triggers evaluation (same as `=`).  
  - Pressing Backspace removes the last character (same as the backspace button).

- **Fixed Window Size**  
  The window size is set and not resizable, which helps keep the layout consistent.

---

## Concepts Practiced

- Creating windows and widgets with Tkinter  
- Using `Entry` widgets as a calculator display  
- Arranging buttons using the `grid` layout manager  
- Handling button clicks through callback functions  
- Working with event bindings for keyboard input  
- Building and manipulating strings to represent expressions  
- Evaluating expressions and handling runtime errors  
- Basic GUI design and user interaction patterns  

---

## Expected Behavior

- When the application starts, a calculator window appears with a display and buttons.  
- Clicking numeric and operator buttons (or using the keyboard) updates the display.  
- Pressing `=` or Enter evaluates the current expression and shows the result.  
- Pressing `C` clears the entire display.  
- Pressing the backspace button or Backspace key removes the last character.  
- If the user attempts an invalid operation (like division by zero or malformed input), an error message is shown instead of crashing.
