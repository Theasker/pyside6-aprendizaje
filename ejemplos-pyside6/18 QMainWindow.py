"""Breve: Ejemplo básico de `QMainWindow` con widget central y señales.
Muestra estructura mínima para ventanas principales en PySide6.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QLabel, QVBoxLayout, QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("18 QMainWindow - Ejemplo Básico")

        self._create_widgets()
        self._create_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.label = QLabel("Estado: esperando acción…")
        self.btn1 = QPushButton("Púlsame") 
    
    def _create_layout(self):
        # Crear un widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn1)

        # Asignar el layout al widget central
        central_widget.setLayout(layout)
    
    def _connect_signals(self):
        self.btn1.clicked.connect(lambda: self.label.setText(f"Presionado el botón {self.btn1.text()}"))
                                                                                    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())