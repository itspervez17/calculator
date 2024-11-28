# Calculator with GUI and Backspace Key

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == 'C':
                tk.Button(self.master, text=button, padx=20, pady=20, command=self.clear).grid(row=row_val, column=col_val)
            elif button == '=':
                tk.Button(self.master, text=button, padx=20, pady=20, command=self.calculate).grid(row=row_val, column=col_val)
            else:
                tk.Button(self.master, text=button, padx=20, pady=20, command=lambda b=button: self.append_to_expression(b)).grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Backspace Button
        tk.Button(self.master, text='←', padx=20, pady=20, command=self.backspace).grid(row=row_val, column=0, columnspan=4)

    def append_to_expression(self, value):
        current_text = self.result_var.get()
        self.result_var.set(current_text + value)

    def clear(self):
        self.result_var.set("")

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

    def backspace(self):
        current_text = self.result_var.get()
        self.result_var.set(current_text[:-1])

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
