"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, atributos nós conseguimos representar computacionalmente os estados de um objeto.

Dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;


# Atributos de Instância: São atributos declarados dentro do método construtor.

** Todo atributo de uma classe é público, e pode ser acessado em todo o projeto. Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja que deve ser acessado/utilizado somente dentro da própria classe  onde está declarada, utiliza-se __ duplo underscore no início do seu nome.

Isso é conhecido também como Name Mangling.

OBS: Método construtor: É um modelo espacial utilizado para construção do objeto.



# Underscore __ é necessário lembrar que isso é apenas uma convenção, ou seja a linguagem Python não vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo: 

user = Acesso('user@gmail.com', '123456')

print(user.email) # Visualiza normalmente pois não tem underscore.
print(user.__senha) # AtributeError Object not found
# print(dir(user)) Identificação da classe e dos atributos da classe Acesso.
print(user._Acesso__senha) # Temos acesso mas não deveríamos fazer esse acesso. (Name Mangling)

# Atributos de Instância: A característica é que quando criamos instâncias/objetos de uma classe, todas as instâncias serão atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de classes


# Atributos de classes, são atributos declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor é um compartilhado entre todas as instâncias da classe; ou seja, ao invés de cada instância da classe ter seus próprios valores, como é o caso dos atributos de instância. Com os atributos de classe, todas as instâncias terão o mesmo valor para esse atributo.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Vídeo Game', 4500)

print(p1.valor) # Acesso possível mas incorreto
print(p2.valor) # Acesso passível mas incorreto

# OBS: Não precisamos criar uma instância de uma classe, para fazer acesso a um atributo de classe.

print(Produto.imposto)
print(p1.id)
print(p2.id)


"""


# Classes com Atributo de Instância Público

class Lampada: 
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


"""class Produto: 
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor"""

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos Públicos e Atributos Privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# Refatorando a classe produto.

class Produto:
    #Atributo de classe 
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id 

# Atributos Dinâmicos -> Atributo de instância que pode ser criado em tempo de execução
# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg' # Não existe na classe Produto

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)
#print(Produto.__dict__)
del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)