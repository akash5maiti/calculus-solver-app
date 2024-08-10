import tkinter as tk
from tkinter import messagebox
import sympy as sp

class CalculusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculus Calculator")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Expression:").grid(row=0, column=0, padx=10, pady=10)
        self.expr_entry = tk.Entry(self.root, width=30)
        self.expr_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        tk.Label(self.root, text="Variable:").grid(row=1, column=0, padx=10, pady=10)
        self.var_entry = tk.Entry(self.root, width=15)
        self.var_entry.grid(row=1, column=1, padx=10, pady=10)

        self.operation_var = tk.StringVar(value="differentiate")
        tk.Radiobutton(self.root, text="Differentiate", variable=self.operation_var, value="differentiate").grid(row=2, column=0, padx=10, pady=10)
        tk.Radiobutton(self.root, text="Integrate", variable=self.operation_var, value="integrate").grid(row=2, column=1, padx=10, pady=10)

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve_calculus)
        self.solve_button.grid(row=2, column=2, columnspan=2, pady=10)

        self.result_text = tk.Text(self.root, height=10, width=60)
        self.result_text.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def solve_calculus(self):
        expression = self.expr_entry.get()
        variable = self.var_entry.get()
        operation = self.operation_var.get()

        if not expression or not variable:
            messagebox.showerror("Input Error", "Please enter both expression and variable.")
            return

        try:
            x = sp.Symbol(variable)
            expr = sp.sympify(expression)
            
            if operation == 'differentiate':
                derivative = sp.diff(expr, x)
                steps = f"Original expression: {expr}\nDerivative with respect to {variable}: {derivative}\n"
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, steps)

            elif operation == 'integrate':
                integral = sp.integrate(expr, x)
                steps = f"Original expression: {expr}\nIntegral with respect to {variable}: {integral}\n"
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, steps)

            else:
                messagebox.showerror("Operation Error", "Operation not recognized. Please choose 'differentiate' or 'integrate'.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculusApp(root)
    root.mainloop()
