"""Breve: Ejemplo de `QDialog` simple con botones Aceptar/Cancelar.
Se muestra cómo ejecutar el diálogo y leer el resultado en la ventana principal.
"""

import sys
from PySide6.QtWidgets import QWidget, QApplication, QDialog, QLabel, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("17 QDialog - Ventana Principal")

        self._create_widgets()
        self._create_layout()
        self._connect_signals()
  
    def _create_widgets(self):
        self.open_dialog_button = QPushButton("Abrir Diálogo")
        self.result_label = QLabel("Resultado del diálogo:")

    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.open_dialog_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def _connect_signals(self):
        self.open_dialog_button.clicked.connect(self.open_dialog)
    
    def open_dialog(self):
        dialog = MyDialog()
        result = dialog.exec()
        print(f"Resultado del diálogo: {result}")
        if result == QDialog.Accepted:
            self.result_label.setText("Resultado del diálogo: Aceptado")
        else:
            self.result_label.setText("Resultado del diálogo: Cancelado")


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()        
        self.setWindowTitle("Diálogo simple")
        self.resize(200, 100)
            
        self._create_widgets()
        self._create_layout()
        self._connect_signals()   

    def _create_widgets(self):
        self.label = QLabel("¿Aceptar o cancelar?")
        self.btn_ok = QPushButton("Aceptar")
        self.btn_cancel = QPushButton("Cancelar")

    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_ok)
        layout.addWidget(self.btn_cancel)
        self.setLayout(layout)

    def _connect_signals(self):
        self.btn_ok.clicked.connect(self.accept)
        self.btn_cancel.clicked.connect(self.reject)
        print("self.accept:", self.accept)
        print("self.reject:", self.reject)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())