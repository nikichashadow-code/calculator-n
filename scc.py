import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)

        self.setStyleSheet("background-color: black;")

        self.layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setStyleSheet("background-color: black; color: white; font-size: 32px; font-family: Arial; border: none;")
        self.display.setFocusPolicy(Qt.NoFocus)  # Remove focus outline
        self.layout.addWidget(self.display)

        grid_layout = QGridLayout()
        buttons = [
            ('7', 1, 0, 1, 1), ('8', 1, 1, 1, 1), ('9', 1, 2, 1, 1), ('/', 1, 3, 1, 1),
            ('4', 2, 0, 1, 1), ('5', 2, 1, 1, 1), ('6', 2, 2, 1, 1), ('*', 2, 3, 1, 1),
            ('1', 3, 0, 1, 1), ('2', 3, 1, 1, 1), ('3', 3, 2, 1, 1), ('-', 3, 3, 1, 1),
            ('0', 4, 0, 1, 2), ('.', 4, 2, 1, 1), ('=', 4, 3, 1, 1), ('+', 5, 0, 1, 2),
            ('Delete', 5, 2, 1, 2)
        ]

        for (button_text, row, col, rowspan, colspan) in buttons:
            if button_text == 'Delete':
                button = QPushButton(button_text)
                button.clicked.connect(lambda checked, text=button_text: self.button_click(text))
                button.setStyleSheet("background-color: orange; font-size: 24px; color: black; font-family: Arial;")
                button.setFocusPolicy(Qt.NoFocus)  # Remove focus outline from buttons
                grid_layout.addWidget(button, row, col, rowspan, colspan)
            else:
                button = QPushButton(button_text)
                button.clicked.connect(lambda checked, text=button_text: self.button_click(text))
                button.setStyleSheet("background-color: orange; font-size: 24px; color: black; font-family: Arial;")
                button.setFocusPolicy(Qt.NoFocus)  # Remove focus outline from buttons
                grid_layout.addWidget(button, row, col, rowspan, colspan)

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)

        self.current_input = ''

    def keyPressEvent(self, event):
        key = event.key()
        key_mapping = {
            Qt.Key_0: '0', Qt.Key_1: '1', Qt.Key_2: '2', Qt.Key_3: '3',
            Qt.Key_4: '4', Qt.Key_5: '5', Qt.Key_6: '6', Qt.Key_7: '7',
            Qt.Key_8: '8', Qt.Key_9: '9', Qt.Key_Plus: '+', Qt.Key_Minus: '-',
            Qt.Key_Asterisk: '*', Qt.Key_Slash: '/', Qt.Key_Period: '.',
            Qt.Key_Enter: '=', Qt.Key_Backspace: 'Delete'
        }

        if key in key_mapping:
            self.button_click(key_mapping[key])

    def button_click(self, input_str):
        if input_str == '=':
            try:
                result = eval(self.current_input)
                self.display.setText(str(result))
                self.current_input = str(result)
            except Exception as e:
                self.display.setText('Error')
                self.current_input = ''
        elif input_str == 'Delete':
            self.current_input = self.current_input[:-1]
            self.display.setText(self.current_input)
        else:
            self.current_input += input_str
            self.display.setText(self.current_input)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())
