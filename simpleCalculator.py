import tkinter as tk

root = tk.Tk()
root.title("simpleCalculator")

def button_press(symbol):
    if symbol == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

entry = tk.Entry(root, font=("Arial, 18"))
entry.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 10)

#Makes the symbols on the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+' ]

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

