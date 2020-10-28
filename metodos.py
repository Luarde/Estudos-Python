"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto, ou seja as ações que este objeto pode realizar no seu sistema. 

Em Python dividimos os métodos em 2 grupos: Métodos de instância e métodos de classe.

# Métodos de classe


# Métodos de instância
*** O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe.
>>> OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)
>>> OBS: Os métodos/funções dunder em Python são chamados métodos mágicos
>>> OBS:Métodos são escritos em letras minúsculas, se nome for composto, as palavras serão separadas por underline.
nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere... ')
    exit(1)

print('Usuário criado com sucesso!!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso Permitido...')
else:
    print('Acesso Negado!')

print(f'Senha user Criptografada: {user._Usuario__senha}')



# Métodos de classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

Usuario.conta_usuarios()

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:  

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor 
        Produto.contador = self.__id   

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""    
        return(self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema.')
    
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False    
    
    def __gera_usuario(self):
        return self.__email.split('@')[0]

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com','123456')

