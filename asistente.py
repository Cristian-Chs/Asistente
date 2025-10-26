import speech_recognition as sr # Importar la librería de reconocimiento de voz
import pyttsx3 # Importar pyttsx3 para síntesis de voz
import os # Importar os para comandos del sistema
import time # Importar time para pausas
from datetime import datetime # Importar datetime para obtener la fecha y hora
import webbrowser # Importar webbrowser para abrir Google
import urllib.parse # Importar urllib para codificar URLs

def speak(text):
    print(f"🤖 Asistente: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Inicializar el reconocedor
recognizer = sr.Recognizer()


#funciones personalizadas [en proceso]
def youtuber():
    speak("Abriendo YouTube")
    webbrowser.open("https://www.youtube.com")
    time.sleep(5)
    speak("¿Qué deseas buscar en youtuber?")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            busqueda = recognizer.recognize_google(audio, language="es-VE")
            speak(f"Buscando {busqueda} en YouTube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={busqueda}")
        except sr.UnknownValueError:
            speak("No pude entender lo que dijiste para buscar.")
        except sr.RequestError:
            speak("Hubo un problema con el servicio de reconocimiento.")
    

#voz o chat 
def voz_o_chat():
    speak("¿Deseas usar voz o chatear?")
    Decision = input("").lower()
    if "voz" in Decision:
        escuchar_y_responder()


#funcion contar chiste
def contar_chiste():
    import Chistes
    chiste = Chistes.contar_chiste()
    speak(chiste)


#funcion contar cuento
def contar_cuento():
    import cuento
    cuento = cuento.contar_cuento()
    speak(cuento)


def abrir_google():
    speak("Abriendo Google")
    webbrowser.open("https://www.google.com")
    time.sleep(5)
    speak("¿Qué deseas buscar?")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            busqueda = recognizer.recognize_google(audio, language="es-VE")
            speak(f"Buscando {busqueda} en Google")
            webbrowser.open(f"https://www.google.com/search?q={busqueda}")
        except sr.UnknownValueError:
            speak("No pude entender lo que dijiste para buscar.")
        except sr.RequestError:
            speak("Hubo un problema con el servicio de reconocimiento.")

def spotyfy():
    speak("Abriendo Spotify")
    os.startfile("C:\\Users\\Usuario\\AppData\\Roaming\\Spotify\\Spotify.exe") 

def hola():
    speak("¡Hola! ¿Cómo estás?")

def adios():
    speak("Hasta luego, Cristian.")

def hora():
    hora = datetime.now().strftime("%H:%M")
    speak(f"La hora actual es {hora}")  

def fecha():
    fecha = datetime.now().strftime("%d/%m/%Y")
    speak(f"Hoy es {fecha}")    

def apagar():
    speak ("apagando la computador")
    time.sleep(3)
    speak("Adios")
    os.system("shutdown /s /t 1")

def reiniciar():
    speak ("reiniciando la computador")
    time.sleep(3)
    os.system("shutdown /r /t 1")

def suspender():
    speak ("suspendiendo la computador")
    time.sleep(3)
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def word():
    speak("Abriendo Word")
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programss\\Word 2016")

def excel():
    speak("Abriendo Excel")
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel 2016")

def power_point():
    speak("Abriendo Power Point")
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint 2016")

def discord():
    speak("Abriendo Discord")
    os.startfile("C:\\Users\\Usuario\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord")

def chatgpt():
    recognizer = sr.Recognizer()
    speak("¿Qué deseas consultar en ChatGPT?")
    time.sleep(1)
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            busqueda = recognizer.recognize_google(audio, language="es-VE")
            busqueda_codificada = urllib.parse.quote(busqueda)
            speak(f"Buscando {busqueda} en ChatGPT")
            webbrowser.open(f"https://copilot.microsoft.com/search?q={busqueda_codificada}")
            print(busqueda_codificada)
        except sr.UnknownValueError:
            speak("No pude entender lo que dijiste para buscar.")
        except sr.RequestError:
            speak("Hubo un problema con el servicio de reconocimiento.")
    

# Función principal
def escuchar_y_responder():
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            speak("Hola Cristian, soy tu asistente virtual en que te puedo ayudar?, te escucho...")
            print("🎤 Escuchando...")
            audio = recognizer.listen(source)

            try:
                comando = recognizer.recognize_google(audio, language="es-VE")
                print(f"🗣️ Tú dijiste: {comando}")

                # Lógica de respuesta
                if "hola" in comando.lower():
                    hola()

                #Salir del bucle
                elif "adiós" in comando.lower():
                    adios()
                    break

                # Hora actual
                elif "hora" in comando.lower():
                    hora()

                elif "fecha" "Dia" in comando.lower():
                    fecha()

                #Apagar, reiniciar o suspender

                elif "apagar" in comando.lower():
                    apagar()

                elif "reiniciar" in comando.lower():
                    reiniciar()

                elif "suspender" in comando.lower():
                    suspender()
                #Abrir navegador y apps 

                elif "word" in comando.lower():
                    word()
                
                elif "excel" in comando.lower():
                    excel()  

                elif "power point" in comando.lower(): 
                    power_point()

                elif "discord" in comando.lower():
                    discord()

                elif "spotify" in comando.lower():
                    speak("No puedo abrir Spotify, ya que la carpeta esta protejida")

                elif "abrir google" in comando.lower():
                    abrir_google()

                elif "youtube" in comando.lower():
                    youtuber()

                elif "chat g p t" in comando.lower() or "chat gpt" in comando.lower() or "chat" in comando.lower():
                    chatgpt()
                # Contar chistes o cuentos
                elif "chiste" in comando.lower():
                    contar_chiste()
                
                elif "cuento" in comando.lower():
                    contar_cuento()

                elif "figma" in comando.lower():
                    speak("Abriendo Figma")
                    os.startfile("C:\\Users\\Usuario\\AppData\\Local\\Programs\\Figma\\Figma.exe")

                #probar nuevamente la escucha (Mantenimiento)
                elif "intentar de nuevo" in comando.lower():
                    responder()

                else:
                    speak("No entendí bien, ¿puedes repetir?")

            except sr.UnknownValueError:
                speak("No pude entender lo que dijiste.")
            except sr.RequestError:
                speak("Hubo un problema con el servicio de reconocimiento.")

# Ejecutar
if __name__ == "__main__":
    while True:
        escuchar_y_responder()


def responder():
    speak("Deseas algo mas, te escucho...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Escuchando...")
        audio = recognizer.listen(source)

        try:
            comando = recognizer.recognize_google(audio, language="es-VE")
            print(f"🗣️ Tú dijiste: {comando}")

            if "sí" in comando.lower() or "si" in comando.lower():
                escuchar_y_responder()
            elif "no" in comando.lower():
                speak("Hasta luego, Cristian.")
                return
            else:
                speak("No entendí bien, ¿puedes repetir?")
                responder()

        except sr.UnknownValueError:
            speak("No pude entender lo que dijiste.")
            responder()
        except sr.RequestError:
            speak("Hubo un problema con el servicio de reconocimiento.")
            responder()


