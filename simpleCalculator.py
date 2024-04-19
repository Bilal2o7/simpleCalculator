import tkinter as tk

root = tk.Tk()
root.title("simpleCalculator")

#Check for button press and acts accordently
def button_press(symbol):
    if symbol == '=':
        expression()
    elif symbol == 'C':
        clear()
    else:
        clear.insert(tk.END, symbol)

def expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str("Result"))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Clears the calcualtor
def clear():
    entry.delete(0, tk.END)

entry = tk.Entry(root, font = ("Arial, 18"))
entry.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 10)

#Makes the symbols on the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+' ]

row = 1
col = 0

Button_widget = []
for button_text in buttons:
    bn = tk.Button(root, text = button_text, font = ("Arial", 18), padx = 20, pady = 10)
    bn.grid(row = row, column = col)

#Erects buttons and gives them size and font
for button in buttons:
    bn = tk.Button(root, text = button, font = ("Arial", 18), padx = 20, pady = 10)
    bn.grid(row = row, column = col)
    
    #First adds columns then stops the column after its reached 3 columns and then starts to add rows
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

