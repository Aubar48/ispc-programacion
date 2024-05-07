"""
Desafío. Considera un sistema de gestión de biblioteca dónde las
instancias posibles son los Libros. Ej. “El principito”. Modela la clase Libro
utilizando los símbolos definidos por el Diagrama de Clases UML
identificando atributos, métodos y sus correspondientes modificadores de acceso.


Sí, en Python es posible heredar de múltiples clases base, lo que se conoce como herencia múltiple. Esto significa que una clase puede heredar atributos y métodos de más de una clase base.

En este ejemplo, la clase C hereda de las clases A y B, lo que le permite acceder a 
los métodos de ambas clases base.

Sin embargo, es importante tener en cuenta que la herencia múltiple puede llevar a
situaciones complicadas de diseño y 
mantenimiento del código. Puede aumentar la complejidad y la posibilidad de conflictos
de nombres o ambigüedad en el código. Es recomendable usarla con moderación y tener 
en cuenta los principios de diseño de clases para mantener un código claro y fácil de
entender.
Por ejemplo, considera el siguiente caso:
"""

class A:
    def metodo_A(self):
        print("Método de clase A")

class B:
    def metodo_B(self):
        print("Método de clase B")

class C(A, B):
    pass

instancia_C = C()
instancia_C.metodo_A()  # Salida: Método de clase A
instancia_C.metodo_B()  # Salida: Método de clase B
