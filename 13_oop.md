# POO en Python:🐍 De Principiante 👶 a Héroe 🦸

Introducción
La Programación Orientada a Objetos (POO) es un paradigma de programación fundamental para el desarrollo de software complejo. En este curso, exploraremos los conceptos básicos de POO y cómo se aplican en Python.

Conceptos Básicos de POO
Objetos
Un objeto es una entidad que encapsula datos (atributos) y comportamiento (métodos). Los objetos se crean a partir de clases, que son como planos o plantillas.

Clases
Una clase define la estructura y funcionalidad de un tipo de objeto. Contiene atributos y métodos que describen las características y el comportamiento de los objetos de esa clase.

Atributos
Los atributos son variables que almacenan datos asociados a un objeto. Se definen dentro de la clase y se acceden a ellos utilizando la notación de punto.

Métodos
Los métodos son funciones definidas dentro de una clase que operan sobre los atributos de los objetos. Se invocan utilizando la notación de punto y pueden recibir argumentos.

Creación y Uso de Objetos
Creando Instancias
Para crear un objeto a partir de una clase, se utiliza la palabra clave **init** (constructor) que se llama automáticamente cuando se crea un objeto. En Python, no se utiliza new, simplemente se llama a la clase. Cada objeto creado es una instancia única de la clase.

Accediendo a Atributos
Se acceden a los atributos de un objeto utilizando la notación de punto. Por ejemplo, objeto.atributo.

Invocando Métodos
Se invocan métodos de un objeto utilizando la notación de punto seguida del nombre del método y argumentos entre paréntesis. Por ejemplo, objeto.metodo(argumento1, argumento2).

Encapsulación
La encapsulación es el mecanismo para ocultar la implementación interna de una clase y solo exponer los métodos y atributos necesarios para su uso. Promueve la modularidad y protege los datos internos de modificaciones accidentales.

Niveles de Acceso
Python no tiene modificadores de acceso estrictos como público, privado y protegido. Se pueden simular utilizando convenciones:

Público: atributos y métodos sin guiones bajos iniciales.
Privado: atributos y métodos con un guion bajo inicial (\_).
Protegido: atributos y métodos con dos guiones bajos iniciales (\_\_).
Herencia
La herencia permite crear clases que heredan atributos y métodos de otras clases existentes (clases base). Promueve la reutilización de código y la organización jerárquica de clases.

Clases Base y Subclases
Una clase que hereda de otra se denomina subclase. La subclase hereda todos los atributos y métodos públicos de la clase base. Se puede extender o modificar la funcionalidad heredada en la subclase.

Polimorfismo
El polimorfismo permite que objetos de diferentes clases respondan al mismo mensaje de manera diferente. Se basa en la sobreescritura de métodos en clases derivadas.

Métodos Sobreescritos
Cuando una subclase define un método con el mismo nombre que un método heredado de la clase base, se produce una sobreescritura. La subclase proporciona su propia implementación del método, redefiniendo el comportamiento heredado.

Abstracción
La abstracción se centra en las características esenciales de un objeto o proceso, ignorando detalles de implementación. Permite crear clases que definen interfaces sin proporcionar implementaciones completas.

Clases Abstractas
Python no posee clases abstractas como tal, pero se puede simular su comportamiento mediante clases base que definen métodos sin implementar (usando pass). Las subclases deben implementar estos métodos para proporcionar funcionalidad completa.

Ejemplos Prácticos
Creando una Clase de Vehículo
Python

class Vehiculo:
def **init**(self, marca, modelo, color):
self.marca = marca
self.modelo = modelo
self.color = color

    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")

    def acelerar(self):
        print(f"El vehículo {self.marca} {self.modelo} está acelerando.")

    def frenar(self):
        print(f"El vehículo {self.marca} {self.modelo} está frenando.")

miAuto = Vehiculo("Toyota", "Corolla", "Azul")
miMoto = Vehiculo("Honda", "CBX", "Negra")

# Accionando los métodos de los objetos:

