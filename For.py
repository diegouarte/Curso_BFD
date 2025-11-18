# Questao 01: Imprimir números de 1 a 10

for i in range(1, 11):
    print(i)

# Questao 02: Números pares de 1 a 20

for i in range(0, 22, 2):
    print(i)

# Questao 03:

for i in range(1, 11):
    print(i)

# Questao 04: Tabuada do 5

i = 1
tabuada = 5
for i in range(11):
    print(f"{tabuada}x{i} = {tabuada*i}")
    i += 1

# Questao 05: Tabuada de um número informado

'''i = 1
tabuada = int(input("Digite um numero: "))
for i in range(11):
    print(f"{tabuada}x{i} = {tabuada*i}")
    i += 1'''

# Questao 06: Soma de 1 a 100

i = 0
soma = 0
for i in range(101):
    soma += i
    i += 1
print(soma)
    
# Questao 07: Mostrar caracteres de uma palavra

for letra in "Amigo":
    print(letra)

# Questao 08: Contar vogais em uma palavra

nome = "Diego"
vogais = "aeiou"
i= 0
for letra in nome:
    if letra in vogais:
        i += 1

print(i)

# Questao 09: Média de 10 números

numeros = [2, 6, 9, 55, 10, 25, 30, 11, 3, 4]
soma = 0
for n in numeros:
    soma += n

media = soma / (len(numeros))
print(media)

# Questao 10: Fatorial de um número

n = 6
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(fatorial)

# Questao 11: Contar espaços em uma frase

texto2 = " ola mundo, tudo bom?"
i = 0
for caractere in texto2:
    if caractere == " ":
        i += 1
print(i)

# Questao 12

    #nao tem

# Questao 13: Ler 5 nomes e mostrar em ordem inversa

nomes3 = ["jonas", "dawn", "diego", "jf", "felipe"]
for nomes3 in nomes3[::-1]:
        print(nomes3)

# Questao 14: Maior e menor de 5 notas

n = [2, 6, 9, 55, 10]
maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(menor)
print(maior)

# Questao 15: Números ímpares de 1 a 30

impares = []
for i in range(1, 30):
    if i % 2 != 0:
        impares.append(i)

print(impares)

# Questao 16: Quadrados de 1 a 10

for i in range(1, 11):
    print(i**2)

# Questao 17: Quantos números são positivos entre 5 entradas

n = [2, -6, 9, 55, -10]

for n in n:
    if n >0:
      print(n)

# Questao 18: Palavra invertida

'''palavra = input("digite uma palavra: ")
invertida = " "
for letra in palavra:
    invertida = letra + invertida
print(invertida)'''

# Questao 19: Mostrar apenas os pares entre 10 números

n = [2, 6, 9, 55, 10]

for n in n:
    if n % 2 ==0:
      print(n)

# Questao 20: Lista com 10 elementos e seus índices
# Questao 21: Contar de 10 até 1

for i in range(11)[::-1]:
    print(i)

# Questao 22: Nome com mais letras entre 5
# Questao 23: Soma dos números pares de 1 a 50
# Questao 24: Divisores de um número
# Questao 25: Quantas idades >= 18
# Questao 26: Quantidade de letra 'a' em uma frase
# Questao 27: Fibonacci até o 10º termo
# Questao 28: Maior número ímpar de 5 entradas
# Questao 29: Números de 100 até 50 (decrescente)
# Questao 30: Quantos números negativos entre 10
