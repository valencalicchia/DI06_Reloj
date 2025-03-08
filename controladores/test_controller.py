from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QTimeEdit, QLineEdit, QCheckBox
from PySide6.QtCore import QTime
from controladores.reloj_controller import DigitalClock

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reloj Digital con Alarma")

        # Configuración de la ventana principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # Reloj digital
        self.clock = DigitalClock()
        self.layout.addWidget(self.clock)

        # Checkbox para cambiar el formato de 12/24 horas
        self.format_checkbox = QCheckBox("Formato 12 horas")
        self.format_checkbox.stateChanged.connect(self.toggle_format)
        self.layout.addWidget(self.format_checkbox)

        # Checkbox para activar/desactivar la alarma
        self.alarm_checkbox = QCheckBox("Activar Alarma")
        self.alarm_checkbox.stateChanged.connect(self.toggle_alarm)
        self.layout.addWidget(self.alarm_checkbox)

        # QTimeEdit para seleccionar la hora de la alarma
        self.alarm_time_edit = QTimeEdit()
        self.alarm_time_edit.setDisplayFormat("HH:mm")
        self.alarm_time_edit.setTime(QTime.currentTime())  # Hora actual por defecto
        self.layout.addWidget(QLabel("Hora de Alarma:"))
        self.layout.addWidget(self.alarm_time_edit)

        # QLineEdit para el mensaje de la alarma
        self.message_lineedit = QLineEdit()
        self.message_lineedit.setPlaceholderText("Introduce el mensaje de la alarma")
        self.layout.addWidget(QLabel("Mensaje de Alarma:"))
        self.layout.addWidget(self.message_lineedit)

        # Etiqueta para mostrar el estado de la alarma
        self.alarm_label = QLabel("Alarma desactivada")
        self.layout.addWidget(self.alarm_label)

        self.central_widget.setLayout(self.layout)

        # Conectar la señal de alarma del reloj a un método
        self.clock.alarm_triggered.connect(self.on_alarm_triggered)

    def toggle_format(self, state):
        """Cambia el formato del reloj entre 12 y 24 horas."""
        self.clock.set_is_12_hour_format(state == 2)

    def toggle_alarm(self, state):
        """Activa o desactiva la alarma."""
        self.clock.set_alarm_enabled(state == 2)
        if state == 2:
            self.alarm_label.setText("Alarma activada")
            self.set_alarm()
        else:
            self.alarm_label.setText("Alarma desactivada")

    def set_alarm(self):
        """Configura la hora y el mensaje de la alarma."""
        alarm_time = self.alarm_time_edit.time()
        self.clock.set_alarm_hour(alarm_time.hour())
        self.clock.set_alarm_minute(alarm_time.minute())
        self.clock.set_alarm_message(self.message_lineedit.text())
        self.alarm_label.setText(f"Alarma configurada para {alarm_time.toString('HH:mm')}")

    def on_alarm_triggered(self, message):
        """Maneja el evento de alarma activada."""
        self.alarm_label.setText(f"Alarma activada: {message}")