"""Breve: Ejemplo de `QComboBox` mostrando selección actual.
Actualiza una etiqueta cuando cambia la opción seleccionada.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QComboBox,
    QVBoxLayout, QLabel
)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox básico")

        self.label = QLabel("Tema seleccionado:")
        self.combo = QComboBox()

        # Añadir opciones
        self.combo.addItems([
            "Claro",
            "Oscuro",
            "Sistema",
        ])
        self.label.setText(f"Has elegido: {self.combo.currentText()}")

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Señal
        self.combo.currentTextChanged.connect(self.on_changed)

    def on_changed(self, text):
        self.label.setText(f"Has elegido: {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
