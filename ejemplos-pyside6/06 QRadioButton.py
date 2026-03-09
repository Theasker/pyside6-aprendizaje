"""Breve: Ejemplo básico de `QRadioButton` y `QButtonGroup`.
Actualiza una etiqueta con la opción seleccionada.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QRadioButton,
    QVBoxLayout, QLabel, QButtonGroup
)
 
class MainWindow(QWidget):
 
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QRadioButton básico")

        self.label = QLabel("Elige un color:")

        self.radio1 = QRadioButton("Rojo")
        self.radio2 = QRadioButton("Verde")
        self.radio3 = QRadioButton("Azul")

        # Grupo de botones
        self.group = QButtonGroup(self)
        self.group.addButton(self.radio1)
        self.group.addButton(self.radio2)
        self.group.addButton(self.radio3)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        self.setLayout(layout)

        # Señal del grupo
        self.group.buttonClicked.connect(self.on_radio_clicked)

    def on_radio_clicked(self, button):
        self.label.setText(f"Color seleccionado: {button.text()}")
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())