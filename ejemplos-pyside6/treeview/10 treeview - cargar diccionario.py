"""Breve: Muestra cómo cargar un diccionario anidado en un `QTreeView`.
Contiene estructura de ejemplo y esqueleto para poblar el modelo.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTreeView, QLabel
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt


data = {
    "empresa": "Gobierno de Aragón",
    "departamentos": {
        "Tecnología": {
            "responsable": "Mauricio Segura",
            "equipo": ["Ana", "Luis", "Marta"]
        },
        "Compras": {
            "responsable": "Elena",
            "presupuesto": 125000
        }
    },
    "inventario": {
        "portátiles": [
            {"marca": "Dell", "serie": "ABC123"},
            {"marca": "HP", "serie": "XYZ456"}
        ],
        "monitores": 42
    }
}

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QTreeView - Diccionario anidado (Paso 1)")
        self.resize(600, 400)

        central_widget = QWidget() # Crear widget central
        layout = QVBoxLayout(central_widget) # Crear layout vertical
        self.setCentralWidget(central_widget) # Asignar widget central al QMainWindow

        
        info = QLabel(
            "Mostrando un diccionario anidado en un QTreeView.\n"
            "Clave → columna izquierda | Valor → columna derecha"
        )
        info.setWordWrap(True)
        layout.addWidget(info)

        # Vista
        self.tree = QTreeView() # Crear QTreeView
        self.tree.setAlternatingRowColors(True) # Colores alternos en filas
        self.tree.setUniformRowHeights(True) # Filas de altura uniforme
        self.tree.header().setStretchLastSection(False) # No estirar última columna
        self.tree.header().setDefaultSectionSize(200) # Ancho por defecto de las columnas
        layout.addWidget(self.tree) # Añadir QTreeView al layout

        # Modelo
        self.model = QStandardItemModel() # Crear modelo
        self.model.setHorizontalHeaderLabels(["Clave", "Valor"]) # Establecer encabezados
        self.tree.setModel(self.model) # Asignar modelo al QTreeView

        # Cargar el diccionario en el modelo
        self.populate_model(self.model, data)

        self.tree.expandAll() # Expandir todos los nodos

    def populate_model(self, parent, data):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

