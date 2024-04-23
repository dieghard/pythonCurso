# POO en Python: De Principiante 👶 a HEROE 🏋️

## Introducción

> La Programación Orientada a Objetos (POO) es un paradigma de programación fundamental para el desarrollo de software complejo. veremos paso a paso desde los conceptos básicos hasta técnicas avanzadas.

## Conceptos Básicos de POO

### Objetos:

- Un objeto es una entidad que encapsula datos (atributos) y comportamiento (métodos).
  \*Los objetos se crean a partir de clases, que son como planos o plantillas.

### Clases:

Una clase define la estructura y funcionalidad de un tipo de objeto.
Contiene atributos y métodos que describen las características y el comportamiento de los objetos de esa clase.

### Atributos:

Los atributos son variables que almacenan datos asociados a un objeto.
Se definen dentro de la clase y se accede a ellos utilizando la notación de punto.

### Métodos:

Los métodos son funciones definidas dentro de una clase que operan sobre los atributos de los objetos.
Se invocan utilizando la notación de punto y pueden recibir argumentos.

## Creación y Uso de Objetos

### Creando Instancias:

Para crear un objeto a partir de una clase, se utiliza la palabra clave new seguida del nombre de la clase y argumentos entre paréntesis. En Python, no se utiliza new, simplemente se llama a la clase.
Cada objeto creado es una instancia única de la clase.

### Accediendo a Atributos:

Se accede a los atributos de un objeto utilizando la notación de punto.
Por ejemplo, objeto.atributo.

### Invocando Métodos:

Se invocan métodos de un objeto utilizando la notación de punto seguida del nombre del método y argumentos entre paréntesis.
Por ejemplo, objeto.metodo(argumento1, argumento2). 3. Encapsulación

### Definición:

> La encapsulación es el mecanismo para ocultar la implementación interna de una clase y solo exponer los métodos y atributos necesarios para su uso.
> Promueve la modularidad y protege los datos internos de modificaciones accidentales.

### Niveles de Acceso:

Si bien Python no tiene modificadores de acceso estrictos como public, private y protected, se pueden simular usando convenciones:
Público: atributos y métodos sin guiones bajos iniciales.
Privado: atributos y métodos con un guion bajo inicial (\_). En la práctica, se desaconseja su uso estricto, ya que los elementos privados siguen siendo accesibles desde la clase.
Protegido: atributos y métodos con dos guiones bajos iniciales (\_\_). Se utiliza para elementos internos destinados a ser usados por subclases.

# Herencia

### Definición:

> La herencia permite crear clases que heredan atributos y métodos de otras clases existentes (clases base).
> Promueve la reutilización de código y la organización jerárquica de clases.

### Clases Base y Subclases:

Una clase que hereda de otra se denomina subclase.
La subclase hereda todos los atributos y métodos públicos de la clase base.
Se puede extender o modificar la funcionalidad heredada en la subclase.

# Polimorfismo

### Definición:

> El polimorfismo permite que objetos de diferentes clases respondan al mismo mensaje de manera diferente.
> Se basa en la sobreescritura de métodos en clases derivadas.

### Métodos Sobreescritos:

Cuando una subclase define un método con el mismo nombre que un método heredado de la clase base, se produce una sobreescritura.
La subclase proporciona su propia implementación del método, redefiniendo el comportamiento heredado. 6. Abstracción

### Definición:

> La abstracción se centra en las características esenciales de un objeto o proceso, ignorando detalles de implementación.
> Permite crear clases que definen interfaces sin proporcionar implementaciones completas.

### Clases Abstractas:

Python no posee clases abstractas como tal, pero se puede simular su comportamiento mediante clases base que definen métodos sin implementar (usando pass).
Las subclases deben implementar estos métodos para proporcionar funcionalidad completa.

## Ejemplos Prácticos

### Creando una Clase de Vehículo:

Python

```
class Vehiculo:
  def __init__(self, marca, modelo, color):
    self.marca = marca  # Atributo público
    self.modelo = modelo  # Atributo público
    self.color = color  # Atributo público

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

```

### Explicación:

> Se agregó un constructor **init** que inicializa los atributos marca, modelo, y color del objeto cuando se crea una instancia. Se definieron tres métodos públicos: arrancar(), acelerar(), y frenar(). Estos métodos imprimen mensajes utilizando f-strings para incorporar los valores de los atributos.

```
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

class Auto(Vehiculo):
    def __init__(self, marca, modelo, color, cantidad_puertas):
        super().__init__(marca, modelo, color)  # Llamada al constructor de la clase padre
        self.cantidad_puertas = cantidad_puertas

    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} acelera rápidamente!")  # Sobreescritura

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, color, capacidad_carga):
        super().__init__(marca, modelo, color)
        self.capacidad_carga = capacidad_carga

    def acelerar(self):
        print(f"La camioneta {self.marca} {self.modelo} acelera con potencia.")  # Sobreescritura

auto1 = Auto("Ford", "Fiesta", "Rojo", 5)
camioneta1 = Camioneta("Toyota", "Hilux", "Plateada", 1000)
auto1.acelerar()
camioneta1.acelerar()

```

### Explicación:

> Se crearon dos clases herederas: Auto y Camioneta.
> Ambas heredan de la clase Vehiculo.
> Los constructores de Auto y Camioneta utilizan super().**init**(marca, modelo, color) para llamar al constructor de la clase padre e inicializar sus atributos heredados.
> Se agregaron atributos específicos a cada clase: cantidad_puertas para Auto y capacidad_carga para Camioneta.
> Se sobrescribió el método acelerar() en ambas subclases para proporcionar un comportamiento personalizado de acuerdo al tipo de vehículo.

## Verificar el polimorfismo:

> Observa cómo el mismo método (acelerar()) produce diferentes resultados en objetos de diferentes clases (Auto y Camioneta).

## Probar los atributos:

Accede a los atributos de las instancias para verificar su valor correcto:

```
print(f"Auto: {auto1.marca} {auto1.modelo} - Puertas: {auto1.cantidad_puertas}")
print(f"Camioneta: {camioneta1.marca} {camioneta1.modelo} - Carga: {camioneta1.capacidad_carga}")
```

## Utilizar aserciones (opcional):

> Si utilizas un marco de pruebas, puedes incluir aserciones para verificar el comportamiento esperado de forma más robusta. Por ejemplo:

```
self.assertEqual(auto1.acelerar(), "El auto Ford Fiesta acelera rápidamente!")
self.assertEqual(camioneta1.acelerar(), "La camioneta Toyota Hilux acelera con potencia.")
```
