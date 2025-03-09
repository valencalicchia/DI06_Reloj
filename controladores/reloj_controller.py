from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, QTime, Signal
from vistas.ui_reloj import Ui_vcRelojW  # Importamos la UI generada


class DigitalClock(QWidget, Ui_vcRelojW):
    """
    Clase que representa un reloj digital con funcionalidad de alarma.

    Hereda de QWidget y de la interfaz generada Ui_vcRelojW.
    """
    alarm_triggered = Signal(str)  # Señal emitida cuando la alarma se activa

    def __init__(self, parent=None):
        """
        Inicializa el reloj digital.

        Args:
            parent (QWidget, optional): Widget padre. Defaults to None.
        """
        super().__init__(parent)
        self.setupUi(self)  # Configura la interfaz de usuario
        self.is_12_hour_format = False  # Formato de 12 horas (False = 24 horas)
        self.alarm_enabled = False  # Estado de la alarma (activada/desactivada)
        self.alarm_hour = 0  # Hora de la alarma
        self.alarm_minute = 0  # Minuto de la alarma
        self.alarm_message = "Alarma!"  # Mensaje de la alarma
        self.alarm_triggered_flag = False  # Bandera para evitar múltiples activaciones

        # Configura un temporizador para actualizar la hora cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        """
        Actualiza la hora mostrada en el reloj y verifica si la alarma debe activarse.
        """
        current_time = QTime.currentTime()

        # Define el formato de la hora (12h o 24h)
        format_str = "hh:mm:ss AP" if self.is_12_hour_format else "HH:mm:ss"
        self.vcRelojLbl.setText(current_time.toString(format_str))

        # Verifica si la alarma está activada y si es la hora correcta
        if self.alarm_enabled and current_time.hour() == self.alarm_hour and current_time.minute() == self.alarm_minute:
            if not self.alarm_triggered_flag:  # Evita múltiples activaciones
                print(f"Alarma activada: {self.alarm_message}")  # Depuración
                self.alarm_triggered.emit(self.alarm_message)  # Emite la señal
                self.alarm_triggered_flag = True  # Activa la bandera
        else:
            self.alarm_triggered_flag = False  # Reinicia la bandera

    def set_12_hour_format(self, value):
        """
        Establece el formato de la hora (12h o 24h).

        Args:
            value (bool): True para formato de 12 horas, False para 24 horas.
        """
        self.is_12_hour_format = value

    def set_alarm(self, enabled, hour, minute, message):
        """
        Configura la alarma con los valores proporcionados.

        Args:
            enabled (bool): True para activar la alarma, False para desactivarla.
            hour (int): Hora de la alarma.
            minute (int): Minuto de la alarma.
            message (str): Mensaje de la alarma.
        """
        self.alarm_hour = hour
        self.alarm_minute = minute
        self.alarm_message = message
        self.alarm_enabled = enabled