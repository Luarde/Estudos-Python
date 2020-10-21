""" 
Funções com parametros (de entrada)
def quadrado(numero):
    #return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

def cantarParabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vidaaaaa. ')
    print(f'Congratules {aniversariante}!')


cantarParabens('Batman')
"""
#

def somaImpares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7] 
print(somaImpares(lista))           