miAuto.arrancar()
miMoto.acelerar()
miAuto.frenar()
Explicación
Se agregó un constructor **init** que inicializa los atributos marca, modelo y color del objeto cuando se crea una instancia. Se definieron tres métodos públicos: arrancar(), acelerar() y frenar(). Estos métodos imprimen mensajes utilizando f-strings para incorporar los valores de los atributos.

Herencia
Se crearon dos clases herederas: Auto y Camioneta. Ambas heredan de la clase Vehiculo. Los constructores de Auto y Camioneta utilizan super().**init**(marca, modelo, color) para llamar al constructor de la clase padre e inicializar sus atributos heredados.

Polimorfismo
Observa cómo el mismo método (acelerar()) produce diferentes resultados en objetos de diferentes clases (Auto y Camioneta).

Utilizando Aserciones (opcional)
Si utilizas un marco de pruebas, puedes incluir aserciones para verificar el comportamiento esperado de forma más robusta. Por ejemplo:

self.assertEqual(auto1.acelerar(), "El auto Ford Fiesta acelera rápidamente!")
self.assertEqual(camioneta1.acelerar(), "La camioneta Toyota Hilux acelera con potencia.")
Teoría

Objetos: Un objeto es una entidad que tiene propiedades y comportamientos. En Python, los objetos se crean a partir de clases.
Clases: Una clase es un molde o plantilla que define la estructura y el comportamiento de un objeto. En Python, las clases se definen utilizando la palabra clave class.
Atributos: Un atributo es una propiedad o característica de un objeto. En Python, los atributos se definen utilizando la notación de punto (objeto.atributo).
Métodos: Un método es un bloque de código que se ejecuta cuando se llama a un objeto. En Python, los métodos se definen utilizando la notación de punto (objeto.metodo()).
Herencia: La herencia es la capacidad de una clase de heredar comportamientos de otra clase. En Python, la herencia se logra utilizando la palabra clave class y la notación de punto (super().**init**()).
Polimorfismo: El polimorfismo es la capacidad de un objeto de responder a diferentes tipos de mensajes. En Python, el polimorfismo se logra utilizando métodos con el mismo nombre pero con diferentes implementaciones.
Abstracción: La abstracción es la capacidad de un objeto de definir un comportamiento sin proporcionar implementaciones completas. En Python, la abstracción se logra utilizando clases abstractas y métodos abstractos.
Encapsulación: La encapsulación es la capacidad de un objeto de proteger sus datos internos y solo exponer los métodos y atributos necesarios para su uso. En Python, la encapsulación se logra utilizando getters y setters.
Práctica

Ejemplo 1: Crear una clase de vehículo
class Vehiculo:
def **init**(self, marca, modelo, color):
self.marca = marca
self.modelo = modelo
self.color = color

    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")

    def acelerar(self):
        print(f"El vehículo {self.marca} {self.modelo} está acelerando.")

    def frenar(self):
        print(f"El vehículo {self.marca} {self.modelo} está frenando.")

miAuto = Vehiculo("Toyota", "Corolla", "Azul")
miAuto.arrancar()
miAuto.acelerar()
miAuto.frenar()
Ejemplo 2: Crear una clase de persona
class Persona:
def **init**(self, nombre, edad):
self.nombre = nombre
self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

juan = Persona("Juan", 30)
juan.saludar()
Ejemplo 3: Crear una clase de vehículo con herencia
class Vehiculo:
def **init**(self, marca, modelo, color):
self.marca = marca
self.modelo = modelo
self.color = color

    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")

class Coche(Vehiculo):
def **init**(self, marca, modelo, color, cantidad_puertas):
super().**init**(marca, modelo, color)
self.cantidad_puertas = cantidad_puertas

    def abrir_puertas(self):
        print(f"Se abren las {self.cantidad_puertas} puertas del coche.")

miCoche = Coche("Toyota", "Corolla", "Azul", 4)
miCoche.arrancar()
miCoche.abrir_puertas()
