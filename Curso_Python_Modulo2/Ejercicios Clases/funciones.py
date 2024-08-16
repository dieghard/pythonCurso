#Nuestas funciones
#Import necesarios para el Laboratorio 1
import pyttsx3
import speech_recognition as sr
from groq import Groq
    
def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hable (tiene 10 segundos): ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=10)
        try:
            prompt = r.recognize_google(audio, language='es-ES')
            print(f"Dijiste: {prompt}")
            return prompt
        except sr.UnknownValueError:
            print("Lo siento, no he podido entender lo que has dicho.")
            return None
        except sr.RequestError as e:
            print(f"Lo siento, ha habido un problema al intentar comunicarme con el servicio de Google: {e}")
            return None
        
def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def interactuar_con_ia(prompt):
    if prompt is None:
        return "No se pudo obtener un prompt válido."
    
    client = Groq(
        api_key="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",
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


def ingresar_numero (texto_input:str|None= "Ingrese un numero:")-> int:
    """
    Funcion para ingresar y validar un numero, \n
    texto_input muestra el mensaje por consola
    """
    while True:
        numero_1 = input (texto_input)
        if numero_1.isdigit():
            numero_1 = int(numero_1)
            return numero_1
        else:
            print("El valor ingresado no es un Nro")
    return 


#Ejemplo 1: Una funcion que salude, teniendo en cuenta que puede tener doble nombre y doble apellido:

def saludo(nombre:str, apellido:str | None = " ")->str:
    print(f"Hola {nombre}{apellido}")
    return 



#Ejemplo 2: Calcular el área de un cuadrado:

def area (lado:int | None = 0)->int:
    return  lado**2

def suma(n_1:int ,n_2:int , n_3:int | None = 0,n_4:int | None = 0)->int:
    """
    Funcion para sumar hasta 4 numeros, en caso de que no se especifique alguno de los 4 se colocará un 0 \n si o si, deberas especificar al menos dos parametros.
    """
    return n_1+n_2+n_3+n_4


def resta(n_1:int | None = 0,n_2:int | None = 0,n_3:int | None = 0,n_4:int | None = 0)->int:
    """
    Funcion para restar hasta 4 numeros, en caso de que no se especifique alguno de los 4 se colocará un 0
    """
    return n_1-n_2-n_3-n_4

def division(n_1:int | None = 0,n_2:int | None = 0,n_3:int | None = 0)->int:
    """
    Funcion para dividir, si se especifica con un 1 en el tercer parametro mostrará tambien el resto
    """
    if n_3 == 1:
        return  n_1 % n_2
    else:
        return n_1 / n_2

#Funcion para validar un numero

def validar_numero()->int:
    """
    Esta funcion retorna un int validado. Hasta que no se ingrese un número
    no va a permitir ingresar otra cosa.
    """
    while True:
        numero_a_validar = input("Ingrese un número:")
        if numero_a_validar.isdigit():
            numero_a_validar = int(numero_a_validar)
            break
        else:
            print ("el dato ingresado no corresponde a un número.")
    return numero_a_validar







def validar_texto(texto_input:str | None="Ingrese un texto: ", validar_vacio : bool| None=False, dato_a_validar :str |None="dato")->str:
    """
    Valida si es un texto. Se puede validar que no quede el dato vacio y se puede pasar que dato valida para mostrar al usuario
    """
    while True:
        texto = input(texto_input)
        if validar_vacio: 
            if texto =="":
                print (f"El {dato_a_validar} no debe quedar vacio!")       
            elif texto.isalpha():
                break
            else:
                print("El dato no corresponde a lo solicitado.")
        else:
            break
    return texto

#