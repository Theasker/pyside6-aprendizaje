"""Breve: Ejemplo de uso de `setStatusTip` para mostrar descripciones en StatusBar.
Muestra cómo asociar tips a widgets y manejar mensajes de estado.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QVBoxLayout,
    QCheckBox, QSpinBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StatusTip + StatusBar ejemplo")

        self._create_widgets()
        self._create_layout()
        self._connect_signals()
        self.statusBar().showMessage("Aplicación iniciada", 3000)

    def _create_widgets(self):
        self.label = QLabel("Interacciones con StatusBar:")

        self.button = QPushButton("Pulsa aquí")
        self.button.setStatusTip("Este botón cambia el texto del label")

        self.checkbox = QCheckBox("Activar opción")
        self.checkbox.setStatusTip("Marca o desmarca esta opción")

        self.spinbox = QSpinBox()
        self.spinbox.setRange(0, 10)
        self.spinbox.setStatusTip("Selecciona un número del 0 al 10")

    def _create_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.spinbox)
        central_widget.setLayout(layout)

    def _connect_signals(self):
        self.button.clicked.connect(self.on_button_clicked)
        self.checkbox.stateChanged.connect(self.on_checkbox_changed)
        self.spinbox.valueChanged.connect(self.on_spinbox_changed)

    def on_button_clicked(self):
        self.label.setText("¡Botón pulsado!")
        self.statusBar().showMessage("Has pulsado el botón", 2000)

    def on_checkbox_changed(self, state):
        if state:
            self.statusBar().showMessage("Opción activada", 2000)
        else:
            self.statusBar().showMessage("Opción desactivada", 2000)

    def on_spinbox_changed(self, value):
        self.statusBar().showMessage(f"Valor del SpinBox: {value}", 1500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
