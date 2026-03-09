"""Breve: Demuestra diferentes tipos de QMessageBox y uso de StatusBar.
Incluye acciones de menú y mensajes informativos/confirmación.
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
        self.setWindowTitle("Bloque 22 – QMessageBox + StatusBar")

        self._create_widgets()
        self._create_layout()
        self._create_actions()
        self._create_menu_toolbar()
        self.statusBar()  # Creamos la barra de estado
        self._connect_signals()

    def _create_widgets(self):
        self.label = QLabel("Estado: esperando acción…")
        self.label.setStatusTip("Etiqueta para mostrar el estado actual")

        self.btn_info = QPushButton("Info")
        self.btn_info.setStatusTip("Mostrar mensaje de información")

        self.btn_warn = QPushButton("Advertencia")
        self.btn_warn.setStatusTip("Mostrar mensaje de advertencia")

        self.btn_danger = QPushButton("Peligro")
        self.btn_danger.setStatusTip("Mostrar mensaje de peligro")

        self.btn_question = QPushButton("Pregunta")
        self.btn_question.setStatusTip("Mostrar mensaje de pregunta")

    def _create_layout(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_info)
        layout.addWidget(self.btn_warn)
        layout.addWidget(self.btn_danger)
        layout.addWidget(self.btn_question)
        central.setLayout(layout)

    def _create_actions(self):
        self.action_exit = QAction("Salir", self)
        self.action_exit.setStatusTip("Cerrar la aplicación")

    def _create_menu_toolbar(self):
        # Menú Archivo
        menu_archivo = self.menuBar().addMenu("Archivo")
        menu_archivo.addAction(self.action_exit)

        # Toolbar
        toolbar = self.addToolBar("Principal")
        toolbar.addAction(self.action_exit)

    def _connect_signals(self):
        # Botones
        self.btn_info.clicked.connect(self.show_info)
        self.btn_warn.clicked.connect(self.show_warning)
        self.btn_danger.clicked.connect(self.show_danger)
        self.btn_question.clicked.connect(self.show_question)

        # Acción salir
        self.action_exit.triggered.connect(self.close)

    def show_info(self):
        QMessageBox.information(self, "Información", "Esto es un mensaje informativo.")
        self.statusBar().showMessage("Se mostró información", 2000)

    def show_warning(self):
        QMessageBox.warning(self, "Advertencia", "¡Esto es una advertencia!")
        self.statusBar().showMessage("Se mostró advertencia", 2000)

    def show_danger(self):
        QMessageBox.critical(self, "Peligro", "¡Esto es un mensaje de peligro!")
        self.statusBar().showMessage("Se mostró mensaje de peligro", 2000)

    def show_question(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmación",
            "¿Deseas cambiar el texto del label?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            self.label.setText("Texto cambiado tras confirmación")
            self.statusBar().showMessage("El usuario confirmó la acción", 2000)
        else:
            self.statusBar().showMessage("El usuario canceló la acción", 2000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
