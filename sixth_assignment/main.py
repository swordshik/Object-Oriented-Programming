import sys
from PyQt5.QtWidgets import QApplication
from bmi_calculator import BMICalculator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())