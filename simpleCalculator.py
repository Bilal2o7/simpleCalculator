import tkinter as tk

root = tk.Tk()
root.title("simpleCalculator")

#Makes the symbols on the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 0
col = 0

#Makes the buttons and gives them size and font
for button in buttons:
    bn = tk.Button(root, text=button, font=("Arial", 18), padx=20, pady=10)
    bn.grid(row=row, column=col)
    #First adds columns then stops the column after its reached 3 columns and then starts to add rows
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()