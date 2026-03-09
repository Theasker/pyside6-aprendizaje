"""Breve: Conversor con validador `QDoubleValidator` y ejemplo de
habilitar/deshabilitar widgets según validez de la entrada.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout
)
from PySide6.QtGui import QDoubleValidator
from PySide6.QtCore import QLocale

class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor con validación automática")

        self.converter = TemperatureConverter()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Introduce grados Celsius")

        validator = QDoubleValidator(-50.0, 50.0, 1)
        validator.setLocale(QLocale.c())
        self.input.setValidator(validator)

        self.button = QPushButton("Convertir")
        self.button.setEnabled(False)

        self.result_label = QLabel("Introduce un valor")

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        self.input.textChanged.connect(self.on_text_changed)
        self.button.clicked.connect(self.on_convert_clicked)

    def on_text_changed(self, text):
        # Si cumple la validación, habilitar el botón
        if self.input.hasAcceptableInput() and text:
            self.button.setEnabled(True)
            self.result_label.setText("Valor válido")
        else:
            self.button.setEnabled(False)
            self.result_label.setText("Introduce un número válido")

    def on_convert_clicked(self):
        celsius = float(self.input.text())
        fahrenheit = self.converter.celsius_to_fahrenheit(celsius)
        self.result_label.setText(f"Fahrenheit: {fahrenheit:.2f} °F")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
