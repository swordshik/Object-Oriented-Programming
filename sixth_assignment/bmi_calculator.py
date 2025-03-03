from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel,QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QRadioButton, QButtonGroup, QMessageBox, QAction)
from PyQt5.QtGui import QIcon


class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(400, 250, 300, 300)
        self.setWindowIcon(QIcon("sixth_assignment\images.png"))

        
        center_ = QWidget()
        self.setCentralWidget(center_)
        layout = QVBoxLayout(center_)

        
        choosing_units = QHBoxLayout()
        self.unit_group = QButtonGroup(self)
        
        self.metric_ = QRadioButton("Metric (kg, m)")
        self.unit_group.addButton(self.metric_)
        self.metric_.setChecked(True)
        choosing_units.addWidget(self.metric_)

        self.imperial_ = QRadioButton("Imperial (lbs, inches)")
        self.unit_group.addButton(self.imperial_)
        choosing_units.addWidget(self.imperial_)

        layout.addLayout(choosing_units)

        
        weight_layout = QHBoxLayout()
        self.weight_label = QLabel("Weight:")
        self.weight_input = QLineEdit()
        weight_layout.addWidget(self.weight_label)
        weight_layout.addWidget(self.weight_input)
        layout.addLayout(weight_layout)

        
        height_layout = QHBoxLayout()
        self.height_label = QLabel("Height:")
        self.height_input = QLineEdit()
        height_layout.addWidget(self.height_label)
        height_layout.addWidget(self.height_input)
        layout.addLayout(height_layout)

        
        self.calculate_button = QPushButton("Calculate BMI")
        self.calculate_button.clicked.connect(self.calculate_bmi)
        layout.addWidget(self.calculate_button)

        
        self.bmi_result = QLabel("BMI: ")
        self.bmi_status = QLabel("Status: ")
        layout.addWidget(self.bmi_result)
        layout.addWidget(self.bmi_status)

        
        self.create_menu()

    def create_menu(self):
        menu_bar = self.menuBar()

        
        file_menu = menu_bar.addMenu("File")
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_inputs)
        file_menu.addAction(clear_action)

        
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def clear_inputs(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.bmi_result.setText("BMI: ")
        self.bmi_status.setText("Status: ")
        self.metric_.setChecked(True)

    def show_about(self):
        QMessageBox.information(self, "About",
                               "Enter your weight and height in the selected units:\n"
                               "Metric: kilograms and meters\n"
                               "Imperial: pounds and inches\n"
                               "Click 'Calculate BMI' to view your BMI result and status.")

    def calculate_bmi(self):
        
        weight_text = self.weight_input.text()
        height_text = self.height_input.text()

        try:
            weight = float(weight_text)
            height = float(height_text)
            if weight <= 0 or height <= 0:
                raise ValueError("Values must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid positive numbers.")
            return

        
        if self.metric_.isChecked():
            bmi = weight / (height ** 2)
        else:
            bmi = (weight * 703) / (height ** 2)
        bmi_rounded = round(bmi, 2)

        
        if bmi < 18.5:
            status = "Underweight"
            color = "blue"
        elif 18.5 <= bmi < 25:
            status =  "Normal"
            color = "green"
        elif 25 <= bmi < 30:
            status = "Overweight" 
            color = "orange"
        else:
            status = "Obese"
            color =  "red"

        
        self.bmi_result.setText(f"BMI: {bmi_rounded}")
        self.bmi_status.setText(f"Status: <font color='{color}'>{status}</font>")