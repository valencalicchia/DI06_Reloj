from PySide6.QtCore import QTime
from PySide6.QtWidgets import QMainWindow
from vistas.ui_test import Ui_Test
from controladores.reloj_controller import DigitalClock


class TestWindow(QMainWindow, Ui_Test):
    """
    Ventana de prueba para el reloj digital.

    Hereda de QMainWindow y de la interfaz generada Ui_Test.
    """
    def __init__(self):
        """Inicializa la ventana de prueba."""
        super().__init__()
        self.setupUi(self)

        # Instancia el reloj digital
        self.clock = DigitalClock(self)
        self.vcVerticalLayout.insertWidget(0, self.clock)

 # Configura los eventos de la interfaz
        self.vcTimeEdit.setTime(QTime.currentTime().addSecs(60))  # Establece la hora actual + 1 minuto
        self.vcChck12H.toggled.connect(self.toggle_format)  # Conecta el checkbox de formato
        self.vcBtnActivar.clicked.connect(self.activate_alarm)  # Conecta el botón de activar alarma
        self.vcBtnDesactivar.clicked.connect(self.deactivate_alarm)  # Conecta el botón de desactivar alarma
        self.clock.alarm_triggered.connect(self.show_alarm_message)  # Conecta la señal de alarma

    def toggle_format(self, checked):
        """
        Cambia el formato del reloj entre 12 y 24 horas.

        Args:
            checked (bool): Estado del checkbox (True = formato de 12 horas).
        """
        self.clock.set_12_hour_format(checked)

    def activate_alarm(self):
        """Activa la alarma con los valores configurados en la interfaz."""
        time = self.vcTimeEdit.time()
        message = self.vcMensajeTxt.toPlainText()
        self.clock.set_alarm(True, time.hour(), time.minute(), message)
        self.vcLblMensaje_2.setText(f"Alarma configurada para {time.toString('HH:mm')}")

    def deactivate_alarm(self):
        """Desactiva la alarma."""
        self.clock.set_alarm(False, 0, 0, "")
        self.vcLblMensaje_2.setText("Alarma desactivada")

    def show_alarm_message(self, message):
        """
        Muestra el mensaje de la alarma cuando se activa.

        Args:
            message (str): Mensaje de la alarma.
        """
        time = self.vcTimeEdit.time().toString('HH:mm')
        self.vcLblMensaje_2.setText(f"Alarma '{message}' activada a las {time}")