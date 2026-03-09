"""Breve: Muestra la reutilización de `QAction` en menú y toolbar.
Permite activar la misma acción desde botón, menú o acceso directo.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout)
from PySide6.QtGui import QAction, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reutilización de QAction")

        self._create_widgets()
        self._create_actions()
        self._create_menu()
        self._create_toolbar()
        self._connect_signals()

    def _create_widgets(self):
        self.label = QLabel("Texto original")
        self.button = QPushButton("Cambiar texto (botón)")
        self.button.setStatusTip("Este botón cambia el texto del label")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        central_widget.setLayout(layout)

        self.statusBar().showMessage("Listo")

    def _create_actions(self):
        self.action_change_text = QAction("Cambiar texto", self)
        self.action_change_text.setShortcut(QKeySequence("Ctrl+T"))
        self.action_change_text.setStatusTip("Cambia el texto del label")

    def _create_menu(self):
        menu_opciones = self.menuBar().addMenu("Opciones")
        menu_opciones.addAction(self.action_change_text)

    def _create_toolbar(self):
        toolbar = self.addToolBar("Principal")
        toolbar.addAction(self.action_change_text)

    def _connect_signals(self):
        self.action_change_text.triggered.connect(self.change_label_text)
        self.button.clicked.connect(self.action_change_text.trigger)

    def change_label_text(self):
        self.label.setText("Texto cambiado 🎉")
        self.statusBar().showMessage("Texto cambiado correctamente", 2000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
