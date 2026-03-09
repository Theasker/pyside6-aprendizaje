"""Breve: Ejemplo de `QAction` dentro de menús y su uso para ejecutar comandos.
Incluye una acción 'Acerca de' que muestra un `QMessageBox`.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QVBoxLayout, QPushButton, QMessageBox
)
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("19 QActions con Menú")

        self._create_widgets()
        self._create_layout()
        self._create_menu()
        self._connect_signals()

    def _create_widgets(self):
        self.label = QLabel("Estado: esperando acción…")
        self.btn1 = QPushButton("Púlsame")
    
    def _create_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn1)

        central_widget.setLayout(layout)

    def _create_menu(self):
        # Menú Archivo
        self.menu_archivo = self.menuBar().addMenu("Archivo")
        self.accion_salir = QAction("Salir", self)
        self.menu_archivo.addAction(self.accion_salir)

        # Menú Opciones
        self.menu_opciones = self.menuBar().addMenu("Opciones")
        self.accion_opcion1 = QAction("Opción 1", self)
        self.accion_opcion2 = QAction("Opción 2", self)
        self.menu_opciones.addAction(self.accion_opcion1)
        self.menu_opciones.addAction(self.accion_opcion2)

        # Menú Ayuda
        self.menu_ayuda = self.menuBar().addMenu("Ayuda")
        self.accion_acerca = QAction("Acerca de", self)
        self.menu_ayuda.addAction(self.accion_acerca)

    def _connect_signals(self):
        # Botón
        self.btn1.clicked.connect(lambda: self.label.setText(f"Presionado el botón {self.btn1.text()}"))
        # Archivo
        self.accion_salir.triggered.connect(self.close)
        # Opciones
        self.accion_opcion1.triggered.connect(lambda: self.label.setText("Seleccionada Opción 1"))  
        self.accion_opcion2.triggered.connect(lambda: self.label.setText("Seleccionada Opción 2"))
        # Ayuda
        # self.accion_acerca.triggered.connect(self._show_about)
        self.accion_acerca.triggered.connect(lambda: QMessageBox.information(self, "Acerca de", "Curso PySide6\nEjemplo de QActions con Menú"))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())