"""Breve: Muestra cómo crear una `QToolBar` y conectar `QAction`.
Incluye menú, toolbar y acciones con atajos.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QVBoxLayout, QMessageBox
)
from PySide6.QtGui import QAction, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("20 QToolBar + QAction")

        self._create_widgets()
        self._create_layout()
        self._create_actions()
        self._create_menu_status()
        self._create_toolbar()
        self._connect_signals()

    def _create_widgets(self):
        self.label = QLabel("Estado: esperando acción…")

    def _create_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        central_widget.setLayout(layout)

    def _create_actions(self):
        # Acción Salir
        self.action_exit = QAction("Salir", self)
        self.action_exit.setShortcut(QKeySequence("Ctrl+Q"))
        self.action_exit.setStatusTip("Cerrar la aplicación") # Para la barra de estado

        # Acción Cambiar texto
        self.action_change_text = QAction("Cambiar texto", self)
        self.action_change_text.setShortcut(QKeySequence("Ctrl+T"))
        self.action_change_text.setStatusTip("Cambiar el texto del label") # Para la barra de estado

        # Acción reset del texto
        self.action_reset_text = QAction("Resetear texto", self)
        self.action_reset_text.setShortcut(QKeySequence("Ctrl+R"))
        self.action_reset_text.setStatusTip("Resetear el texto del label") # Para la barra de estado

    def _create_menu_status(self):
        menu_archivo = self.menuBar().addMenu("Archivo")
        menu_archivo.addAction(self.action_exit)

        menu_opciones = self.menuBar().addMenu("Opciones")
        menu_opciones.addAction(self.action_change_text)
        menu_opciones.addAction(self.action_reset_text)

        # Barra de estado
        self.statusBar()

    def _create_toolbar(self):
        toolbar = self.addToolBar("Principal")
        toolbar.addAction(self.action_change_text)
        toolbar.addAction(self.action_reset_text)
        toolbar.addAction(self.action_exit)

    def _connect_signals(self):
        self.action_exit.triggered.connect(self.close)
        self.action_change_text.triggered.connect(lambda: self.label.setText("Texto cambiado por QAction"))
        self.action_reset_text.triggered.connect(lambda: self.label.setText("Texto reseteado por QAction"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
