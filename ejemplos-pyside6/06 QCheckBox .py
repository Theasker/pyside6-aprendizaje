"""Breve: Ejemplo de `QCheckBox` que muestra estado (seleccionado/deseleccionado).
Actualiza una etiqueta según el estado del checkbox.
"""

from calendar import c
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QCheckBox, QVBoxLayout, QLabel
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de QCheckBox")

        self.checkbox = QCheckBox("Aceptar términos y condiciones")
        self.label = QLabel("")

        _layout = QVBoxLayout()
        _layout.addWidget(self.checkbox)
        _layout.addWidget(self.label)
        self.setLayout(_layout)

        # Conectar la señal stateChanged a un método
        self.checkbox.stateChanged.connect(self.on_state_changed)
    
    def on_state_changed(self, state):
        if self.checkbox.isChecked():
            self.label.setText("Checkbox seleccionado")
        else:
            self.label.setText("Checkbox deseleccionado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())