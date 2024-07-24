import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Number 1
        self.num1_label = tk.Label(root, text="Number 1:")
        self.num1_label.grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(root)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        # Number 2
        self.num2_label = tk.Label(root, text="Number 2:")
        self.num2_label.grid(row=1, column=0, padx=10, pady=10)
        self.num2_entry = tk.Entry(root)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        # Operation
        self.operation_label = tk.Label(root, text="Operation (+, -, *, /):")
        self.operation_label.grid(row=2, column=0, padx=10, pady=10)
        self.operation_entry = tk.Entry(root)
        self.operation_entry.grid(row=2, column=1, padx=10, pady=10)

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, padx=10, pady=10)

        # Clear button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear)
        self.clear_button.grid(row=3, column=1, padx=10, pady=10)

        # Result
        self.result_label = tk.Label(root, text="Result:")
        self.result_label.grid(row=4, column=0, padx=10, pady=10)
        self.result_display = tk.Label(root, text="", font=('Helvetica', 14))
        self.result_display.grid(row=4, column=1, padx=10, pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_entry.get()

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Invalid operation")
                return

            self.result_display.config(text=str(result))
        except ValueError:
            messagebox.showerror("Error", "Invalid input, please enter numeric values")

    def clear(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.operation_entry.delete(0, tk.END)
        self.result_display.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
