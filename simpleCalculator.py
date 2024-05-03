import tkinter as tk
import math

class Caluclator:
    def __init__(self, root):
        self.root = root
        self.root.title("simpleCalculator")
        
        self.entry = tk.Entry(root, font = ("Arial", 20))
        self.entry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

        self.buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+', "sq", "^"
        ]

        self.create_buttons()

    def create_buttons(self):
        row = 1
        col = 0
        for button_text in self.buttons:
            btn = tk.Button(self.root, text = button_text, width = 5, height = 2, font = ("Arial", 18),  command = lambda b = button_text: self.button_press(b))
            btn.grid(row = row, column = col, padx = 5, pady = 5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_press(self, symbol):
        if symbol == '=':
            self.evaluate_expression()
        elif symbol == 'C':
            self.clear_entry()
        else:
            self.entry.insert(tk.END, symbol)

    def evaluate_expression(self):
        try:
            expression = self.entry.get()
            expression = expression.replace("^", "**")
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, (result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def clear_entry(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Caluclator(root)
    root.mainloop()

