"""Breve: Introducción mínima a PySide6.
Crea una ventana simple con `QLabel` y layouts horizontales/verticales.
"""

from ast import main
import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

if __name__ == "__main__":
    # 1. Crear la aplicación
    app = QApplication(sys.argv)

    # 2. Crear una ventana
    window = QWidget()
    window.setWindowTitle("Ventana con QLabel")
    window.resize(400, 300)

    # 3. Layout principal vertical
    main_layout = QVBoxLayout()

    title = QLabel("Título Principal")
    title.setStyleSheet("font-weight: bold; font-size: 16px;")
    main_layout.addWidget(title)

    # 4. Layout horizontal para etiquetas secundarias
    row_layout = QHBoxLayout()
    row_layout.addWidget(QLabel("Etiqueta 1"))
    row_layout.addWidget(QLabel("Etiqueta 2"))
    row_layout.addWidget(QLabel("Etiqueta 3"))
    
    # 5. Añadir el layout horizontal al layout principal
    main_layout.addLayout(row_layout)

    # 6. Establecer el layout principal en la ventana
    window.setLayout(main_layout)

    window.show()
    sys.exit(app.exec())