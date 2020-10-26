"""
POO - Classes

Em POO classes nada mais são que objetos do mundo real representados computacionalmente.

Classes pode conter: 
    * Atributos -> Representam as características e os estados do objeto. Ou seja, pelos atributos conseguimos representar computacionalmente os estados do objeto. No caso da lâmpada necessário identificar se ela é 110 ou 220 volts, qual a cor e qual luminosidade, ou se ela está ligada e desligada.

    * Métodos (funções) -> Representam os comportamentos do objeto. As ações que este objeto pode realizar no sistema, no caso da lâmpada, um comportamento comum que muito provavelmente iríamos querer representar no sistema, é o de ligar e desligar.



OBS: QUando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos que serão mapeados para classes de Entidades.
"""

class Lampada:
    pass

lamp = Lampada()

print(type(lamp))
