"""Breve: Ejemplo básico de `QSlider` horizontal.
Muestra cómo conectar la señal `valueChanged` para actualizar la UI.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QSlider,
    QVBoxLayout, QLabel
)
from PySide6.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider básico")

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(25)

        self.label = QLabel(f"Valor: {self.slider.value()} %")

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Señal
        self.slider.valueChanged.connect(self.on_value_changed)

    def on_value_changed(self, value):
        self.label.setText(f"Valor: {value} %")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
