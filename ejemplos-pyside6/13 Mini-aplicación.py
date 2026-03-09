"""Breve: Mini-aplicación ejemplo — conversor de Celsius a Fahrenheit.
Demuestra widgets básicos: QLineEdit, QPushButton, QLabel.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout
)

class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de temperatura")

        self.converter = TemperatureConverter()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Grados Celsius")

        self.button = QPushButton("Convertir")
        self.result_label = QLabel("Resultado:")

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        self.button.clicked.connect(self.on_convert_clicked)

    def on_convert_clicked(self):
        text = self.input.text()
        
        if not text:
            self.result_label.setText("Por favor, ingrese un valor.")
            return
        try:
            celsius = float(text)
            fahrenheit = self.converter.celsius_to_fahrenheit(celsius)
            self.result_label.setText(f"Fahrenheit: {fahrenheit:.2f} °F")
        except ValueError:
            self.result_label.setText("Entrada inválida. Por favor, ingrese un número.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())