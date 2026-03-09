"""Breve: Ejemplo mínimo del patrón MVC (modelo-vista-controlador).
Controlador conecta un modelo de contador con una vista Qt.
"""

import sys
from PySide6.QtWidgets import QApplication, QSpinBox, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

class CounterModel:
    def __init__(self):
        self._value = 0
        self._max_value = 10

    def increment(self):
        if self._value < self._max_value: # No puede subir de 10
            self._value += 1
            return True
        return False
    
    def decrement(self):
        if self._value > 0: # No puede bajar de 0
            self._value -= 1
            return True
        return False
    
    def reset(self):
        self._value = 0
    
    def set_max_value(self, value):
        self._max_value = value
        if self._value > self._max_value:
            self._value = self._max_value
    
    def value(self):
        return self._value

class CounterView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bloque 23 – MVC básico")
        self._create_widgets()
        self._create_layout()

    def _create_widgets(self):
        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_add = QPushButton("Sumar")
        self.btn_decrement = QPushButton("Restar")
        self.btn_reset = QPushButton("Reset")
        self.spin_max = QSpinBox()  
        self.spin_max.setRange(0, 10)
        self.spin_max.setSingleStep(1)
        self.spin_max.setValue(10)
        self.spin_max.setAlignment(Qt.AlignCenter)
        self.msg_label = QLabel("")
        self.msg_label.setAlignment(Qt.AlignCenter)


    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_decrement)
        layout.addWidget(self.btn_reset)
        layout.addWidget(self.spin_max)
        layout.addWidget(self.msg_label)
        self.setLayout(layout)

class CounterController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.btn_add.clicked.connect(self.add)
        self.view.btn_decrement.clicked.connect(self.decrement)
        self.view.btn_reset.clicked.connect(self.reset)
        self.view.spin_max.valueChanged.connect(self.set_max_value)

    def add(self):
        if self.model.increment():           
            self.view.label.setText(str(self.model.value()))
            self.view.msg_label.setText("") # Borrar mensaje
        else:
            self.view.msg_label.setText("Máximo alcanzado")
    
    def decrement(self):
        if self.model.decrement():
            self.view.label.setText(str(self.model.value()))
            self.view.msg_label.setText("") # Borrar mensaje
        else:
            self.view.msg_label.setText("Mínimo alcanzado")
    
    def reset(self):
        self.model.reset()
        self.view.label.setText(str(self.model.value()))
    
    def set_max_value(self, value):
        self.model.set_max_value(value)
        self.view.msg_label.setText(str(self.model.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = CounterModel()
    view = CounterView()
    controller = CounterController(model, view)

    view.show()
    sys.exit(app.exec())
