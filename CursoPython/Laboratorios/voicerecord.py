#INSTALAR pip install sounddevice
#INSTALAR pip install scipy
import sounddevice as sd
from scipy.io.wavfile import write
#sample rate
fs = 44100
second = int(input("Ingrese la cantidad de segundos que desea guardar:"))
print ("...grabando...")
#record
record_voice = sd.rec(int(second * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()
print ("grabación finalizada")
#guardar
write('migrabaciondevoz.wav', fs, record_voice)
print ("archivo guardado, verifique en la carpeta de trabajo")
#fin del programa

