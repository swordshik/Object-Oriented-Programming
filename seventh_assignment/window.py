from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt
from methods import Methods

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.calculator = Methods()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.input = QLineEdit()
        self.input.setAlignment(Qt.AlignRight)
        self.input.setReadOnly(True)
        self.input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input.setMinimumHeight(35)
        self.input.setStyleSheet("font-size: 25px")  
        self.layout.addWidget(self.input)

        self.buttons_layout = QGridLayout()
        self.layout.addLayout(self.buttons_layout)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_button_click)
            self.buttons_layout.addWidget(button, row, col)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.calculator.clear_expression()
            self.input.clear()
        elif text == '=':
            result = self.calculator.calculate()
            self.input.setText(result)
            self.calculator.clear_expression()
        else:
            self.calculator.add_to_expression(text)
            self.input.setText(self.calculator.get_expression())