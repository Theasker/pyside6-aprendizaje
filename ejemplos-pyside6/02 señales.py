"""Breve: Demostración básica de señales y slots en PySide6.
Conecta la señal `clicked` de un botón a un método que cambia el texto.
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Señales y Slots en PySide6")

        self.button = QPushButton("Púlsame")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

        # Conectamos la señal al método
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        if self.button.text() == "Púlsame":
            self.button.setText("Pulsado")
            print("¡Botón pulsado1!")
        else:
            self.button.setText("Púlsame")
            print("¡Botón pulsado2!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())