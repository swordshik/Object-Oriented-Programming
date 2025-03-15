import sys
from PyQt5.QtWidgets import QApplication
from window import CalculatorWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())