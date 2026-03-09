"""Breve: Ejemplo de uso de `StatusBar` con acciones y toolbar.
Incluye atajos de teclado y mensajes temporales en la barra de estado.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
)
from PySide6.QtGui import QAction, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bloque 21 – StatusBar Ejemplo")

        self._create_widgets()
        self._create_layout()
        self._create_actions()
        self._create_menu_toolbar_status()
        self._connect_signals()

    def _create_widgets(self):
        self.label = QLabel("Estado: esperando acción…")
        self.button = QPushButton("Presióname")

    def _create_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        central_widget.setLayout(layout)

    def _create_actions(self):
        # Acción Cambiar texto
        self.action_change_text = QAction("Cambiar texto", self)
        self.action_change_text.setShortcut(QKeySequence("Ctrl+T"))
        self.action_change_text.setStatusTip("Cambia el texto del label")  # explicación al pasar el ratón

        # Acción Resetear texto
        self.action_reset_text = QAction("Resetear texto", self)
        self.action_reset_text.setShortcut(QKeySequence("Ctrl+R"))
        self.action_reset_text.setStatusTip("Restaura el texto original")  # explicación al pasar el ratón

        # Acción Salir
        self.action_exit = QAction("Salir", self)
        self.action_exit.setShortcut(QKeySequence("Ctrl+Q"))
        self.action_exit.setStatusTip("Cierra la aplicación")

    def _create_menu_toolbar_status(self):
        # Menú
        menu_opciones = self.menuBar().addMenu("Opciones")
        menu_opciones.addAction(self.action_change_text)
        menu_opciones.addAction(self.action_reset_text)
        menu_opciones.addSeparator()
        menu_opciones.addAction(self.action_exit)

        # Toolbar
        toolbar = self.addToolBar("Principal")
        toolbar.addAction(self.action_change_text)
        toolbar.addAction(self.action_reset_text)
        toolbar.addAction(self.action_exit)

        # StatusBar
        self.statusBar().showMessage("Aplicación iniciada", 3000)

    def _connect_signals(self):
        self.action_change_text.triggered.connect(self.on_change_text)
        self.action_reset_text.triggered.connect(self.on_reset_text)
        self.action_exit.triggered.connect(self.close)
        self.button.clicked.connect(self.action_change_text.trigger)

    def on_change_text(self):
        self.label.setText("Texto cambiado correctamente")
        self.statusBar().showMessage("El texto fue cambiado", 2000)

    def on_reset_text(self):
        self.label.setText("Estado: esperando acción…")
        self.statusBar().showMessage("El texto fue restaurado", 2000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
