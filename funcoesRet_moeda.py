#Bibliotéca de gerar números pseudo-randômicos.
from random import random


def jogaMoeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogaMoeda())
