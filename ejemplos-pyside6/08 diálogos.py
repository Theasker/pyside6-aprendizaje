"""Breve: Muestra uso de `QMessageBox.question` para confirmación antes de cerrar.
Ejemplo simple de diálogo de confirmación.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QMessageBox
)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox básico")

        self.button = QPushButton("Cerrar aplicación")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.show_message)

    def show_message(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmación",
            "¿Seguro que quieres salir?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
