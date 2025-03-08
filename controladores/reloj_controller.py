from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, QTime, Signal

class DigitalClock(QWidget):
    alarm_triggered = Signal(str)  # Señal para emitir el mensaje de alarma

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_12_hour_format = False  # Formato de 12 horas (por defecto 24 horas)
        self.alarm_enabled = False  # Alarma desactivada por defecto
        self.alarm_hour = 0  # Hora de la alarma
        self.alarm_minute = 0  # Minuto de la alarma
        self.alarm_message = "Alarma!"  # Mensaje de la alarma
        self.alarm_triggered_flag = False  # Bandera para evitar múltiples activaciones

        # Configuración de la interfaz
        self.time_label = QLabel(self)
        self.time_label.setStyleSheet("font-size: 24px;")
        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        # Temporizador para actualizar la hora cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        """Actualiza la hora y verifica si la alarma debe activarse."""
        current_time = QTime.currentTime()

        if self.is_12_hour_format:
            display_text = current_time.toString("hh:mm:ss AP")
        else:
            display_text = current_time.toString("HH:mm:ss")
        self.time_label.setText(display_text)

        if self.alarm_enabled:
            if (current_time.hour() == self.alarm_hour and
                current_time.minute() == self.alarm_minute):
                if not self.alarm_triggered_flag: 
                    print(f"Alarma activada: {self.alarm_message}") 
                    self.alarm_triggered.emit(self.alarm_message)
                    self.alarm_triggered_flag = True
            else:
                self.alarm_triggered_flag = False 

    def get_is_12_hour_format(self):
        return self.is_12_hour_format

    def set_is_12_hour_format(self, value):
        self.is_12_hour_format = value

    def get_alarm_enabled(self):
        return self.alarm_enabled

    def set_alarm_enabled(self, value):
        self.alarm_enabled = value

    def get_alarm_hour(self):
        return self.alarm_hour

    def set_alarm_hour(self, value):
        self.alarm_hour = value

    def get_alarm_minute(self):
        return self.alarm_minute

    def set_alarm_minute(self, value):
        self.alarm_minute = value

    def get_alarm_message(self):
        return self.alarm_message

    def set_alarm_message(self, value):
        self.alarm_message = value