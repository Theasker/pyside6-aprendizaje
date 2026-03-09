"""Breve: Conversor de temperatura usando `QDoubleSpinBox`.
Actualiza la vista en tiempo real al cambiar el valor del spinbox.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QDoubleSpinBox,
    QVBoxLayout
)

class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor Celsius → Fahrenheit")

        self.converter = TemperatureConverter()

        self._create_widgets()
        self._create_layout()
        self._connect_signals()

    def _create_widgets(self):
        # QDoubleSpinBox para Celsius
        self.spin = QDoubleSpinBox()
        self.spin.setSuffix(" °C")
        self.spin.setRange(-100.0, 100.0)
        self.spin.setDecimals(1)
        self.spin.setSingleStep(1)
        self.spin.setValue(0.0)

        self.result_label = QLabel()

    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.spin)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def _connect_signals(self):
        # Señal
        self.spin.valueChanged.connect(self.on_value_changed)
        self.on_value_changed(self.spin.value())

    def on_value_changed(self, value):
        fahrenheit = self.converter.celsius_to_fahrenheit(value)
        self.result_label.setText(f"Fahrenheit: {fahrenheit:.2f} °F")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
