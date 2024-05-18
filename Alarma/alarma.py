import os
import time
from playsound import playsound
from colorama import init, Fore, Style

init(autoreset=True)  # Inicializa Colorama y configura para que los estilos se reseteen automáticamente

def alarma(minutes, seconds):
    sound_path = os.path.join(os.path.dirname(__file__), 'audio.wav')
    total_seconds = minutes * 60 + seconds

    print(Fore.YELLOW + f'Alarma programada para sonar en {minutes} minutos y {seconds} segundos')

    time.sleep(total_seconds)

    playsound(sound_path)

minutos = int(input(Fore.GREEN + 'Ingrese los minutos de la alarma: '))
segundos = int(input(Fore.GREEN + 'Ingrese los segundos de la alarma: '))
alarma(minutos, segundos)

