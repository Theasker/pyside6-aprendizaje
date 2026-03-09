"""Breve: Diálogo de configuración con `QDoubleSpinBox`.
Ejemplo de abrir un `QDialog` modally y devolver un valor al padre.
"""

import sys
from PySide6.QtWidgets import (
    QDoubleSpinBox, QWidget, QApplication, QDialog, 
    QLabel, QPushButton, QVBoxLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("17.5 QDialog - Afianzar")

        self._create_widgets()
        self._create_layout()
        self._connect_signals()
    
    def _create_widgets(self):
        self.btn_configuration = QPushButton("Abrir Configuración")
        self.result_label = QLabel("Temperatura configurada:")
    
    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.btn_configuration)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
    
    def _connect_signals(self):
        self.btn_configuration.clicked.connect(self.open_configuration_dialog)
    
    def open_configuration_dialog(self):
        dialog = ConfigurationDialog()
        result = dialog.exec()
        
        if result == QDialog.Accepted:
            self.result_label.setText(f"Temperatura: {dialog.temp_value:.1f} °C")
        else:
            self.result_label.setText("Configuración cancelada")

class ConfigurationDialog(QDialog):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Diálogo de Configuración")

        self.temp_value = None

        self._create_widgets()
        self._create_layout()
        self._connect_signals()
    
    def _create_widgets(self):
        # spinbox
        self.spin_temperature = QDoubleSpinBox()
        self.spin_temperature.setSuffix(" °C")
        self.spin_temperature.setRange(-20.0, 50.0)
        self.spin_temperature.setDecimals(1)
        self.spin_temperature.setSingleStep(0.5)
        self.spin_temperature.setValue(20.0)

        # botones
        self.btn_ok = QPushButton("Aceptar")
        self.btn_cancel = QPushButton("Cancelar")
    
    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.spin_temperature)
        layout.addWidget(self.btn_ok)
        layout.addWidget(self.btn_cancel)
        self.setLayout(layout)
    
    def _connect_signals(self):
        # self.spin_temperature.valueChanged.connect(self.on_temp_changed)

        self.btn_ok.clicked.connect(self.on_accepted)
        self.btn_cancel.clicked.connect(self.reject)
    
    def on_accepted(self):
        self.temp_value = self.spin_temperature.value()
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())