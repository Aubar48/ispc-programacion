"""
Desafío. Observa que tanto en las relaciones de composición, como de
agregación se considera la multiplicidad. Investiga ¿qué significa ésto? y
¿cómo se representa?
"""




"""

La multiplicidad en el contexto de relaciones de composición y agregación en UML se refiere a cuántos objetos de una clase están asociados con otro objeto de otra clase. Es una medida de la cantidad de instancias que pueden estar relacionadas entre sí según el tipo de relación establecido en el diagrama UML.

La multiplicidad se representa en un diagrama UML mediante notaciones específicas que indican la cantidad de instancias que pueden estar involucradas en una relación. Se representan utilizando números o rangos, y pueden ser expresados de diferentes maneras según el tipo de relación y la cardinalidad de la asociación.

Aquí tienes una breve explicación de cómo se representan:

Notación de Un solo número: Se utiliza un solo número para representar la multiplicidad exacta de instancias que pueden estar involucradas en la relación. Por ejemplo, "1" significa que solo puede haber una instancia, "0..1" significa que puede haber cero o una instancia.
Notación de Rango: Se utiliza un rango para representar la multiplicidad. Por ejemplo, "0..*" significa que puede haber cero o más instancias, mientras que "1..5" significa que puede haber entre 1 y 5 instancias.
Notación de Rango Ilimitado: Se utiliza un asterisco () para indicar que la multiplicidad es ilimitada en un extremo. Por ejemplo, "1.." significa que puede haber al menos una instancia, pero puede haber infinitas.
La multiplicidad también puede ser bidireccional, lo que significa que se puede especificar la cantidad de instancias en ambas direcciones de la relación.

En resumen, la multiplicidad en UML especifica cuántas instancias de una clase están relacionadas con otras clases en una relación determinada, y se representa mediante números, rangos o símbolos especiales en un diagrama UML.

"""