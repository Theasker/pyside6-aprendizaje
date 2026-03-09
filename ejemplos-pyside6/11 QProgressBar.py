"""Breve: Demostración básica de `QProgressBar` vinculada a un `QSlider`.
Actualiza la barra y una etiqueta con el porcentaje actual.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QSlider,
    QVBoxLayout, QLabel, QProgressBar
)
from PySide6.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar básico")
        self._create_widgets()
        self._create_layout()
        self._connect_signals()
    
    def _create_widgets(self):
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(10)
    
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(self.slider.value())

        self.label = QLabel(f"Progreso: {self.slider.value()}%")
    
    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.progress)
        layout.addWidget(self.label)
        self.setLayout(layout)
    
    def _connect_signals(self):
        self.slider.valueChanged.connect(self.on_slider_value_changed)

    def on_slider_value_changed(self, value):
        self.progress.setValue(value)
        self.label.setText(f"Progreso: {value}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
