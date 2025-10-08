# Questão 1: Peça o nome do usuário e mostre a mensagem: "Olá, ! Bem-vindo ao Python."

nome = "diego"
print(f"ola, {nome}! bem vindo ao python.")

# Questão 2: Peça dois números e mostre: "A soma de + é = ".

numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))
soma = numero1 + numero2
print(f"a soma de {numero1} + {numero2} é = {soma}")

# Questão 3: Peça a idade e mostre: "Você tem anos."

idade = int(input("digite sua idade: "))
print(f"sua idade é de {idade} anos")

# Questão 4: Peça um produto e um preço e exiba: "O produto custa R$."

produto = input("diga um poduto: ")
preco = float(input("agora diga o valor desse produto: "))
print(f"o {produto} custa {preco} reais")

# Questão 5: Peça o nome e a altura do usuário e exiba: " tem metros de altura."

altura = 1.76
print(f" {nome} tem {altura}m de altura")

# Questão 6: Usando .format(), exiba: "Meu nome é João e tenho 25 anos." (valores devem vir de variáveis).

nome2 = "joao"
idade2 = 25
print("meu nome é {} e tenho {} anos de idade".format(nome2, idade2))

# Questão 7: Usando .format(), peça dois números e exiba: "O produto de {} e {} é {}".

n1 = float(input("digite um numero: "))
n2 = float(input("digite um numero: "))
produto = n1 * n2
print("o produro de {} e {} é {}.".format(n1, n2, produto))

# Questão 8: Usando .format(), mostre a frase: "O aluno {} tirou nota {} na prova.".

aluno = "ander"
nota = 0
print("o aluno {} tirou {} na prova".format(aluno, nota))

# Questão 9: Usando .format(), peça um país e uma capital e exiba: "A capital de {} é {}.".

pais = input("Digite o nome de um país: ")
capital = input("Digite a capital desse país: ")
print("A capital de {} é {}.".format(pais, capital))

# Questão 10: Usando .format(), peça o nome de um filme e o ano e exiba: "O filme {} foi lançado em {}.".

filme = input("diga um filme: ")
ano = int(input("agr diga o seu ano de lançamento: "))
print("o {} foi lançado em {}".format(filme,ano))

# Questão 11: Usando %, exiba: "O valor de PI é aproximadamente %.2f" (3.14159).

pi = 3.14159
print("O valor de PI é aproximadamente %.2f" % pi)

# Questão 12: Usando %, peça um nome e idade e exiba: "Nome: %s | Idade: %d".

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("Nome: %s | Idade: %d" % (nome, idade))

# Questão 13: Usando %, peça uma cidade e um estado e exiba: "Cidade: %s - Estado: %s".

cidade="Sousa"
estado="PB"
print("Cidade: %s - Estado: %s."%(cidade,estado))

# Questão 14: Usando %, peça o nome de um time e o número de títulos e exiba: "%s tem %d títulos"

time="Brasil"
titulos=5
print("O %s tem %d titulos."%(time,titulos))

# Questão 15: Usando %, peça a temperatura e exiba: "Temperatura atual: %.1f °C".

temperatura=float(input("diga a temp atual: "))
print("agora esta fazendo %.1f graus."%(temperatura))

# Questão 16: Peça nome, idade e curso e exiba com f-string: "O aluno tem anos e está matriculado em ."

curso="arquitetura"
print(f"o {aluno} tem {idade2} anos e cursa {curso}.")

# Questão 17: Usando .format(), peça dois valores e exiba a divisão formatada com duas casas decimais.

n1=float(input("diga um numero: "))
n2=float(input("diga outro numero: "))
divisao=n1/n2
print("a divisao de {} e {} é de {:.2f}".format(n1,n2,divisao))

# Questão 18: Usando %, peça três notas e exiba a média com uma casa decimal.

nota=float(input("nota 1: "))
nota2=float(input("nota : "))
nota3=float(input("nota 3: "))
media = ((nota+nota2+nota3)/3)
print("a media é: %.1f ."%(media))

# Questão 19: Monte uma tabela com 3 produtos e preços alinhados usando f-string.

produtos = ("pao", "leite", "biscoito")
precos = (3.0, 5.50, 2.60)
print(f"{'Produto':<8} | {'Preço':>3}")
print("-" * 18)
for produto, preco in zip(produtos, precos):
    print(f"{produto:<8} | R$ {preco:>3.2f}")

# Questão 20: Escreva um programa que peça nome e salário e exiba em formato monetário: "O funcionário recebe RS".

salario=float(input("qual seu salario: "))
print(" o funcionario {} recebe {} de salario liquido".format(nome,salario))