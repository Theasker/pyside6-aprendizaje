"""Breve: Ejemplo de `QLineEdit` y manejo de sus señales (returnPressed, textChanged).
Imprime/actualiza información cuando el usuario escribe y pulsa el botón.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, 
    QLineEdit, QPushButton, QVBoxLayout
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit Example")

        # Widgets
        self.label = QLabel("Enter your name:")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Mostrar texto")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # Señales y slots
        self.button.clicked.connect(self.on_button_clicked)
        self.line_edit.returnPressed.connect(self.on_button_clicked)
        self.line_edit.textChanged.connect(self.on_text_changed)

    def on_button_clicked(self):
        text = self.line_edit.text().strip()
        if text:
            print(f"Has escrito: {text}!")
        else:
            print("No has escrito nada.")

    def on_text_changed(self, text):
        text = text.strip()
        if text:
            self.label.setText(f"Longitud: {len(text)}")
        else:
            self.label.setText("Campo vacío")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())