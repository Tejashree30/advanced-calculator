import tkinter as tk
from tkinter import messagebox
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Scientific Calculator")
        master.geometry("400x600")
        master.config(bg="#1e1e1e")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        input_frame = tk.Frame(self.master, bd=0, bg="#1e1e1e")
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 22, 'bold'),
                               textvariable=self.input_text, width=30, bg="#2e2e2e", fg="white", bd=10, insertwidth=4,
                               justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=15)

    def create_buttons(self):
        btns_frame = tk.Frame(self.master, bg="#1e1e1e")
        btns_frame.pack()

        buttons = [
            ["C", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "**", "="],
            ["sin", "cos", "tan", "sqrt"],
            ["log", "ln", "//", "π"]
        ]

        for row_index, row in enumerate(buttons):
            for col_index, button in enumerate(row):
                self.create_button(btns_frame, button, row_index, col_index)

    def create_button(self, frame, text, row, col):
        button = tk.Button(
            frame,
            text=text,
            width=8,
            height=3,
            fg="white",
            bg="#333333",
            font=('arial', 14),
            bd=0,
            command=lambda: self.on_button_click(text)
        )
        button.grid(row=row, column=col, padx=1, pady=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.expression = self.expression[:-1]
        elif char == "=":
            self.calculate_result()
            return
        elif char == "π":
            self.expression += str(math.pi)
        elif char == "sin":
            self.calculate_function(math.sin)
            return
        elif char == "cos":
            self.calculate_function(math.cos)
            return
        elif char == "tan":
            self.calculate_function(math.tan)
            return
        elif char == "sqrt":
            self.calculate_function(math.sqrt)
            return
        elif char == "log":
            self.calculate_function(math.log10)
            return
        elif char == "ln":
            self.calculate_function(math.log)
            return
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)

    def calculate_function(self, func):
        try:
            value = eval(self.expression)
            result = func(math.radians(value)) if func in [math.sin, math.cos, math.tan] else func(value)
            self.input_text.set(f"{func.__name__}({value}) = {result}")
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input!\n{e}")
            self.expression = ""
            self.input_text.set("")

    def calculate_result(self):
        try:
            result = eval(self.expression)
            self.input_text.set(str(result))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression!\n{e}")
            self.expression = ""
            self.input_text.set("")


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
