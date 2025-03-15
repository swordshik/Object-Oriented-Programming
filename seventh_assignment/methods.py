class Methods:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char: str):
        self.expression += char

    def remove_last_character(self):
        self.expression = self.expression[:-1]

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            result = eval(self.expression)
            return str(result)
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error: {str(e)}"

    def get_expression(self):
        return self.expression