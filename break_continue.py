# Questão 01: Crie um loop for de 1 a 10 e use break para parar quando o número for 5.
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# Questão 2:	Use continue para imprimir apenas números ímpares de 1 a 10
for i in range(1, 11):
    if i % 2 ==0:
        continue 
    print(i)

# Questão 03 Faça um while que conte de 1 a 20, mas pare o loop quando o número for maior que 15.

numero = 0
while numero <21:
    if numero > 14:
        break
    numero +=1
    print(numero)

# Questão 04: Crie uma lista de nomes e use continue para pular os nomes que começam com “A”.

lista = ["bola", "agua", "arvore", "camaleao", "lapis"]
for letra in lista:
    if letra[0] == "A" or letra[0] == "a":
        continue
    print(letra)

# Questão 05: Faça um loop for de 10 a 1 e use break quando chegar em 7.

for i in range(11)[::-1]:
    if i == 6:
        break
    print(i)

# Questão 06: Conte de 1 a 15 usando while, mas ignore os múltiplos de 3 usando continue

i = 0
while i == 15:
    if i % 3 == 1:
        continue
    i += 1
    print(i)

# Questão 07: Crie uma lista de números e use break para sair do loop quando encontrar o número 50.

numeros = [1, 30, 50, 45, 9, 100]
for i in numeros:
    if i == 50:
        print('Número 50 encontrado.')
        break
    print(i)

# Questão 08: Faça um loop que percorra números de 1 a 20 e use continue para pular os números pares.

for n in range(1, 21):
    if n % 2 == 0:
        continue
    print(n)

# Questão 09: Escreva um for que percorra uma lista de frutas e pare (break) quando encontrar “banana”.

frutas = ['Maçã', 'uva', 'pera', 'abacaxi',
          'mamão', 'banana', 'goiaba', 'melancia']
for i in frutas:
    if i == 'banana':
        print('Banana encontrada')
        break
    print(i)

# Questão 10: Faça um while que leia números do usuário até que ele digite 0, e use break para sair.

from time import sleep
cont = 0
while True:
    n = int(input('Digite um número [0 para sair]: '))
    cont += 1
    if n == 0:
        print('Encerando...')
        sleep(1)
        break
print('Programa encerrado.')

# Questão 11:Crie um loop que conte de 1 a 10 e use continue para pular o número 5.

for n in range(1, 11):
    if n == 5:
        continue
    print(n)

# Questão 12: Percorra uma lista de palavras e use continue para pular palavras com mais de 5 letras.

palavras = ['Arroz', 'cachorro', 'paralelepípedo',
            'gato','Mouse', 'teclado', 'maçã', 'cubo']
for i in palavras:
    if len(i) > 5:
        continue
    print(i)

# Questão 13: Faça um for que percorra números de 1 a 50 e pare (break) ao encontrar o primeiro múltiplo de 7.

for n in range(1, 51):
    if n % 7 == 0:
        print('Múltiplo de 7 encontrado.')
        break
    print(n)

# Questão 14: Use continue em um loop que vai de 1 a 20 para imprimir apenas os números menores que 10

for n in range(1, 20):
    if n >= 10:
        continue
    print(n)

# Questão 15: Crie um while que some números de 1 a 100, mas pare (break) se a soma ultrapassar 50.

soma = 0
cont = 0
while cont <= 100:
    cont += 1
    soma += cont
    if soma > 50:
        break
    print(soma)

# Questão 16: Faça um loop for que percorra uma lista de notas e use continue para ignorar notas menores que 5.

notas = [7.0, 9.0, 4.0, 8.0, 4.7,]
for i in notas:
    if i < 5:
        continue
    print(i)

# Questão 17: Crie um loop que conte de 1 a 30 e use break quando encontrar o número 25.

for n in range(1, 31):
    if n == 25:
        break
    print(n)

# Questão 18: Use continue para imprimir somente as letras maiúsculas de uma string.

texto = 'BacK eNd PytHon'
for i in texto:
    if not i.isupper():
        continue
    print(i)

# Questão 19: Faça um while que leia palavras do usuário e pare (break) quando ele digitar “sair”.

cont = 0
palavra = 0
while True:
    cont += 1
    palavra = str(input('Digite qualquer palavra ["sair" pra encerrar]: '))
    if palavra == 'sair':
        break

# Questão 20: Crie um loop que percorra números de 1 a 10 e use continue para pular os números múltiplos de 2.

for n in range(1, 11):
    if n % 2 == 0:
        continue
    print(n)

# Questão 21: Percorra uma lista de inteiros e use break se encontrar um número negativo.

numeros = [12, 15, 25, 10, -3, 8, 9, 7]
for i in numeros:
    if i < 0:
        break
    print(i)

# Questão 22: Faça um for que percorra os dias da semana e use continue para pular o domingo.

dias = ['Domingo', 'Segunda', 'Terça',
        'Quarta', 'Quinta', 'Sexta', 'Sábado']
for i in dias:
    if i == 'Domingo':
        continue
    print(i)

# Questão 23:Crie um loop while de 1 a 15 e use continue para não imprimir números múltiplos de 4.

cont = 1
while cont <= 15:
    cont += 1
    if cont % 4 == 0:
        continue
    print(cont)

# Questão 24: Percorra uma lista de cidades e use break se encontrar “Paris”.

cidades = ['Madrid', 'Washington', 'Paris', 'Tokyo']
for i in cidades:
    if i == 'Paris':
        break
    print(i)

# Questão 25: Crie um for que percorra números de 1 a 20 e use continue para pular números maiores que 15.

for n in range(1, 21):
    if n > 15:
        continue
    print(n)

# Questão 26: Faça um loop while que conte de 1 a 10 e use break quando chegar no número 8.

n = 0
while n <= 10:
    n += 1
    if n == 8:
        break
    print(n)

# Questão 27: Faça um loop while que conte de 1 a 10 e use break quando chegar no número 8.
frutas = ['Maçã', 'Pera', 'Uva', 'Kiwi']
for i in frutas:
    if 'a' in i or 'A' in i:
        continue
    print(i)

# Questão 28: Faça um loop que percorra números de 1 a 30 e use break ao encontrar um número divisível por 13.

for n in range(1, 31):
    if n % 13 == 0:
        break
    print(n)

# Questão 29: Crie um for que percorra uma lista de nomes e use continue para ignorar nomes que tenham menos de 4 letras.

nomes = ['Ana', 'Alceu', 'Bia', 'Arthur',
         'Pedro', 'Felipe', 'João']
for i in nomes:
    if len(i) < 4:
        continue
    print(i)

# Questão 30: aça um loop while que conte de 1 a 50, mas use continue para não imprimir números múltiplos de 5.

cont = 0
while cont <= 49:
    cont += 1
    if cont % 5 == 0:
        continue
    print(cont)
    