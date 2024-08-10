from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import sympy as sp

class CalculusApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Input for the mathematical expression
        self.expr_input = TextInput(hint_text='Enter expression (e.g., x**2 + y**2)')
        layout.add_widget(self.expr_input)

        # Input for the variables (comma-separated)
        self.var_input = TextInput(hint_text='Enter variables (e.g., x, y)')
        layout.add_widget(self.var_input)

        # Label to display the result
        self.result_label = Label(text='Result will be displayed here')
        layout.add_widget(self.result_label)

        # Buttons for solving differentiation and integration
        diff_button = Button(text='Differentiate')
        diff_button.bind(on_press=self.differentiate)
        layout.add_widget(diff_button)

        int_button = Button(text='Integrate')
        int_button.bind(on_press=self.integrate)
        layout.add_widget(int_button)

        return layout

    def differentiate(self, instance):
        expression = self.expr_input.text
        variables = self.var_input.text.split(',')

        # Convert expression and variables to sympy objects
        expr = sp.sympify(expression)
        vars = [sp.symbols(var.strip()) for var in variables]

        # Perform differentiation for each variable
        diff_expr = [sp.diff(expr, var) for var in vars]

        # Format the result
        result_text = " + ".join([f"d({expr})/d({var}) = {d_expr}" for var, d_expr in zip(vars, diff_expr)])
        self.result_label.text = f'Result: {result_text}'

    def integrate(self, instance):
        expression = self.expr_input.text
        variables = self.var_input.text.split(',')

        # Convert expression and variables to sympy objects
        expr = sp.sympify(expression)
        vars = [sp.symbols(var.strip()) for var in variables]

        # Perform integration for each variable
        int_expr = [sp.integrate(expr, var) for var in vars]

        # Format the result
        result_text = " + ".join([f"∫({expr}) d({var}) = {i_expr}" for var, i_expr in zip(vars, int_expr)])
        self.result_label.text = f'Result: {result_text}'

if __name__ == "__main__":
    CalculusApp().run()
    
