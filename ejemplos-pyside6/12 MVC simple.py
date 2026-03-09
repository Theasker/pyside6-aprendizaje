"""Breve: Separación de lógica y vista: ejemplo simple de MVC.
El modelo transforma la entrada del slider y la vista muestra el resultado.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QSlider,
    QVBoxLayout, QLabel, QProgressBar
)
from PySide6.QtCore import Qt


class ProgressLogic:
    def compute(self, value):
        return value * 3


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Separación lógica / vista")

        # Lógica
        self.logic = ProgressLogic()

        # Widgets
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(10)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)

        self.label = QLabel()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.progress)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Señales
        self.slider.valueChanged.connect(self.on_slider_changed)

        # Estado inicial
        self.update_ui(self.slider.value())

    def on_slider_changed(self, value):
        self.update_ui(value)

    def update_ui(self, value):
        result = self.logic.compute(value)
        self.progress.setValue(result)
        self.label.setText(f"Entrada: {value} → Salida: {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
