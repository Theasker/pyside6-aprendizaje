"""Breve: Diálogo que guarda texto en un archivo cuando se pulsa un botón.
Ejemplo simple de uso de QDialog/QLineEdit para escribir en fichero.
"""

import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QDialog

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.edit = QLineEdit("Say something to the file")
        self.button = QPushButton("Send to file")
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        with open("dialog.txt", "a") as file:
            file.write(f"{self.edit.text()}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
            
        