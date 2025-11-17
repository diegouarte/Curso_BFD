# Atividade dia 17 de novembro de 2025.

# Questão 1: crie uma classe Carro com método mostrar_estado() que imprima
# o valor atual doa tribudo estado, teste com dois caros.

class Carro():
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado
carro1 = Carro('Celta', 'Novo')
carro2 = Carro('Ferrari', "Seminovo")

print(f'Carro: {carro1.nome} \nEstado: {carro1.estado}')
print(f'Carro: {carro2.nome} \nEstado: {carro2.estado}')

#Questão 2: Crie uma classe Motor com o atributo ligado = False. Adicione método
#ligar_motor() e mude o estado para true.

class Motor:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True 

maquina = Motor()
maquina.ligar()
print(maquina.ligado)

#Questão 3: Crie uma classe Banco com atributos clientes (lista). Adicione 3 
# nomes à lista e imprima todos.

class Banco:
    def clientes(self):
        self.nomes = []
                
nomes = Banco()
nomes.clientes = "joao, jonas, diego"
print(nomes.clientes)

#Questão 4: Crie uma classe Produto com método desconto(percentual) que reduz o preço. 
# Teste com um valor de 10%.

class Produto:
    def __init__(self):
        self.preco = 1200

    def desconto(self, percentual):
        self.preco -= self.preco * percentual /100
        print(self.preco)

geladeira = Produto()
geladeira.desconto(10)

# Questão 5: Crie uma classe pessoa com método __init__ que mostra uma mensagem
# "pessoa criada". crie ddois objetos e veja o resultado.

class Pessoa:
    def falar(self):
        print("pessoa criada!")

humano1 = Pessoa()
humano2 = Pessoa()
humano1.falar()
humano2.falar()

#Questão 6: Crie uma função (a,b) que retorne a soma de dois numeros

class Conta:
    def soma(self, n1, n2):
        return float(n1 + n2)
    
mat = Conta()
print(mat.soma(13.5, 44))

#Questão 7: Crie uam questão soma pares(lista) que retorne a soma apeans dos numeros pares

def somapares(lista):
    return sum(n for n in lista if n % 2 == 0)





